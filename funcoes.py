import random
def rolar_dados(n):
    lista = []
    for i in range(0,n):
        a = random.randint(1,6)
        lista.append(a)
    return lista
def guardar_dado(lista_dados, lista_dg, i):
    lista_dg.append(lista_dados[i])  
    lista_dados.pop(i)              
    return [lista_dados, lista_dg]  