

# **Synapse E/I Classification from MICrONS EM Images**

This repository contains the workflow for training a deep learning model that predicts the presynaptic identity of neurons (excitatory vs inhibitory) from synapse-centered electron microscopy (EM) image patches extracted from the MICrONS *minnie65* dataset.

---

## **Project Overview**

This project investigates a fundamental question in cortical connectomics:

**Can local synaptic ultrastructure alone reveal whether the presynaptic neuron is excitatory or inhibitory?**

To address this question, the workflow includes:

* **Retrieving synapses and presynaptic neuron identities** from the MICrONS minnie65 dataset using the official CAVEclient.
* **Using the Allen Institute’s `allen_v1_column_types_slanted_ref` table** to obtain expert-assigned coarse cell-type labels (`aibs_coarse_excitatory` and `aibs_coarse_inhibitory`).
* **Querying synapse metadata** from the `synapses_pni_2` table and inheriting E/I labels using the `pre_root_id` field.
* **Extracting synapse-centered 2D EM patches** (via CloudVolume and ImageryClient workflows).
* **Ensuring neuron-held-out dataset splits** to prevent information leakage across training, validation, and test sets.
* **Training a 2D CNN classifier (PyTorch)** to infer presynaptic identity from single-slice EM images.
* **Evaluating model performance** with accuracy, balanced accuracy, confusion matrices, and ROC/PR curves.

---

## **Repository Structure**

```
Synapse_Classification_2D/
│
├── Synapse_Classification_2D.ipynb    # Main training notebook
├── README.md                          # Project overview (this file)
├── data_extraction/                   # Scripts for data retrieval
├── models/                            # PyTorch model definitions
└── results/                           # Saved metrics and plots
```

> **Note:** Raw EM imagery and extracted synapse patches are *not* included due to MICRONS data licensing.
> Users must download data using the official CAVEclient.

---

## **Model Summary**

* **Architecture:** ResNet-based CNN
* **Input:** Synapse-centered 2D EM patches
* **Labels:** Presynaptic neuron identity (`aibs_coarse_excitatory` vs `aibs_coarse_inhibitory`)
* **Splitting strategy:** Strict **neuron-held-out** partitioning
* **Performance:**

  * **Accuracy:** ~0.83
  * **Balanced Accuracy:** ~0.83
  * **F1 Score:** High and symmetric across classes

These results demonstrate that **local synaptic ultrastructure encodes meaningful but incomplete information** about presynaptic neuron identity, motivating future exploration of multi-slice and 3D volumetric representations.

---

## **Environment**

Install dependencies:

```
pip install -r requirements.txt
```

Or using Conda:

```
conda env create -f environment.yml
conda activate synapse-ei
```

---

## **Reference / Citation**

If using this code or approach, please cite:

**Massoudi, B. (2026).
Learning Presynaptic Excitatory–Inhibitory Neuron Identity from Synapse-Centered Electron Microscopy Using Deep Learning.**

---

## **About**

This project was completed using:

* MICrONS *minnie65* dataset
* Allen Institute neuron classification table (`allen_v1_column_types_slanted_ref`)
* Synapse metadata (`synapses_pni_2`)
* CAVEclient + CloudVolume
* PyTorch (Python)
* Google Colab for model training

---

## **Next Steps**

Planned extensions include:

* Multi-slice synapse volumes
* Incorporation of postsynaptic identity
* Morphological and segmentation-based feature integration
* Full 3D volumetric CNN models for synapse classification

---


