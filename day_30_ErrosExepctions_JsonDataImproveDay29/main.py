try:
    # File Not Found error
    file = open('teste.txt')
    print(file.read())

    #
    numeros = [1,2,3,4]
    print(numeros + 'ola')
except FileNotFoundError:
    print('arq nao existe, criado um novo')
    file = open('teste.txt', 'w')
    file.write('Dentro do file')


except TypeError as erro:
    print(f'impossivel juntar str e int erro: {erro}')