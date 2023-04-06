
def exists_word(word, instance):
    info = []  # guarda o resultado
    for file in instance._queue:  # instancia arquivo/fila pega o nome e linhas
        name_file = file["nome_do_arquivo"]
        row_file = file["linhas_do_arquivo"]
        occurrences = []
        # enumerate me da o index e o valor
        for index, row in enumerate(row_file):
            if word.lower() in row.lower():  # verifica se a palavra esta
                # contida na linha lida lower retorna string em minusculo
                # mostra a linha onde a palavra apaece  index começa em 0
                occurrences.append({"linha": index + 1})
        if occurrences:  # crio a saida dos dados
            info.append({
                "palavra": word,
                "arquivo": name_file,
                "ocorrencias": occurrences
            })
    return info


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


""" if __name__ == "__main__":
    q = Queue()
    process("statics/arquivo_teste.txt", q) """
