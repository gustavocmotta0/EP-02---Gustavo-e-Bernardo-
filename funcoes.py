
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

dados_rolados = [2, 2, 2, 2]
dados_no_estoque = [1]
dado_para_remover = 0

print(remover_dado(dados_rolados, dados_no_estoque, dado_para_remover))

