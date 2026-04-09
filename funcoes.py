import random
def rolar_dados(n):
    lista = []
    for i in range(0,n):
        a = random.randint(1,6)
        lista.append(a)
    return lista
print(rolar_dados(5))
