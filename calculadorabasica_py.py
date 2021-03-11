#!/usr/bin/env python
# coding: utf-8

# In[ ]:


soma = lambda a,b: a + b
sub = lambda a,b : a - b
mult = lambda a,b: a * b
div = lambda a,b: a / b

def cal():
    print("BEM VINDO A CALCULADORA PYTHON\n\n***** Digite dois números ******\n\n")
    a = float(input("Numero 1: "))
    b = float(input("Numero 2: "))

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

    print("\nRETORNAREMOS AO MENU....\n")
    menu()

def menu():
    print("Escolha uma opção:\n\n1 - ABRIR CALCULADORA\n\n0 - SAIR DO PROGRAMA")
    op = int(input("\n"))
    if op == 1:
        cal()
    elif op == 0:
        quit()
    else:
        print("OPÇÃO INVALIDA, RETORNATEMOS AO MENU...")
        menu()
menu()
        

