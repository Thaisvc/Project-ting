from ting_file_management.file_management import txt_importer


def process(path_file, instance):

    lines = txt_importer(path_file)

    file_dic = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    for item in instance._queue:  # lista =  print(q._queue) mostra a lista
        if item["nome_do_arquivo"] == path_file:
            return

    instance.enqueue(file_dic)

    print(f"Arquivo {path_file} processado: {file_dic}")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


""" if __name__ == "__main__":
    q = Queue()
    process("statics/arquivo_teste.txt", q) """
