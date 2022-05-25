# Unified Tau Classifier

## Description

Development of a combined tau ID and tau decay mode classifier for ATLAS Tau Group

## Enviroment setup

Install miniconda\
  `conda env create -f config/environment.yaml`

## Dataset creation

TODO: Add documentation for THOR code

## Data preparation

To get efficient test/train/val splits data is split up into 100,000 event chunks and to improve network training features are normalised to have mean zero and standard deviation one.\
This part is **still work in progess** but for now do:\
`python3 tools/compute_stats.py` to get a csv of means and std devs\
`python3 tools/uproot_ntuple_writer.py` to write out the files

## How to run

The [Hydra](https://hydra.cc/) package is used to parse command line arguements and manage config settings
To avoid having to shuffle the entire dataset together, sub-batches of data for taus and fakes are loaded seperately and merged to create a complete training batch. To speed this up, the dataloading is run on a pair of parallel python processes using the [Ray](https://www.ray.io/) library.

### Training

To run training do\
`python3 tauclassifier.py learning_rate=1e-4 batch_size=1024`\
Training related options can be found in `config/training_config.yaml`\
Each training run will be saved to its own working directory saved in `outputs/train_output/<date-time>`
Training progress can be tracked through the tensorboard callback; you can launch tensorboard using\
`tensorboard --logdir=outputs/train_output/<date-time>/logs`.\
To run on just a fraction of the full dataset use set the `fraction` option. e.g. to train on 10% of data\
`python3 tauclassifier.py fraction=0.1`

### Evaluation

After training you'll probably want to make some performance plots. To do this 1st run the evaluate function to write out a set of ntuples containing all the features you need to make the plots you want to make.\
`python3 tauclassifier.py run=evaluate`\
This will automatically select the most recently saved weights file\
To select a specific weights file add a `weights` field to config e.g.\
`python3 tauclassifier.py evaluate +weights=<path-to-weights-file>`
The branches of the output file can be customised by modifing the `OutFileBranches` filed in`config/testing_config.yaml`. To configure additional custom branches related to the network predictions you can modify `source/datawriter.py`.

### Visualisation

To plot performance plots from a run \
`python3 tauclassifier.py run=visualise`\
To run on a specific set of evaluated ntuples add `results` field to config e.g.\
`python3 tauclassifier.py run=visualise +results=<path-to-evaluated-ntuples-dir>`\
Options related to evaluation and visualisation steps are found in `config/evaluation_config.yaml`
