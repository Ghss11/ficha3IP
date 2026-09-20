linhas = int(input())
colunas = int(input())

if linhas <= 0 or colunas <= 0:
    print("Dimensões do mapa inválidas!")
else:

# Leitura da matriz
    matriz = []
    for i in range(linhas):
        linha_atual = []
        for j in range(colunas):
            valor = int(input())
            linha_atual.append(valor)
        matriz.append(linha_atual)

# Analise das diagonais
    for i in range(linhas):
        for j in range(colunas):
            valor = matriz[i][j]
            if i == j:
                valor = valor * 2
            if linhas == colunas and (i + j) == (linhas - 1):
                valor = valor + 5
            if valor < 15:
                valor = 0
            if valor % 2 != 0:
                valor = valor + 1
            matriz[i][j] = valor

 # Impressão da matriz
    print("Avatar: A Lenda de Aang - Planejamento da Invasão!")
    print("Sokka: Mapeando os setores da Nação do Fogo...")
    for i in range(linhas):
        linha_texto = ""
        for j in range(colunas):
            if j == 0:
                linha_texto = linha_texto + str(matriz[i][j])
            else:
                linha_texto = linha_texto + " " + str(matriz[i][j])
        print(linha_texto)

# Relatório 
    soma_total = 0
    maior_valor = matriz[0][0]
    linha_critica = 0
    coluna_critica = 0
    for i in range(linhas):
        for j in range(colunas):
            soma_total += matriz[i][j]
            if matriz[i][j] > maior_valor:
                maior_valor = matriz[i][j]
                linha_critica = i
                coluna_critica = j

    print("--- RELATÓRIO DO TÚNEL E AMEAÇAS ---")
    print(f"Soma Total de Resistência: {soma_total}")
    print(f"Setor Mais Crítico: ({linha_critica}, {coluna_critica}) com valor {maior_valor}")

# Cenário estratégico
    if soma_total < 100:
        print("Sokka: O mapa revela poucas defesas inimigas!")
        print("Aang: Parece que o caminho está livre.")
        print("Katara: Conseguimos passar sem grandes problemas!")
        print("Estratégia aprovada! O Avatar está pronto para a batalha.")
    elif soma_total < 200:
        print("Sokka: Atenção! Detectamos resistência nas defesas da Nação do Fogo.")
        print("Toph: Sinto muitas tropas pelo solo, mas podemos avançar com cuidado.")
        print("Aang: Então vamos atentos. A Equipe Avatar está pronta!")
        print("Estratégia aprovada, mas a invasão será realizada com cautela.")
    else:
        print("Sokka: Alerta! As defesas inimigas são muito fortes!")
        print("Toph: A linha de defesa deles é densa demais para atravessarmos.")
        print("Aang: Então precisamos recuar e repensar nosso plano.")
        print("Alerta vermelho: Nível de ameaça crítico! Invasão adiada.")

# Missão do aliado
    aliado = input()
    limite_energia = int(input())

    sucesso = False
    if aliado == "Aang":
        if soma_total <= limite_energia:
            sucesso = True
    elif aliado == "Katara":
        pares = 0
        impares = 0
        for i in range(linhas):
            for j in range(colunas):
                if matriz[i][j] % 2 == 0:
                    pares += 1
                else:
                    impares += 1
        if pares > impares:
            sucesso = True
    elif aliado == "Toph":
        if maior_valor <= 50:
            sucesso = True
    elif aliado == "Sokka":
        if linhas == colunas:
            sucesso = True

    if sucesso:
        print(f"{aliado} usou sua especialidade com maestria e garantiu o sucesso na missão!")
    else:
        print(f"{aliado} encontrou barreiras intransponíveis e a missão precisou ser abortada...")