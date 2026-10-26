# Actividad 1: obtener y preparar datos desde Hugging Face

## Archivos
- `hf_dataset_loader.py`: clase `HFDatasetLoader`, carga un split de Hugging Face y lo devuelve como DataFrame de pandas.
- `dataset_summarizer.py`: clase `DatasetSummarizer`, genera un resumen del DataFrame en un archivo `.txt`.
- `actividad_1_huggingface.ipynb`: coordina las clases y realiza una transformación mínima.
- `resumen_dataset.txt`: ejemplo de resumen para el dataset Iris después de renombrar una columna. Se actualiza al ejecutar el notebook.

## Requisitos
Python 3.10 o superior recomendado.

Instala las dependencias en una terminal:
```bash
python -m pip install pandas datasets jupyter
```

## Ejecutar
1. Abre la carpeta en Jupyter Notebook o VS Code.
2. Abre `actividad_1_huggingface.ipynb`.
3. Ejecuta las celdas en orden. Se requiere conexión a Internet para descargar el dataset desde Hugging Face.
4. Verifica que se genere/actualice `resumen_dataset.txt`.

Dataset usado: `scikit-learn/iris`, split `train`.

## Transformación aplicada
Se renombra la columna `sepal_length` como `sepal_length_cm` (si el dataset presenta el nombre `sepal_length`). Esto cambia el nombre de una columna y permite observar una transformación real del DataFrame antes de generar el resumen.

## Publicar en GitHub
1. Crea un repositorio nuevo en GitHub.
2. Copia estos archivos a la carpeta del repositorio.
3. En una terminal dentro de esa carpeta:
```bash
git init
git add hf_dataset_loader.py dataset_summarizer.py actividad_1_huggingface.ipynb resumen_dataset.txt README.md
git commit -m "Agrega carga, transformación y resumen de dataset"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/TU-REPOSITORIO.git
git push -u origin main
