Synapse E/I Classification from MICrONS EM Images

This repository contains the full workflow for training a deep learning model that predicts the presynaptic identity of neurons (excitatory vs inhibitory) from synapse-centered electron microscopy (EM) image patches extracted from the MICrONS minnie65 dataset.

Project Overview

This project investigates a central question in cortical connectomics:

Can local synaptic ultrastructure alone reveal whether the presynaptic neuron is excitatory or inhibitory?

To answer this, we:

Retrieve synapses from proofread neurons using the MICrONS CAVEclient.

Merge AIBS and Baylor coarse cell-type tables to obtain reliable E/I labels.

Extract synapse-centered EM patches at MIP-0 resolution using CloudVolume.

Split synapses by presynaptic neuron (neuron-held-out) to avoid data leakage.

Train a 2D CNN classifier (PyTorch) to predict E/I identity from single-slice EM images.

Evaluate performance using accuracy, balanced accuracy, ROC, PR curves, and confusion matrices.

Repository Structure
Synapse_Classification_2D/
│
├── Synapse_Classification_2D.ipynb    # Training notebook
├── README.md                          # Project overview
├── data_extraction/                   # (optional) Scripts for CAVEclient extraction
├── results/                           # (optional) Saved metrics and plots
└── models/                            # (optional) PyTorch model definitions


Note: Raw EM imagery and extracted synapse patches are not included in the repository due to MICrONS data licensing. Users must download data using the official CAVEclient.

Model Summary

Architecture: ResNet-based CNN

Input: 2D EM patches, synapse-centered

Labels: Presynaptic neuron identity (excitatory/inhibitory)

Splitting: Neuron-held-out (strict)

Achieved performance:

Accuracy: ~0.83

Balanced Accuracy: ~0.83

F1 Score: High and symmetric across classes

These results indicate that local ultrastructure contains informative but incomplete signatures of presynaptic neuron identity, motivating future extensions to multi-slice or 3D volumetric modeling.

Environment

Install dependencies:

pip install -r requirements.txt


Or using conda:

conda env create -f environment.yml
conda activate synapse-ei

Reference / Citation

If using this code or approach, please cite:

Massoudi, B. (2026).
Learning Presynaptic Excitatory–Inhibitory Neuron Identity from Synapse-Centered Electron Microscopy Using Deep Learning.

About

This project was completed using:

MICrONS minnie65 dataset

AIBS + Baylor cell-type annotations

CAVEclient + CloudVolume

PyTorch / Python

Google Colab for training

Next Steps

Planned extensions include:

Multi-slice synapse volumes

Postsynaptic identity incorporation

Morphological integration

Higher-resolution representations
