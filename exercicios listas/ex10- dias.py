lista = [1, 2, 3, 4]
def ordenar(lista, ordem=1):
    troquei = True

    while troquei:
        troquei = False
        x = 0
        while x < len(lista) - 1:
            if lista[x] * ordem > lista[x + 1] * ordem:
                temp = lista[x]
                lista[x] = lista[x + 1]
                lista[x + 1] = temp
                troquei = True
            x += 1
    return lista


if __name__ == "__main__":
    vendas = [100, 50, 250, 27, 150, 600]
    print(ordenar(vendas))
    print(ordenar(vendas, -1))
