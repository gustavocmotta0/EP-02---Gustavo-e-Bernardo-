import random
from funcoes import faz_jogada
from funcoes import imprime_cartela
from funcoes import calcula_pontos_regra_avancada
from funcoes import calcula_pontos_regra_simples
from funcoes import rolar_dados
from funcoes import guardar_dado
from funcoes import remover_dado

imprime_cartela(faz_jogada(rolar_dados(0),None,{}))
jogador_1 = 
indicej1 = 1
jogador_2 = 
indicej2 = 2
imprime_cartela()
dados_rolados_1 = rolar_dados(n)
dados_rolados_2 = rolar_dados(n)
dg = [] #dados guardados
print(dados_rolados_1)
k1 = 0
for i in range(12):
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    acao = input()
    if(acao == 1):
        print("Digite o índice do dado a ser guardado (0 a 4):")
        l = input()
        dg = guardar_dado(n)[1]
        print()
    if(acao == 2):
        print("Digite o índice do dado a ser removido (0 a 4):")
    if(acao == 3 and k1 <=1):
            rolar_dados
        






