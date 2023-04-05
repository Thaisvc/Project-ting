import sys
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
    if len(instance) == 0:
        print("Não há elementos")
    else:
        remove_file = instance.dequeue()
        print(f"Arquivo {remove_file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        index_list = instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
        return
    print(index_list)


""" if __name__ == "__main__":
    q = Queue()
    process("statics/arquivo_teste.txt", q) """
