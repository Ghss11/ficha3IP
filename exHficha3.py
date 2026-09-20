# FASE 1 - A VARREDURA DA CENA

print("--- FASE 1: A VARREDURA ---")
print("Lisbon: Jane, focamos as buscas no quadrante delimitado.")

n_linhas_cena = int(input())

matriz_cena = []
for i in range(n_linhas_cena):
    linha = input()
    itens = linha.split(", ")
    matriz_cena.append(itens)

margens = input().split()
linha_inicio = int(margens[0])
linha_fim = int(margens[1])
coluna_inicio = int(margens[2])
coluna_fim = int(margens[3])

submatriz = []
for linha in matriz_cena[linha_inicio:linha_fim]:
    submatriz.append(linha[coluna_inicio:coluna_fim])

qtd_sangue = 0
qtd_arma = 0
smiley_encontrado = False

for linha_sub in submatriz:
    print(linha_sub)
    for item in linha_sub:
        if item == "Sangue":
            qtd_sangue += 1
        if item == "Arma":
            qtd_arma += 1
        if item == "Smiley":
            smiley_encontrado = True

if smiley_encontrado:
    smiley_texto = "Sim"
else:
    smiley_texto = "Nao"

print(f"Evidencias encontradas: Sangue ({qtd_sangue}), Arma ({qtd_arma}). Smiley ({smiley_texto})")
print()

# FASE 2 - A MATRIZ DE EVIDÊNCIAS

print("--- FASE 2: A MATRIZ DE EVIDÊNCIAS ---")
print("Patrick Jane: Às vezes, a verdade está escondida bem diante dos nossos olhos.")

dimensoes = input().split()
num_linhas = int(dimensoes[0])
num_colunas = int(dimensoes[1])

matriz_evidencias = []
for i in range(num_linhas):
    linha = input().split()
    linha_numerica = []
    for valor in linha:
        linha_numerica.append(int(valor))   
    matriz_evidencias.append(linha_numerica)

limiar = int(input())

matriz_binaria = []
for linha in matriz_evidencias:
    linha_binaria = [1 if valor >= limiar else 0 for valor in linha]
    matriz_binaria.append(linha_binaria)

for linha_binaria in matriz_binaria:
    print(" ".join([str(x) for x in linha_binaria]))

assinatura = [
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0]
]
altura_assinatura = 3
largura_assinatura = 5

assinatura_encontrada = False
linha_encontrada = -1
coluna_encontrada = -1

for i in range(num_linhas - altura_assinatura + 1):
    for j in range(num_colunas - largura_assinatura + 1):
        if not assinatura_encontrada:
            bate = True
            for di in range(altura_assinatura):
                for dj in range(largura_assinatura):
                    if matriz_binaria[i + di][j + dj] != assinatura[di][dj]:
                        bate = False
            if bate:
                assinatura_encontrada = True
                linha_encontrada = i
                coluna_encontrada = j

if assinatura_encontrada:
    print("Patrick Jane: Eu conheço esse sorriso.")
    print("RED JOHN DEIXOU UMA ASSINATURA!")
    print(f"ASSINATURA ENCONTRADA EM [{linha_encontrada}][{coluna_encontrada}]")
else:
    print("Patrick Jane: Nada aqui parece familiar.")

print()

# CRUZAMENTO DAS FASES 1 E 2

caso_red_john = smiley_encontrado or assinatura_encontrada

# FASE 3

if caso_red_john:
    print("--- FASE 3: A MENSAGEM ---")

    numeros_texto = input().split()
    numeros = [int(x) for x in numeros_texto]

    alfabeto = "abcdefghijklmnopqrstuvwxyz "

    caracteres = [alfabeto[(x // 2) % 27] if x % 2 == 0 else alfabeto[(x * 3 + 1) % 27] for x in numeros]

    mensagem = "".join(caracteres)

    print(f'Mensagem decodificada: "{mensagem}"')
    print("Jane: Ele acha que é mais esperto que eu. Nós vamos pegá-lo.")

else:
    print("--- FASE 3: O CÓDIGO ---")
    print("Patrick Jane: Vamos ver o que ele quis dizer dessa vez.")

    nota_cifrada = input()

    invertida = nota_cifrada[::-1]
    pares = invertida[::2]

    caracteres_finais = []
    for caractere in pares:
        if caractere.isupper():
            caracteres_finais.append(caractere.lower())
        elif caractere.islower():
            caracteres_finais.append(caractere.upper())
        else:
            caracteres_finais.append(caractere)

    mensagem_decodificada = "".join(caracteres_finais)

    qtd_j = 0
    for caractere in mensagem_decodificada:
        if caractere == "J" or caractere == "j":
            qtd_j += 1

    print("MENSAGEM DECODIFICADA!")
    print(f"Patrick Jane: '{mensagem_decodificada}'...")
    print("Patrick Jane: Esse caso acabou de dar uma reviravolta interessante.")
    print(f"Grau de Obsessão: {qtd_j} aparição(ões) da letra J na mensagem.")
    print("--- CASO ENCERRADO (por enquanto...) ---")