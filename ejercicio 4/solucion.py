import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder 

# Cargar datos
data = pd.read_excel("data_customer_classification.xlsx")

# Convertir la columna 'trans_date' a tipo datetime
data['trans_date'] = pd.to_datetime(data['trans_date'])

# Calcular la frecuencia de compra por cliente
data['frequency'] = data.groupby('customer_id')['customer_id'].transform('count')

# Calcular el total gastado por cliente
data['total_spent'] = data.groupby('customer_id')['tran_amount'].transform('sum')

# Calcular el máximo gastado por cliente
data['max_spent'] = data.groupby('customer_id')['tran_amount'].transform('max')

def genCateg(x):
    if x < 500:
        return 0
    elif x < 1000:
        return 1
    else:
        return 2

# Eliminar duplicados
data_unique = data.drop_duplicates(subset=['customer_id'])

# Generar etiquetas de clasificación basadas en el total gastado
data_unique['customer_category'] = [genCateg(i) for i in data_unique['total_spent']]

# Crear un nuevo DataFrame para características y etiquetas
features_labels = data_unique[['frequency', 'total_spent', 'max_spent', 'customer_category']]

# Codificar las etiquetas de clasificación
label_encoder = LabelEncoder()
features_labels['customer_category'] = label_encoder.fit_transform(features_labels['customer_category'])

# Definir las características y las etiquetas
X = features_labels[['frequency', 'total_spent', 'max_spent']].values
y = features_labels['customer_category'].values

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from tensorflow.keras.utils import to_categorical

# Convertir y_train y y_test en representaciones one-hot
y_train_one_hot = to_categorical(y_train)
y_test_one_hot = to_categorical(y_test)

# Suponiendo que tienes las predicciones en one-hot llamadas 'predictions_one_hot'
# y que cada fila representa una predicción para un dato

# Invertir la codificación one-hot
predictions = np.argmax(y_train_one_hot, axis=1)

# Contar la frecuencia de cada categoría
category_counts = np.bincount(predictions)

# Imprimir el resultado
for i, count in enumerate(category_counts):
    print(f"Categoría {i}: {count} datos")

# Construir el modelo
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(3,)),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
historial = model.fit(X_train, y_train, epochs=250, batch_size=32, validation_data=(X_test, y_test))

# Guardar el modelo
model.save("customer_classification_model.h5")
