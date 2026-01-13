"""Query synapse metadata and presynaptic neuron identities
from the MICrONS minnie65_public dataset using CAVEclient."""

from caveclient import CAVEclient
import pandas as pd


def load_synapse_table():
    """Load synapse metadata from the `synapses_pni_2` table."""
    client = CAVEclient("minnie65_public")
    syn_df = client.materialize.query_table("synapses_pni_2")
    return pd.DataFrame(syn_df)


def load_neuron_labels():
    """Load neuron-level E/I annotations from
    the Allen Institute's `allen_v1_column_types_slanted_ref` table."""
    client = CAVEclient("minnie65_public")
    label_df = client.materialize.query_table("allen_v1_column_types_slanted_ref")
    return pd.DataFrame(label_df)


def merge_synapses_with_labels():
    """Merge synapse metadata with presynaptic neuron labels.
    Returns a dataframe with inherited E/I identity for each synapse."""
    syn_df = load_synapse_table()
    label_df = load_neuron_labels()

    merged = syn_df.merge(
        label_df[["root_id", "cell_type", "classification_system"]],
        left_on="pre_root_id",
        right_on="root_id",
        how="inner"
    )

    return merged
