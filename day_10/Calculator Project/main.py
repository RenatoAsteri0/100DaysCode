def add(n1, n2):
    return n1 + n2

def division(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

def subtraction(n1, n2):
    return n1 - n2

operators = {
    "-":subtraction,
    "+":add,
    "*":multiply,
    "/":division
}

jogue = True
continuar = 'y'
while jogue:
    primeiro_numero = float(input("coloque o primeiro numero: "))
    while continuar == 'y':
        operator = str(input("'+', '-', '*', '/'"))
        segundo_numero = float(input("coloque o segundo numero: "))
        resultado = operators[operator](primeiro_numero, segundo_numero)
        print(f'{primeiro_numero} {operator} {segundo_numero} = {resultado}')
        continuar = str(input(f"escreva y para continuar o calculo com {resultado}, ou digite 'n' para restart a calculadora"))
        if continuar == 'n':
            jogue = False
        

