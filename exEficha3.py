# LEITURA DOS HERÓIS
herois = []

linha = input()
while linha != "FIM":
    partes = linha.split(" - ")
    herois.append([partes[0], int(partes[1]), int(partes[2]),
                   int(partes[3]), int(partes[4]), int(partes[5])])
    linha = input()

# CABEÇALHO
print("========================================")
print("GDA - HERO DISPATCH SYSTEM")
print("========================================")
print("[ROBOT] Sistema de despacho iniciado.")
print(f"[ROBOT] {len(herois)} heróis disponíveis.")

qtd_ameacas = int(input())

# UMA VOLTA POR AMEAÇA
for ameaca in range(qtd_ameacas):
    dados = input().split(" - ")
    nome_ameaca = dados[0]
    nivel = int(dados[1])
    prioridade = dados[2]

    # atributo para posição
    if prioridade == "Força":
        indice = 1
    elif prioridade == "Resistência":
        indice = 2
    elif prioridade == "Velocidade":
        indice = 3
    elif prioridade == "Inteligência":
        indice = 4
    else:
        indice = 5

    # lista auxiliar
    ranking = []
    for heroi in herois:
        pontuacao = heroi[1] + heroi[2] + heroi[3] + heroi[4] + heroi[5]
        pontuacao += heroi[indice]
        ranking.append([heroi[0], pontuacao, heroi[indice]])

    # ordenação manual decrescente
    for i in range(len(ranking) - 1):
        for j in range(len(ranking) - 1 - i):
            trocar = False
            if ranking[j][1] < ranking[j + 1][1]:
                trocar = True
            elif ranking[j][1] == ranking[j + 1][1] and ranking[j][2] < ranking[j + 1][2]:
                trocar = True

            if trocar == True:
                guardado = ranking[j]
                ranking[j] = ranking[j + 1]
                ranking[j + 1] = guardado

    # dados da ameaça
    print("========================================")
    print("NOVA AMEAÇA DETECTADA")
    print("========================================")
    print(f"AMEAÇA: {nome_ameaca}")
    print(f"NÍVEL DE DIFICULDADE: {nivel}")
    print(f"PRIORIDADE: {prioridade}")
    print("[ROBOT] Analisando heróis disponíveis...")
    print("[ROBOT] Calculando compatibilidade...")
    print("[ROBOT] Análise concluída.")

    # ranking
    print("========================================")
    print("RANKING DE HERÓIS")
    print("========================================")
    for posicao in range(len(ranking)):
        print(f"{posicao + 1}. {ranking[posicao][0]} - {ranking[posicao][1]} pontos")
    print("----------------------------------------")

    # classificação da ameaça
    if nivel <= 30:
        classificacao = "SIMPLES"
        necessarios = 1
    elif nivel <= 70:
        classificacao = "MODERADA"
        necessarios = 2
    else:
        classificacao = "CRÍTICA"
        necessarios = 3

    despachados = min(necessarios, len(herois))

    print(f"[ROBOT] Ameaça {classificacao}.")
    print(f"[ROBOT] {necessarios} herói(s) serão despachados.")

    if necessarios > len(herois):
        print("[ROBOT] ALERTA!")
        print(f"[ROBOT] São necessários {necessarios} heróis,")
        print(f"[ROBOT] mas apenas {len(herois)} estão disponíveis.")
        print("[ROBOT] Despachando todos os heróis disponíveis.")
    else:
        print("[CECIL] Equipe selecionada para a missão.")

    print("EQUIPE DESPACHADA:")
    for posicao in range(despachados):
        print(f"> {ranking[posicao][0]}")
    print("========================================")