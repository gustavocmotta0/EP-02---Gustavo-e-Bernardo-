
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
    if 1 in faces and 2 in faces and 3 in faces and 4 in faces:
        return 15
    if 2 in faces and 3 in faces and 4 in faces and 5 in faces:
        return 15
    if 3 in faces and 4 in faces and 5 in faces and 6 in faces:
        return 15
    return 0

def calcula_pontos_sequencia_alta(faces):
    if 1 in faces and 2 in faces and 3 in faces and 4 in faces and 5 in faces:
        return 30
    if 2 in faces and 3 in faces and 4 in faces and 5 in faces and 6 in faces:
        return 30
    return 0

def calcula_pontos_full_house(dados):
    dados = sorted(dados)
    
    soma = 0
    if dados[0] == dados[1] and dados[2] == dados[3] == dados[4] and dados[0] != dados[2]:
        for i in range(len(dados)):
            soma += dados[i]
        return soma

    if dados[0] == dados[1] == dados[2] and dados[3] == dados[4] and dados[0] != dados[3]:
        for i in range(len(dados)):
            soma += dados[i]
        return soma

        
    
    return 0 

def calcula_pontos_quadra(dados):

    dados = sorted(dados)
    if len(dados) < 4:
        return 0 
    for i in range(3,len(dados)):
        soma = 0
        if dados[i - 3] == dados[i-2] == dados[i-1] == dados[i]:
            for i in range(0,len(dados)):
                soma += dados[i]
            return soma
        
    return 0

def calcula_pontos_quina(dados):

    dados = sorted(dados)
    if len(dados) < 5:
        return 0 
    for i in range(4,len(dados)):
        if dados[i-4] == dados[i - 3] == dados[i-2] == dados[i-1] == dados[i]:
    
            return 50
        
    return 0

def calcula_pontos_regra_avancada(dados):
    a = calcula_pontos_soma(dados):
    b = calcula_pontos_sequencia_baixa(dados)
    c = calcula_pontos_sequencia_alta(dados)
    e = calcula_pontos_regra_avancada(dados)
    f = calcula_pontos_full_house(dados)
    g = calcula_pontos_quina(dados)
    h = calcula_pontos_quadra (dados)
    return {
    'cinco_iguais': g,
    'full_house': f,
    'quadra': h,
    'sem_combinacao': a,
    'sequencia_alta': c,
    'sequencia_baixa': b
    }

