###############################################
##Programa para treinar para a prova do osmar##
###############################################

###########################################
##Funcao que cria e insere itens na lista##
###########################################

def CriaLista():
    lista = []
    tamanho = int(input("Qual o tamanho da lista? "))
    for i in range (tamanho):
        numero = int(input(f"Digite o {i + 1} numero a ser adicionado!"))
        lista.append(numero)
    return lista

#######################################
##Funcao que reverte a ordem da lista##
#######################################

def inverteLista(lista):
    lista_invertida = lista[::-1]
    return lista_invertida

#######################################################
##Funcao que retorna o produto dos elementos da lista##
#######################################################

def multiplicaElementos(lista):
    resultado = 1
    for numero in lista:
        resultado = resultado * numero
    return (f"O resultado da multiplicacao dos elementos da lista e {resultado}")

##############################
##Funcao que imprime a lista##
##############################

def imprimeLista(lista):
    x = print(lista)
    return x

#######################################################################
##Funcao que cria um dicionario com N alunos e suas respectivas notas##
#######################################################################

def criaDic():
    dicionario = {}
    tamanho = int(input("Quantos alunos queremos adicionar? "))

    for i in range (tamanho):
        x = gramaticaBonita(i)
        nome = input(f"Digite o NOME do {x} aluno: ")
        nota = float(input(f"Digite a NOTA do {x} aluno: "))
        dicionario[nome] = nota
    return dicionario

##Funcao suporte
def gramaticaBonita(i):
    if i == 0:
        return "Primeiro"
    elif i == 1:
        return "Segundo"
    elif i == 2:
        return "Terceiro"
    elif i == 3:
        return "Quarto"
    elif i == 4:
        return "Quinto"
    elif i == 5:
        return "Sexto"
    elif i == 6:
        return "Sétimo"
    elif i == 7:
        return "Oitavo"
    elif i == 8:
        return "Nono"
    elif i == 9:
        return "Décimo"
    elif i == 10:
        return "Décimo Primeiro"
    else:
        return i
    

###################################
##Funcao que imprime o dicionario##
###################################

def imprimeDic(dicionario):
    for nome, nota in dicionario.items():
        print(f"Aluno: {nome}, Nota: {nota}")

#####################################
##Funcao que altera a nota do aluno##
#####################################

def alteraNota(dicionario):
    nome = input("Qual aluno deseja alterar a nota?")
    if nome in dicionario:
        dicionario[nome] = float(input("Deseja alterar a nota para quanto? "))
    return dicionario

#######################################################
##Funcao que retorna elementos repetidos de uma lista##
########################################################

def retornaRepetido(x,y):
    repetidos = []
    for numero in x:
        if numero in y:
            repetidos.append(numero)
    return repetidos

lista1 = [1,4.3,6,8]
lista2 = [2,4.3,7,8]

x = retornaRepetido(lista1,lista2)
print(x)


#x = criaDic()
#imprimeDic(x)
#alteraNota(x)
#imprimeDic(x)

#Criar uma lista de inteiros e inserir  elementos
#inverter a lista de inteiros
#retornar o produto dos elementos da lista criada
#imprimir a lista
#criar um dicionario de n alunos com as respectivas notas
#imprimir os alunos com suas notas
#alterar a nota de um aluno do dicionario
#retornar uma lista dos elementos repetidos de duas listas- obter as duas listas
#tecle 0 ou sair para fechar o programa
#escolha uma opcao

