class Calculadora:

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.operador = ""

    def somar(self):
        self.result = self.num1 + self.num2

    def subtrair(self):
        self.result = self.num1 - self.num2

    def multiplicar(self):
        self.result = self.num1 * self.num2

    def dividir(self):
        self.result = self.num1 / self.num2

    def get_result(self):
        return self.result
    
def main():
    calculadora = Calculadora()
    calculadora.num1 = int(input("Digite o primeiro numero: "))
    calculadora.num2 = int(input("DIgite o segundo numero: "))
    calculadora.operador = input("Digite o operador: ")

    if calculadora.operador == "+":
        calculadora.somar()
    elif calculadora.operador == "-":
        calculadora.subtrair()
    elif calculadora.operador == "*":
        calculadora.multiplicar()
    elif calculadora.operador == "/":
        calculadora.dividir()

    print("O resultado é: ", calculadora.get_result())


if __name__ == "__main__":
    main()
    