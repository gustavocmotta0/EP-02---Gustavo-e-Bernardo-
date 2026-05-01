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
dados_rolados = rolar_dados(5)
dg = [] #dados gurdados
 
print(f"Dados rolados: {dados_rolados}")
print(f"Dados guardados: {dg}")
print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
 
k = 0
for i in range(12):
    rodada_encerrada = False
    while not rodada_encerrada:
        acao = input(">")
 
        if acao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            l = int(input(">"))
            resultado = guardar_dado(dados_rolados, dg, l)
            dados_rolados = resultado[0]
            dg = resultado[1]
 
        elif acao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            l = int(input(">"))
            resultado = remover_dado(dados_rolados, dg, l)
            dados_rolados = resultado[0]
            dg = resultado[1]

 
        elif acao == "3":
            if k <= 1:
                dados_rolados = rolar_dados(len(dados_rolados))
                k += 1
            else:
                print("Você já usou todas as rerrolagens.")
 
        elif acao == "4":
            imprime_cartela(cartela)
 
        elif acao == "0":
            print("Digite a combinação desejada:")
            jogada_feita = False
            while not jogada_feita:
                categoria = input(">")
 
                if categoria not in todas_combinacoes:
                    print("Combinação inválida. Tente novamente.")
                    continue
 
                if categoria in combinacoes_simples:
                    chave = int(categoria)
                    if cartela['regra_simples'][chave] != -1:
                        print("Essa combinação já foi utilizada.")
                        continue
                else:
                    if cartela['regra_avancada'][categoria] != -1:
                        print("Essa combinação já foi utilizada.")
                        continue
 
                todos_dados = dados_rolados + dg
                pontos_simples = calcula_pontos_regra_simples(todos_dados)
                pontos_avancado = calcula_pontos_regra_avancada(todos_dados)
 
                if categoria in combinacoes_simples:
                    chave = int(categoria)
                    cartela['regra_simples'][chave] = pontos_simples[chave]
                else:
                    cartela['regra_avancada'][categoria] = pontos_avancado[categoria]
 
                jogada_feita = True
                rodada_encerrada = True
 
            if rodada_encerrada:
                dados_rolados = rolar_dados(5)
                dg = []
                k = 0
 
        else:
            print("Opção inválida. Tente novamente.")
            continue
 
        if not rodada_encerrada:
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dg}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
 
    if i < 11:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dg}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
 
pontuacao = 0
soma_simples = 0
 
for chave, valor in cartela['regra_simples'].items():
    if valor != -1:
        pontuacao += valor
        soma_simples += valor
 
for chave, valor in cartela['regra_avancada'].items():
    if valor != -1:
        pontuacao += valor
 
if soma_simples >= 63:
    pontuacao += 35
 
imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao}")