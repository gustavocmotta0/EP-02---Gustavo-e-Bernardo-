import random

cartela = cria_cartela()

for rodada in range(12):
    dados_rolados = [random.randint(1, 6) for _ in range(5)]
    dados_guardados = []
    rerrolagens = 0

    print(f"Dados rolados: {dados_rolados}")
    print(f"Dados guardados: {dados_guardados}")

    jogada_feita = False

    while jogada_feita == False:
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input()

        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            dados_guardados.append(dados_rolados[indice])
            dados_rolados.pop(indice)

        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            dados_rolados.append(dados_guardados[indice])
            dados_guardados.pop(indice)

        elif opcao == "3":
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados = [random.randint(1, 6) for _ in range(len(dados_rolados))]
                rerrolagens = rerrolagens + 1

        elif opcao == "4":
            imprime_cartela(cartela)

        elif opcao == "0":
            combinacao_feita = False
            while combinacao_feita == False:
                print("Digite a combinação desejada:")
                combinacao = input()

                if combinacao not in cartela:
                    print("Combinação inválida. Tente novamente.")
                elif cartela[combinacao] != -1:
                    print("Essa combinação já foi utilizada.")
                else:
                    todos_dados = dados_rolados + dados_guardados
                    cartela = faz_jogada(todos_dados, combinacao, cartela)
                    jogada_feita = True
                    combinacao_feita = True

        else:
            print("Opção inválida. Tente novamente.")

        if jogada_feita == False:
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")


pontuacao = 0
pontos_simples = 0

for chave in cartela:
    if cartela[chave] != -1:
        pontuacao = pontuacao + cartela[chave]
        if chave in ["1", "2", "3", "4", "5", "6"]:
            pontos_simples = pontos_simples + cartela[chave]

if pontos_simples >= 63:
    pontuacao = pontuacao + 35

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao}")