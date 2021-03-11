# CALCULADORA BÁSICA
h1 Usando função lambda h1

'''
soma = lambda a,b: a + b
sub = lambda a,b : a - b
mult = lambda a,b: a * b
div = lambda a,b: a / b

print("BEM VINDO A CALCULADORA PYTHON\n\n***** Digite dois números ******\n\n")
a = int(input("Numero 1: "))
b = int(input("Numero 2: "))

print("\nEscolha uma operação: \n** 1 - SOMA\n** 2 - SUBTRAÇÃO\n** 3 - MULTIPLICAÇÃO\n** 4 - DIVISÃO\n\n")
op = int(input("Operação: "))

if op == 1:
    print(soma(a,b))

elif op == 2:
    print(sub(a,b))

elif op == 3:
    print(mult(a,b))

elif op == 4:
    print(div(a,b))

else:
    print("***** OPERAÇÃO INVALIDA *****")
'''
