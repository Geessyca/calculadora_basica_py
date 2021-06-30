<h1 align="center">
  🎓<br>Calculadora básica em Python
</h1>

<h4 align="center">
  O intuito deste repositório é compartilhar a construção uma calculadora construida em Python.
</h4>

<h2 align="left">
  Passo a passo ↷ 
</h2>

<h3>Lambda<h3>

<h4>As funções anônimas — em Python também chamadas de expressões lambda — representam um recurso bem interessante da linguagem Python, mas cuja utilidade pode não ser muito óbvia à primeira vista.

Uma função anônima é útil principalmente nos casos em que precisamos de uma função para ser passada como parâmetro para outra função, e que não será mais necessária após isso, como se fosse “descartável”.<h4>
    
<h8>https://pythonhelp.wordpress.com/tag/lambda/<h8>

<h3>No código:<h3>

<h4>No nosso código ultilizaremos 4 funções lambda, com os respectivos nomes, <i> soma, sub, mult, div </i>, onde cada uma faz uma das operações basicas.<h4>

```
soma = lambda a,b: a + b
sub = lambda a,b : a - b
mult = lambda a,b: a * b
div = lambda a,b: a / b 
```

<h4>
Após realizarmos a declaração das funções, deveremos execultar o código em si. 

Ultizamos o <i><b>input</b></i> para o usuario escolher tanto os algarismos que ele quer realizar a operação, quando o tipo de operação que ele deseja:
<h4>

```
print("BEM VINDO A CALCULADORA PYTHON\n\n***** Digite dois números ******\n\n")
a = int(float("Numero 1: "))
b = int(float("Numero 2: "))

print("\nEscolha uma operação: \n** 1 - SOMA\n** 2 - SUBTRAÇÃO\n** 3 - MULTIPLICAÇÃO\n** 4 - DIVISÃO\n\n")
op = int(input("Operação: "))
```
<h4>Agora para melhor estrura do programa, ultilizaremos uma função para criarmos a calculadora:<h4>
    
```
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
```
<h4>Agora faremos nosso menu, usando também uma função:<h4>

```
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
```
<h4>Após isso é somente chamar a função menu(), para o programa rodar<h4>
    
```
menu()
```


##  👩🏻‍💻 Autora<br>
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/geessyca">
        <img src="https://avatars.githubusercontent.com/u/72661229?v=4" width="100px;" alt="Icon GitHub"/><br>
        <sub>
          <b>Gessyca Moreira</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
