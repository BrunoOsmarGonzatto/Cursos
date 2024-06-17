import pytest

def encontra_impares(lista):
    if len(lista) < 1:
        return []
    else:
        lista2 = []
        if lista[0] % 2 == 1:
            lista2.extend([lista[0]])
            return encontra_impares(lista[1:])
            #return [lista[0]] + encontra_impares(lista[1:])
        else:
            return encontra_impares(lista[1:])
    return lista2

@pytest.mark.parametrize ("lista, esperado", [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 3, 5, 7, 9])
    ])

def test_encontra_impares(lista, esperado):
    assert encontra_impares(lista) == esperado

a = [1, 2, 3, 4, 5, 6, 7, 8]

print(encontra_impares(a))

lista3 = []
lista4 = [2]
lista3.extend([lista4[0]])
print(lista3)