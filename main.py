import csv
import json
import os
from models.csv_to_json import *
from models.estudiante import *

def main():
    csv_filename = input("Ingrese el nombre completo del archivo CSV (incluyendo la ruta): ")

    # Comprobando si el archivo CSV existe
    if not os.path.isfile(csv_filename):
        print("¡El archivo CSV no existe!")
        return

    # Extrayendo el nombre del archivo sin la extensión
    nombre_archivo = os.path.splitext(os.path.basename(csv_filename))[0]
    # Creando el nombre del archivo JSON
    json_filename = os.path.join(os.path.dirname(csv_filename), nombre_archivo[:-4] + ".json")

    # Convertir CSV a JSON
    conversor = ConversorCSVtoJSON(csv_filename)
    estudiantes = conversor.leer_estudiantes()
    conversor.escribir_json(estudiantes, json_filename)

    print(f"El archivo JSON se ha creado exitosamente en {json_filename}.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
