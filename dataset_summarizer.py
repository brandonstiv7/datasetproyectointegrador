"""
Clase para generar un resumen de un DataFrame en un archivo .txt.
Requisitos: pip install pandas
"""
from pathlib import Path
import pandas as pd


class DatasetSummarizer:
    """Resume estructura, tipos, valores nulos y estadísticas de un DataFrame."""

    def __init__(self, dataframe: pd.DataFrame):
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("dataframe debe ser un objeto pandas.DataFrame.")
        self.dataframe = dataframe

    def save_summary(self, output_path: str = "resumen_dataset.txt") -> str:
        """Genera el resumen y devuelve la ruta del archivo creado."""
        df = self.dataframe
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        lines = [
            "RESUMEN DEL DATASET",
            "=" * 60,
            f"Cantidad de filas: {df.shape[0]}",
            f"Cantidad de columnas: {df.shape[1]}",
            "",
            "NOMBRES Y TIPOS DE COLUMNAS",
            "-" * 60,
        ]
        if df.shape[1] == 0:
            lines.append("El DataFrame no contiene columnas.")
        else:
            for column in df.columns:
                lines.append(f"- {column}: {df[column].dtype}")

        lines.extend(["", "VALORES NULOS POR COLUMNA", "-" * 60])
        if df.shape[1] == 0:
            lines.append("No hay columnas para evaluar.")
        else:
            null_counts = df.isna().sum()
            for column, count in null_counts.items():
                lines.append(f"- {column}: {int(count)} ({count / max(len(df), 1) * 100:.2f}%)")

        lines.extend(["", "ESTADÍSTICAS DESCRIPTIVAS", "-" * 60])
        numeric = df.select_dtypes(include="number")
        if numeric.empty:
            lines.append("No hay columnas numéricas.")
        else:
            lines.append(numeric.describe().round(3).to_string())

        lines.extend(["", "MUESTRA DE LOS PRIMEROS 5 REGISTROS", "-" * 60])
        lines.append(df.head().to_string(index=False) if not df.empty else "DataFrame vacío.")
        lines.append("")
        path.write_text("\n".join(lines), encoding="utf-8")
        return str(path)
