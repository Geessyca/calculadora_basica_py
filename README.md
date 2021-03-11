# CALCULADORA BÁSICA
<h4> Usando função lambda <h4>

<h2><b>Lambda<b><h2>

<h4>As funções anônimas — em Python também chamadas de expressões lambda — representam um recurso bem interessante da linguagem Python, mas cuja utilidade pode não ser muito óbvia à primeira vista.

Uma função anônima é útil principalmente nos casos em que precisamos de uma função para ser passada como parâmetro para outra função, e que não será mais necessária após isso, como se fosse “descartável”.<h4>
    
<h8>https://pythonhelp.wordpress.com/tag/lambda/<h8>

<h2><b> No código: <b><h2>

<h4>No nosso código ultilizaremos 4 funções lambda, com os respectivos nomes, <i> soma, sub, mult, div <i>, onde cada uma faz uma das operações basicas.<h4>

'''
soma = lambda a,b: a + b
sub = lambda a,b : a - b
mult = lambda a,b: a * b
div = lambda a,b: a / b
'''

'''
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
