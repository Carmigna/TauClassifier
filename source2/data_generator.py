import ray
import tensorflow as tf
from typing import List, Union, Tuple
import numpy as np
import uproot
import awkward as ak
import yaml
import os
from source2.dataloader import RayDataLoader


class DataGenerator(tf.keras.utils.Sequence):

    def __init__(self, tau_files: List[str], jet_files: List[str], yaml_feature_cfg: str, batch_size: int=256, step_size: Union[str, int]='1GB'):

        self.yaml_feature_config = os.path.abspath(yaml_feature_cfg)
        self.dataloaders = []
        self.batch_size = batch_size
        self.step_size = step_size
        self.tau_files = tau_files
        self.jet_files = jet_files

        x = uproot.lazy(self.tau_files, filter_name='TauJets_truthDecayMode', libray='np')
        y = uproot.lazy(self.jet_files, filter_name='TauJets_truthDecayMode', libray='np')


        x = x["TauJets_truthDecayMode"]
        y = y["TauJets_truthDecayMode"]
        self.ntaus = len(x)
        self.njets = len(y)
        self.nevents = self.ntaus + self.njets

        self.tau_batch_size = int((self.ntaus / self.nevents) * self.batch_size)
        self.jet_batch_size = int((self.njets / self.nevents) * self.batch_size)
        
        self.steps_per_epoch = self.nevents // self.batch_size

        self.tau_loader = RayDataLoader.remote(self.tau_files, self.yaml_feature_config, self.tau_batch_size, step_size=self.step_size)
        self.jet_loader = RayDataLoader.remote(self.jet_files, self.yaml_feature_config, self.jet_batch_size, step_size=self.step_size)

    def __getitem__(self, idx: int) -> Tuple[np.ndarray]:
        """
        Allows DataGenerator to be indexable. Not really though since the index does nothing.
        This method is only provided to satify the requirements for tensorflow generator training.
        This should really be treated as __next__
        args:
            idx: int - Does nothing, just provide it as an arguement so that code works
        returns:
            Tuple[np.ndarrays] - A Tuple of arrays; structure is
            feature arrays, labels, weights
        """

        # batch = (next(self.tau_loader), next(self.jet_loader) )
        batch = ray.get([self.tau_loader.next.remote(), self.jet_loader.next.remote()])

        x_batch = []
        for k in range(0, len(batch[0][0])):
            x_batch.append(np.concatenate([x[0][k] for x in batch]))

        y_batch = np.concatenate([result[1] for result in batch])
        weight_batch = np.concatenate([result[2] for result in batch])

        return x_batch, y_batch, weight_batch

    def on_epoch_end(self):
        """
        Just an alias for reset so that Keras knows what to do at the end of the epcoh
        """
        self.reset()
        
    def reset(self) -> None:
        """
        Terminate ray actors and recreate 
        Do this to free memory accumilated by uproot.iterate
        """
        self.tau_loader.terminate.remote()
        self.jet_loader.terminate.remote()
        self.tau_loader = RayDataLoader.remote(self.tau_files, self.yaml_feature_config, self.tau_batch_size, step_size=self.step_size)
        self.jet_loader = RayDataLoader.remote(self.jet_files, self.yaml_feature_config, self.jet_batch_size, step_size=self.step_size)
    

    def __len__(self):
        return self.steps_per_epoch