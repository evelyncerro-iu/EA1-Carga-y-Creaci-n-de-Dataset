import pandas as pd
from datasets import load_dataset

class HFDatasetLoader:
    """
    Clase para conectar y cargar datasets desde Hugging Face Datasets 
    y convertirlos a un DataFrame de pandas.
    """
    def __init__(self, dataset_name: str, split: str = "train"):
        """
        Parámetros:
        - dataset_name: Identificador del dataset en Hugging Face.
        - split: División del dataset a cargar. Por defecto es 'train'.
        """
        self.dataset_name = dataset_name
        self.split = split

    def load_data(self) -> pd.DataFrame:
        """
        Realiza la conexión, descarga el dataset y lo retorna como un DataFrame de pandas.
        """
        try:
            # Cargar el dataset desde Hugging Face
            if self.split:
                dataset = load_dataset(self.dataset_name, split=self.split)
            else:
                dataset = load_dataset(self.dataset_name)
                # Si no se especifica split y devuelve un DatasetDict, tomamos el primer split disponible
                if hasattr(dataset, "keys"):
                    first_split = list(dataset.keys())[0]
                    dataset = dataset[first_split]
            
            # Convertir el dataset a un DataFrame de pandas
            df = dataset.to_pandas()
            return df
            
        except Exception as e:
            print(f"Error al cargar el dataset '{self.dataset_name}': {e}")
            raise e
