import random
from funcoes import faz_jogada
from funcoes import imprime_cartela
from funcoes import calcula_pontos_regra_avancada
from funcoes import calcula_pontos_regra_simples
from funcoes import rolar_dados
from funcoes import guardar_dado
from funcoes import remover_dado

cartela = {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
 
combinacoes_simples = ["1", "2", "3", "4", "5", "6"]
combinacoes_avancadas = ["sem_combinacao", "quadra", "full_house", "sequencia_baixa", "sequencia_alta", "cinco_iguais"]
todas_combinacoes = combinacoes_simples + combinacoes_avancadas
 
imprime_cartela(cartela)







