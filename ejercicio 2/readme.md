# Test de Procesamiento de Campeonatos

Este proyecto contiene un conjunto de pruebas unitarias para verificar la funcionalidad de una función `procesar_campeonatos` que procesa datos de campeonatos y produce resultados específicos.

## Estructura del Proyecto

- `solucion.py`: Archivo que contiene la implementación de la función `procesar_campeonatos`.
- `test.py`: Archivo que contiene las pruebas unitarias para la función `procesar_campeonatos`.

## Requisitos

- Python 3.10
- `unittest`: Este módulo está incluido en la biblioteca estándar de Python, por lo que no se necesita instalación adicional.

## Instalación

1. Clona el repositorio o descarga los archivos necesarios en tu máquina local.
2. Asegúrate de tener Python 3.10 instalado.

## Uso

1. Implementa la función `procesar_campeonatos` en el archivo `solucion.py`. La función debe recibir una cadena de texto con los datos de entrada y devolver una cadena de texto con los resultados procesados.

2. Ejecuta las pruebas unitarias para verificar la funcionalidad de la implementación.

   python test_procesar_campeonatos.py

## Pruebas Incluidas

El archivo `test_procesar_campeonatos.py` contiene las siguientes pruebas:

1. `test_case_0`: Verifica la función con un conjunto de datos complejos que incluye múltiples campeonatos y escenarios.
2. `test_case_1`: Verifica la función con un conjunto reducido de datos de campeonatos.
3. `test_case_2`: Verifica la función con un conjunto de datos de campeonatos más grande y diverso.
4. `test_case_3`: Verifica la función con un conjunto de datos de campeonatos con menos entradas pero múltiples resultados.

## Ejecución de Pruebas

Para ejecutar las pruebas, simplemente ejecuta el siguiente comando en tu terminal:

python test_procesar_campeonatos.py
