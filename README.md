# Synapse E/I Classification from MICrONS EM Images

A reproducible deep-learning workflow for predicting whether a presynaptic neuron is excitatory or inhibitory from synapse-centered electron microscopy (EM) image patches.

## Project overview

This project asks whether local synaptic ultrastructure contains enough information to distinguish excitatory from inhibitory presynaptic neurons. It combines open MICrONS connectomics data, expert cell-type annotations, neuron-aware dataset construction, and a PyTorch image-classification pipeline.

The workflow:

- queries synapse metadata from the MICrONS `minnie65_public` dataset with CAVEclient;
- obtains neuron-level labels from the Allen Institute `allen_v1_column_types_slanted_ref` table;
- joins labels to synapses through `pre_root_id`;
- extracts synapse-centered 2D EM patches;
- uses neuron-held-out train, validation, and test splits to reduce identity leakage;
- trains and evaluates a ResNet-based 2D CNN in PyTorch; and
- reports accuracy, balanced accuracy, F1 scores, confusion matrices, and ROC/precision-recall analyses.

## Results

The current single-slice model achieves approximately:

- **Accuracy:** 0.83
- **Balanced accuracy:** 0.83
- **Neuron-level accuracy:** approximately 0.88
- **ROC AUC:** approximately 0.96

These results suggest that local ultrastructural features contain predictive information about presynaptic neuronal identity. See the notebook and files under `results/` for experiment details.

## Data sources

- MICrONS dataset: `minnie65_public`
- Synapse table: `synapses_pni_2`
- Cell-type table: `allen_v1_column_types_slanted_ref`

Raw EM imagery and extracted image patches are not included. Users should retrieve data through the official MICrONS/CAVE services and comply with their applicable terms.

## Repository structure

```text
Synapse_Classification_2D/
├── Synapse_Classification_2D.ipynb  # Training and evaluation workflow
├── data_extraction.py               # CAVE metadata queries and label merge
├── models/                          # Saved model artifacts
├── results/                         # Metrics and figures
├── requirements.txt                 # Python dependencies
├── environment.yml                  # Conda environment
└── README.md
```

## Installation

### pip

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Conda

```bash
conda env create -f environment.yml
conda activate synapse-ei
```

## Reproducing the analysis

1. Configure CAVE authentication for `minnie65_public`.
2. Run `data_extraction.py` or import its functions to retrieve and merge synapse and neuron-label tables.
3. Create the documented train/validation/test image directories with neurons held out across splits.
4. Open `Synapse_Classification_2D.ipynb`, update `DATASET_ROOT`, and run the training and evaluation cells.
5. Review generated metrics and visualizations in `results/`.

The notebook was developed in Google Colab and currently expects a user-supplied dataset path.

## Methods and safeguards

- Splitting is performed at the neuron level rather than the image level.
- Class balance is monitored across splits.
- Evaluation includes class-sensitive metrics in addition to accuracy.
- Random seeds are set in the notebook for core Python, NumPy, and PyTorch operations.

## Limitations

- The current model uses a single 2D section rather than a 3D EM volume.
- Performance may depend on patch extraction, image quality, and the sampled neurons.
- Results should not be interpreted as evidence that morphology alone fully determines cell identity.
- The repository does not distribute MICrONS image data.

## Next steps

- incorporate multi-slice or volumetric context;
- add postsynaptic identity and morphology-derived features;
- compare 2D and 3D model families;
- test calibration and uncertainty; and
- evaluate generalization across additional neurons, regions, and datasets.

## Author

**Bita Massoudi, Ph.D.**  
Neuroscience, computational imaging, and machine learning  
University of Washington M.S. ECE candidate

## Citation

If you build on this work, please cite the repository and relevant MICrONS and Allen Institute data resources.
