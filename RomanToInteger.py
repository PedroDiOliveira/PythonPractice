TabelaRomanos = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
    }

#######################
##Pergunta ao usuario##
#######################

def pergunta():
    numero = input("Digite um numero romano: ")
    romano = numero.upper()
    return list(romano)

#####################
##Funcao cria lista##
#####################

def criaLista(lista):
    valores = []
    for numero in lista:
        if numero in TabelaRomanos:
            x = TabelaRomanos[numero]
            valores.append(x)
        else:
            print(f"Caractere inválido: {numero}")
            return None  # Retorna None para indicar um erro
    return valores

######################
##Funcao que compara##
######################

def comparar(lista):
    total = 0
    for i in range(len(lista)):
        if i < len(lista) - 1 and lista[i] < lista[i+1]:
            total -= lista[i]
        else:
            total += lista[i]
    return total
        
    

x = pergunta()
y = criaLista(x)
z = comparar(y)

print(z)