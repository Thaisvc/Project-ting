import sys
import os


def txt_importer(path_file):
    f, extension = os.path.splitext(path_file)
    if extension != '.txt':
        return print("Formato inválido", file=sys.stderr)

    if (os.path.isfile(path_file)):
        with open(path_file, 'r', encoding="utf-8") as files:
            text = files.read().split("\n")
        return text
    else:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
