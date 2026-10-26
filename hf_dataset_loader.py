"""
Clase para cargar un dataset de Hugging Face y devolverlo como DataFrame de pandas.
Requisitos: pip install datasets pandas
"""
from datasets import load_dataset
import pandas as pd


class HFDatasetLoader:
    """Carga un split de Hugging Face Datasets y lo convierte a pandas.DataFrame."""

    def __init__(self, dataset_id: str, split: str = "train"):
        if not dataset_id or not isinstance(dataset_id, str):
            raise ValueError("dataset_id debe ser un identificador válido de Hugging Face.")
        self.dataset_id = dataset_id
        self.split = split

    def load(self) -> pd.DataFrame:
        """Descarga/carga el dataset indicado y devuelve sus datos como DataFrame."""
        dataset = load_dataset(self.dataset_id, split=self.split)
        return dataset.to_pandas()
