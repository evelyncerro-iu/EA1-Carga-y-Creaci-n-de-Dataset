# Proyecto: Procesamiento, Transformación y Resumen de Datasets con Hugging Face

Este proyecto implementa una arquitectura modular en Python orientada a objetos para conectar, extraer, transformar, resumir y exportar información de datasets públicos utilizando **Hugging Face Datasets** y **Pandas**, coordinado mediante un Jupyter Notebook en Google Colab.

---

## 📂 Estructura del Proyecto

El proyecto está compuesto por los siguientes archivos principales:

1. **`hf_loader.py`**: Contiene la clase `HFDatasetLoader`, encargada de realizar la conexión y descarga de cualquier dataset desde Hugging Face y convertirlo a un DataFrame de pandas.
2. **`dataset_summarizer.py`**: Contiene la clase `DatasetSummarizer`, encargada de procesar un DataFrame, extraer sus métricas y estructura (dimensiones, tipos de datos, nulos y estadísticas descriptivas) y exportar el resumen en un archivo `.txt`.
3. **`Jupyter Notebook (.ipynb)`**: Archivo de coordinación que ejecuta el flujo completo, aplicando 4 transformaciones distintas sobre el DataFrame e integrando ambos componentes.
4. **Archivo de Resumen (`.txt`)**: Salida generada automáticamente con el resumen del DataFrame transformado.

---

## 🛠️ Descripción de los Componentes

### 1. Clase `HFDatasetLoader` (`hf_loader.py`)
* **Propósito:** Conexión y carga modular de datos.
* **Características:**
  * Recibe como parámetros el identificador del dataset (ej. `'scikit-learn/iris'`) y el `split` opcional (por defecto `'train'`).
  * Utiliza la librería `datasets` de Hugging Face.
  * Retorna directamente un `pd.DataFrame` listo para su manipulación.

### 2. Clase `DatasetSummarizer` (`dataset_summarizer.py`)
* **Propósito:** Análisis estructural y exportación a texto.
* **Características:**
  * Recibe un `pd.DataFrame` como entrada.
  * Genera un reporte detallado que incluye:
    * Dimensiones (filas y columnas).
    * Nombres y tipos de datos de cada columna.
    * Conteo de valores nulos.
    * Estadísticas descriptivas generales.
  * Cuenta con un método para guardar el reporte de forma limpia en un archivo físico `.txt`.

---

## 🔄 Flujo de Trabajo en el Jupyter Notebook

El cuaderno coordina el proceso en el siguiente orden:
1. **Importación:** Se importan las clases desde sus respectivos archivos `.py`.
2. **Carga:** Se instancia `HFDatasetLoader` para obtener el dataset original de Iris.
3. **Transformaciones (4 distintas aplicadas):**
   * **Transformación 1:** Renombrado dinámico de columnas del dataset a nombres estándar en español.
   * **Transformación 2:** Filtrado de filas mediante una condición numérica (`longitud_petalo > 1.5`).
   * **Transformación 3:** Creación de una columna calculada (`area_petalo` como producto de longitud por ancho).
   * **Transformación 4:** Creación de una columna categórica condicional (`categoria_tamano` clasificada en 'Grande' o 'Moderada').
4. **Resumen y Exportación:** Se instancia `DatasetSummarizer` con el DataFrame ya transformado y se genera el archivo `.txt` con los resultados finales.

---

## 🚀 Instrucciones de Ejecución

1. Sube los archivos `hf_loader.py`, `dataset_summarizer.py` y el Jupyter Notebook a tu entorno de trabajo (por ejemplo, Google Colab).
2. Asegúrate de tener instaladas las librerías necesarias:
   ```bash
   pip install datasets pandas numpy
