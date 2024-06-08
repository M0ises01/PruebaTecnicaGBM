# Customer Classification Model

Este proyecto consiste en un modelo de clasificación de clientes basado en datos de transacciones. Utiliza un modelo de red neuronal creado con TensorFlow/Keras para predecir la categoría de un cliente según su frecuencia de compra, el total gastado y el máximo gastado.

## Archivos del Proyecto

- `data_customer_classification.xlsx`: Archivo de datos en formato Excel con información de transacciones de clientes.
- `solucion.py`: Archivo que contiene la función para cargar el modelo y realizar predicciones.
- `test.py`: Archivo que contiene las pruebas unitarias para verificar el funcionamiento del modelo.
- `modelo.ipynb`: Jupyter Notebook que contiene el código para leer los datos, crear y entrenar el modelo, separado por secciones.
- `customer_classification_model.h5`: Archivo del modelo guardado después del entrenamiento.

## Requisitos

- Python 3.7+
- TensorFlow 2.0+
- scikit-learn
- pandas
- numpy
- openpyxl (para leer archivos Excel en pandas)

Puedes instalar las dependencias necesarias ejecutando:

pip install tensorflow scikit-learn pandas numpy openpyxl

## Uso

### Entrenar el Modelo

1. Abre y ejecuta el archivo `modelo.ipynb` para leer los datos, crear y entrenar el modelo.
2. Guarda el modelo entrenado como `customer_classification_model.h5`.

### Realizar Predicciones

1. Usa la función `predecir_categoria` definida en `solucion.py` para hacer predicciones con el modelo entrenado.

### Pruebas Unitarias

Ejecuta las pruebas unitarias definidas en `test.py` para verificar el correcto funcionamiento del modelo:

python -m unittest test.py
