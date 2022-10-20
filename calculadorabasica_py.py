#!/usr/bin/env python
# coding: utf-8

# In[ ]:


functionSum = lambda firstNumber,secondNumber: firstNumber + secondNumber
functionSubtraction = lambda firstNumber,secondNumber : firstNumber - secondNumber
functionMultiplication = lambda firstNumber,secondNumber: firstNumber * secondNumber
functionDivision = lambda firstNumber,secondNumber: firstNumber / secondNumber

def cal():
    print("BEM VINDO A CALCULADORA PYTHON\n\n***** Digite dois números ******\n\n")
    firstNumber = float(input("Numero 1: "))
    secondNumber = float(input("Numero 2: "))

    print("\nEscolha uma operação: \n** 1 - SOMA\n** 2 - SUBTRAÇÃO\n** 3 - MULTIPLICAÇÃO\n** 4 - DIVISÃO\n\n")
    optionSelect = int(input("Operação: "))

    if optionSelect == 1:
        print(functionSum(firstNumber,secondNumber))

    elif optionSelect == 2:
        print(functionSubtraction(firstNumber,secondNumber))

    elif optionSelect == 3:
        print(functionMultiplication(firstNumber,secondNumber))

    elif optionSelect == 4:
        print(div(firstNumber,secondNumber))

    else:
        print("***** OPERAÇÃO INVALIDA *****")

    print("\nRETORNAREMOS AO MENU....\n")
    main()

def main():
    print("Escolha uma opção:\n\n1 - ABRIR CALCULADORA\n\n0 - SAIR DO PROGRAMA")
    optionSelect = int(input("\n"))
    if optionSelect == 1:
        cal()
    elif optionSelect == 0:
        quit()
    else:
        print("OPÇÃO INVALIDA, RETORNATEMOS AO MENU...")
        main()
main()
