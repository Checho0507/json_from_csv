import csv
import json
import os
from models.estudiante import *

class ConversorCSVtoJSON:
    def __init__(self, csv_filename):
        self.csv_filename = csv_filename

    def leer_estudiantes(self):
        estudiantes = []
        with open(self.csv_filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                estudiante = Estudiante(row[0].strip(), row[1].strip(), row[2].strip())
                estudiantes.append(estudiante)
        return estudiantes

    def escribir_json(self, estudiantes, json_filename):
        estudiantes_json = [estudiante.to_dict() for estudiante in estudiantes]
        with open(json_filename, 'w', encoding='utf-8') as file:
            json.dump(estudiantes_json, file, ensure_ascii=False, indent=4)