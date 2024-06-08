# Test de Cálculo de Saltos Mínimos

Este proyecto contiene un conjunto de pruebas unitarias para verificar la funcionalidad de una función `calcular_saltos` que calcula el número mínimo de saltos necesarios para alcanzar un objetivo dado.

## Estructura del Proyecto

- `solucion.py`: Archivo que contiene la implementación de la función `calcular_saltos`.
- `test.py`: Archivo que contiene las pruebas unitarias para la función `calcular_saltos`.

## Requisitos

- Python 3.10
- `unittest`: Este módulo está incluido en la biblioteca estándar de Python, por lo que no se necesita instalación adicional.

## Instalación

1. Clona el repositorio o descarga los archivos necesarios en tu máquina local.
2. Asegúrate de tener Python 3.10 instalado.

## Uso

1. Implementa la función `calcular_saltos` en el archivo `solucion.py`. La función debe recibir un entero `n` y devolver el número mínimo de saltos necesarios para alcanzar el objetivo.


2. Ejecuta las pruebas unitarias para verificar la funcionalidad de la implementación.

   python test.py

## Pruebas Incluidas

El archivo `test.py` contiene las siguientes pruebas:

1. `test_case_1`: Verifica que se calcula correctamente el número de saltos mínimos para `n = 1`.
2. `test_case_2`: Verifica que se calcula correctamente el número de saltos mínimos para `n = 2`.
3. `test_case_3`: Verifica que se calcula correctamente el número de saltos mínimos para `n = 3`.
4. `test_case_4`: Verifica que se calcula correctamente el número de saltos mínimos para `n = 4`.
5. `test_case_5`: Verifica que se calcula correctamente el número de saltos mínimos para `n = 5`.

## Ejecución de Pruebas

Para ejecutar las pruebas, simplemente ejecuta el siguiente comando en tu terminal:

python test.py
