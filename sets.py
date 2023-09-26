def main():
    # Cria um conjunto com os nomes das estruturas de dados básicas
    set1 = {"lista", "tupla", "dicionário", "conjunto"}

    # Adiciona um elemento ao conjunto
    set1.add("grafo")

    # Remove um elemento do conjunto
    set1.remove("tupla")

    # Verifica se um elemento existe no conjunto
    print("'conjunto' existe no conjunto:", "conjunto" in set1)

    # Combina dois conjuntos
    set2 = {"arvore", "hashmap"}
    set3 = set1 | set2
    print(set3)

    # Encontra a interseção de dois conjuntos
    set4 = set1 & set2
    print(set4)

    # Encontra a diferença de dois conjuntos
    set5 = set1 - set2
    print(set5)

    # Encontra a diferença simétrica de dois conjuntos
    set6 = set1 ^ set2
    print(set6)


if __name__ == "__main__":
    main()
