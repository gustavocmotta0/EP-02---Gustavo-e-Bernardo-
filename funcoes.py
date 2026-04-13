
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


def remover_dado(rolados, guardados, indice_removido):  
    rolados.append(guardados[indice_removido])
    guardados.pop(indice_removido)
    x = [rolados, guardados]
    return x

def calcula_pontos_regra_simples(faces_roladas):
    pontos = {1: faces_roladas.count(1), 2: faces_roladas.count(2) * 2,
              3: faces_roladas.count(3) * 3, 4: faces_roladas.count(4) * 4,
              5: faces_roladas.count(5) * 5, 6: faces_roladas.count(6) * 6}
    return pontos

def calcula_pontos_soma(faces_roladas):
    k = 0
    faces_roladas = sorted(faces_roladas)
    if faces_roladas in [[1,2,3,4,5][2,3,4,5,6]]:
        return 30
    if faces_roladas in [[1,2,3,4] , [2,3,4,5] , [3,4,5,6]]:
        return 15
    if faces_roladas in [[1,1,1,1,1] , [2,2,2,2,2] , [3,3,3,3,3], [4,4,4,4,4], [5,5,5,5,5], [6,6,6,6,6]]:
        return 50
    else: 
        i= 0 
        while i!=5:
            soma =  faces_roladas[i] + soma
            i = i  + 1
        return soma
        
    


            
