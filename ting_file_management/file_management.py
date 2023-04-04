import sys
import os


def txt_importer(path_file):
    f, extensao = os.path.splitext(path_file)
    if not path_file:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    if extensao != '.txt':
        print("Formato inválido", file=sys.stderr)

    with open(path_file, 'r', encoding="utf-8") as files:
        text = files.read().split('\n')
        print(text)
