"""
Plotting Functions
________________________________________________________________________
File to store useful plotting functions
"""

import os
import numpy as np
import seaborn as sns
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.metrics import auc


from typing import Tuple


def get_efficiency_and_rejection(y_true: np.ndarray, y_pred: np.ndarray, weights: np.ndarray) -> Tuple[float, float]:
	fpr_keras, tpr_keras, thresholds_keras = metrics.roc_curve(y_true, y_pred, sample_weight=weights)

	fpr_keras.sort()
	tpr_keras.sort()

	# Get AUC
	auc_keras = auc(fpr_keras, tpr_keras)
	print(f"AUC = {auc_keras}")

	nonzero = fpr_keras != 0  # Copies fpr array but removes all entries that are 0
	eff, rej = tpr_keras[nonzero], 1.0 / fpr_keras[nonzero]
	return eff, rej


def plot_ROC(y_true: np.ndarray, y_pred: np.ndarray, weights: np.ndarray=None, title: str="ROC curve", saveas: str=None) -> None:

	eff, rej = get_efficiency_and_rejection(y_true, y_pred, weights)
	
	fig, ax = plt.subplots()
	ax.plot([0, 1], [0, 1], 'k--')
	#plt.plot(fpr_keras, tpr_keras, label='Keras (AUC = {:.3f})'.format(auc_keras))
	ax.plot(eff, rej)#, label='AUC (area = {:.3f})'.format(auc_keras))
	ax.set_xlabel('Signal Efficiency')
	ax.set_ylabel('Background Rejection')
	ax.set_ylim(1e0, 1e4)
	ax.set_yscale("log")
	ax.set_title(title, loc='right', fontsize=5)
	if saveas is not None:
		plt.savefig(saveas)
	else:
		plt.savefig(os.path.join("plots", "ROC.png"))
	plt.show()


# @nb.njit()
def make_confusion_matrix(prediction: np.ndarray, truth: np.ndarray, weights: np.ndarray=None) -> np.ndarray:
	"""
	Function to make the confusion matrix
	Produces a 2D array which can look like this:
				 0      1      2	  3
	P   jets | .... | .... | .... | .... | 0
	R	1p0n | .... | .... | .... | .... | 1
	E	1p1n | .... | .... | .... | .... | 2
	D	1pxn | .... | .... | .... | .... | 3
		 	 | jets | 1p0n | 1p1n | 1pxn
				 T      R      U      E
	
	:param y_pred: Array of neural network predictions
	:param y_true: Correspondin array of truth data
	:param prong (optional, default=None): Number of prongs - determines the axis labels
	leave as None if you are classifiying 1 and 3 prongs together 
	:param weights (optional, default=None): An array of weights the same length and y_true and y_pred
	"""
	
	nclasses = prediction.shape[1]
	cm = np.zeros((nclasses, nclasses), dtype="float32")
	if weights is None:
		weights = np.ones(len(prediction), dtype='float32')

	for pred, true, weight in zip(prediction, truth, weights):
		pred_max_idx = np.argmax(pred)
		truth_max_idx = np.argmax(true)        
		cm[pred_max_idx][truth_max_idx] += weight
	return cm

def get_diag_score(conf_matrix: np.ndarray, del_first: bool=False):

	if del_first:
		np.delete(conf_matrix, 0, axis=0)
		np.delete(conf_matrix, 0, axis=1)

	return np.trace(conf_matrix) / conf_matrix.shape[0]
	
def plot_confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray, prong: int=None, weights: np.ndarray=None, saveas: str=None, title: str="", no_jets: bool=False) -> None:
	"""
	Function to plot confusion matrix
	Makes two plots:
		One where columns are normalised to unity (Each cell corresponds to purity)
		One where rows are normalised to unity (Each cell corresponds to efficiency)
	
	:param y_pred: Array of neural network predictions
	:param y_true: Correspondin array of truth data
	:param prong (optional, default=None): Number of prongs - determines the axis labels
	leave as None if you are classifiying 1 and 3 prongs together 
	:param weights (optional, default=None): An array of weights the same length and y_true and y_pred
	:param saveas (optional, default=None): A filepath to save to
	:param title (optional, default=""): Title of the plot
	:param no_jets (optional, default=False): If True exclude jet catagory from plotting
	"""

	conf_matrix = make_confusion_matrix(y_pred, y_true, weights)

	# Normalise entries to unity
	purity_matrix = conf_matrix / conf_matrix.sum(axis=0, keepdims=1)        # nomalise columns to unity
	efficiency_matrix = conf_matrix / conf_matrix.sum(axis=1, keepdims=1)    # nomalise rows to unity
	
	efficiency_matrix = np.nan_to_num(efficiency_matrix, posinf=0, neginf=0, copy=False).astype("float32")
	purity_matrix = np.nan_to_num(purity_matrix, posinf=0, neginf=0, copy=False).astype("float32")

	fig, (ax1, ax2) = plt.subplots(1,2, figsize=(40,15))

	labels = ["jets", "1p0n", "1p1n", "1pxn", "3p0n", "3pxn"]
	if prong == 1:
		labels = ["jets", "1p0n", "1p1n", "1pxn"]
	if prong == 3:
		labels = ["jets", "3p0n", "3pxn"]
	if no_jets:
		labels.remove("jets")

	xticklabels = labels
	yticklabels = labels
	sns.heatmap(efficiency_matrix, annot=True, cmap="Oranges", xticklabels=xticklabels, yticklabels=yticklabels,
						fmt=".2", vmin=0, vmax=1, ax=ax1, annot_kws={"size": 35 / np.sqrt(len(efficiency_matrix))},)
	sns.heatmap(purity_matrix, annot=True, cmap="Oranges", xticklabels=xticklabels, yticklabels=yticklabels,
						fmt=".2", vmin=0, vmax=1, ax=ax2, annot_kws={"size": 35 / np.sqrt(len(purity_matrix))},)
	# sns.set(font_scale=8) #! Don't do this! Messes with all subsequent plots
	ax1.set_xlabel("Truth", fontsize=18)
	ax1.set_ylabel("Prediction", fontsize=18)
	ax2.set_xlabel("Truth", fontsize=18)
	ax2.set_ylabel("Prediction", fontsize=18)
	ax1.set_title(f"Diagonal Score = {get_diag_score(efficiency_matrix):.2f} Efficiency: {title}", loc='right', fontsize=12)
	ax2.set_title(f"Diagonal Score = {get_diag_score(purity_matrix):.2f} Purity: {title}", loc='right', fontsize=12)
	fig.suptitle(title, fontsize=9)
	if saveas is None:
		plt.savefig(os.path.join("plots", "confusion_matrix.png"))
	else:
		plt.savefig(saveas)
	plt.show()
	plt.clf()
	plt.close(fig)
	
	return np.trace(purity_matrix) / purity_matrix.shape[0]



def plot_1_and_3_prong_ROC(data_1prong, data_3prong, title="ROC curve", saveas=None):

	eff_1prong, rej_1prong = get_efficiency_and_rejection(*data_1prong)
	eff_3prong, rej_3prong = get_efficiency_and_rejection(*data_3prong)

	fig, ax = plt.subplots()
	ax.plot([0, 1], [0, 1], 'k--')
	#plt.plot(fpr_keras, tpr_keras, label='Keras (AUC = {:.3f})'.format(auc_keras))
	ax.plot(eff_1prong, rej_1prong, label="1-Prong")
	ax.plot(eff_3prong, rej_3prong, label="3-Prong")
	ax.set_xlabel('Signal Efficiency')
	ax.set_ylabel('Background Rejection')
	ax.set_ylim(1e0, 1e4)
	ax.set_yscale("log")
	ax.legend()
	ax.set_title(title, loc='right', fontsize=5)
	if saveas is not None:
		plt.savefig(saveas)
	else:
		plt.savefig(os.path.join("plots", "ROC_seperate_prongs.png"))
	plt.show()