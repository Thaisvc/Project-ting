from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    file = PriorityQueue()
    quantity_lines = [
        {"qtd_linhas": 2},
        {"qtd_linhas": 5},
        {"qtd_linhas": 4},
        {"qtd_linhas": 6},
        {"qtd_linhas": 3}
    ]
    priority_files = [
        {"qtd_linhas": 2},
        {"qtd_linhas": 3},
        {"qtd_linhas": 4},
        {"qtd_linhas": 5},
        {"qtd_linhas": 6}
    ]

    for row in quantity_lines:
        row.enqueue(row)

    for i in range(row.__len__()):
        assert row.search(i) == priority_files[i]

    for row in priority_files:
        assert row.dequeue() == row

    with pytest.raises(
            IndexError,
            match="Índice Inválido ou Inexistente"):
        file.search(0)
