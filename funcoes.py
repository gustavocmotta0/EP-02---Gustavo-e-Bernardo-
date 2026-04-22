
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
    i = 0
    soma = 0

    while i!=len(faces_roladas):
        soma =  faces_roladas[i] + soma
        i = i  + 1
    return soma
        
def calcula_pontos_sequencia_baixa(faces):
    faces = faces.sorted
    if [1,2,3,4] in faces or  [2,3,4,5] in faces or  [3,4,5,6] in faces:
        return 15
    return 0 


            
