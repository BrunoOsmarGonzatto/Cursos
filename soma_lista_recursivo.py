import pytest

def soma_lista(lista):
    if len(lista) < 1:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])

@pytest.mark.parametrize ("lista, esperado", [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 55),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 45),
    ([1, 2, 3, 4, 5, 6, 7, 8], 36),
    ([1, 2, 3, 4, 5, 6, 7], 28),
    ([1, 2, 3, 4, 5, 6], 21),
    ([1, 2, 3, 4, 5], 15),
    ([1, 2, 3, 4], 10),
    ([1, 2, 3], 6),
])

def test_soma_lista(lista, esperado):
    assert soma_lista(lista) == esperado