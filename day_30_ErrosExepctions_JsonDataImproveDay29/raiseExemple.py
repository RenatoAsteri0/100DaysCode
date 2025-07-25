"""

Crie uma função chamada validar_idade() que:
Recebe uma idade como parâmetro.

Se a idade for negativa, use raise para lançar um ValueError com a mensagem: "Idade inválida: não pode ser negativa."

Se for maior que 130, lança um ValueError com a mensagem: "Idade inválida: fora do intervalo realista."

Se estiver no intervalo válido (0 a 130), retorne a idade com uma mensagem de sucesso.

Depois disso, use um try/except para testar a função com 3 casos:

Um valor negativo

Um valor absurdo (como 999)

Um valor válido (como 25)"""


def validar_idade(valor):
    if valor > 130:
        raise ValueError("fora do intervalo realista")

idade = int(input('digite sua idade: '))

try:
    validar_idade(idade)
    print("Idade valida")
except ValueError as erro:
    print(f"Idade inválida: {erro}")