import csv
import os
from models import UsuarioCadastrado


def gerando_csv(data):
    csv_file = "cadastros.csv"
    file_exists = os.path.exists(csv_file)

    if file_exists == False:
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=UsuarioCadastrado.__fields__.keys())
            writer.writeheader()
    else:
        if isinstance(data, UsuarioCadastrado):
            with open(csv_file, mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=UsuarioCadastrado.__fields__.keys())
                writer.writerow(data.dict())

        if isinstance(data, list) and len(data) > 0:
            with open(csv_file, mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=UsuarioCadastrado.__fields__.keys())
                writer.writerows([usuario.dict() for usuario in data])

