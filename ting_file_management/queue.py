from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._queue = list()

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        if self.__len__ == 0:
            return None
        return self._queue.pop(0)

    def search(self, index):
        if index in range(self.__len__()):
            return self._queue[index]
        else:
            raise IndexError("Índice Inválido ou Inexistente")


""" if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    q.enqueue(3)
    q.enqueue(5)
    print(q._queue)
    print(q.search(0))
 """
