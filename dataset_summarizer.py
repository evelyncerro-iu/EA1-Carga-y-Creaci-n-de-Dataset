import pandas as pd

class DatasetSummarizer:
    """
    Clase para resumir un DataFrame de pandas y exportar el resumen a un archivo .txt.
    """
    def __init__(self, df: pd.DataFrame):
        """
        Parámetros:
        - df (pd.DataFrame): El DataFrame que se desea resumir.
        """
        self.df = df

    def generate_summary_text(self) -> str:
        """
        Genera un texto completo con el resumen del DataFrame.
        """
        summary_lines = []
        summary_lines.append("=" * 50)
        summary_lines.append("       RESUMEN DEL DATASET")
        summary_lines.append("=" * 50)
        
        # 1. Dimensiones
        rows, cols = self.df.shape
        summary_lines.append(f"\n[Dimensiones]")
        summary_lines.append(f"- Cantidad de filas: {rows}")
        summary_lines.append(f"- Cantidad de columnas: {cols}")
        
        # 2. Tipos de datos y columnas
        summary_lines.append(f"\n[Columnas y Tipos de Datos]")
        for col, dtype in self.df.dtypes.items():
            summary_lines.append(f"  • {col}: {dtype}")
            
        # 3. Valores nulos
        summary_lines.append(f"\n[Valores Nulos por Columna]")
        null_counts = self.df.isnull().sum()
        for col, nulls in null_counts.items():
            summary_lines.append(f"  • {col}: {nulls} nulos")
            
        # 4. Estadísticas descriptivas básicas
        summary_lines.append(f"\n[Estadísticas Descriptivas]")
        desc = self.df.describe(include='all').to_string()
        summary_lines.append(desc)
        summary_lines.append("\n" + "=" * 50)
        
        return "\n".join(summary_lines)

    def save_summary_to_txt(self, filename: str = "dataset_summary.txt"):
        """
        Guarda el texto resumen en un archivo .txt físico.
        """
        try:
            summary_text = self.generate_summary_text()
            with open(filename, "w", encoding="utf-8") as f:
                f.write(summary_text)
            print(f"¡Éxito! El archivo '{filename}' ha sido generado correctamente.")
        except Exception as e:
            print(f"Error al guardar el archivo de resumen: {e}")
            raise e
