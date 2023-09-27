def criar_tupla(*elementos):
    return tuple(elementos)

#atributos e métodos

def len_tupla(tupla):
    return len(tupla)


def get_item_tupla(tupla, indice):
    return tupla[indice]


def set_item_tupla(tupla, indice, valor):
    raise TypeError("Tuplas são imutáveis")


def eq_tupla(tupla1, tupla2):
    return tupla1 == tupla2


def ne_tupla(tupla1, tupla2):
    return tupla1 != tupla2


def add_tupla(tupla1, tupla2):
    return tuple(tupla1 + tupla2)


def mul_tupla(tupla, n):
    return tuple(tupla * n)


def main():
    # Criação de tuplas
    tupla_1 = criar_tupla(1, 2, 3)
    tupla_2 = criar_tupla(4, 5, 6)

    # Operações básicas
    print(len_tupla(tupla_1))  # 3
    print(get_item_tupla(tupla_1, 0))  # 1
    print(eq_tupla(tupla_1, tupla_2))  # False
    print(add_tupla(tupla_1, tupla_2))  # (1, 2, 3, 4, 5, 6)
    print(mul_tupla(tupla_1, 2))  # (1, 2, 3, 1, 2, 3)


if __name__ == "__main__":
    main()
