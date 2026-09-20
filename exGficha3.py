banco = []

linha = input()
while linha != "FIM":
    partes = linha.split(",")
    nome = partes[0]
    faccao = partes[1]
    dano_base = float(partes[2])
    inteligencia = int(partes[3])
    fator_caos = float(partes[4])

    nivel_inicial = dano_base + (inteligencia * fator_caos)

    if faccao == "Enclave":
        nivel_ameaca = nivel_inicial - (nivel_inicial * 0.15)
    else:
        nivel_ameaca = nivel_inicial

    banco.append((-nivel_ameaca, nome, faccao))

    linha = input()

#  Cópia do banco
analise = banco[:]

# Lista facções
faccoes = [item[2] for item in banco]

# Bônus de frequência
for i in range(len(analise)):
    nivel_ameaca = -analise[i][0]
    nome_atual = analise[i][1]
    faccao_atual = analise[i][2]

    frequencia_faccao = faccoes.count(faccao_atual)

    nivel_ajustado = nivel_ameaca + (nivel_ameaca * 0.05 * (frequencia_faccao - 1))

    analise[i] = (-nivel_ajustado, nome_atual, faccao_atual)

# Critérios de desempate
analise.sort()

# zonas relatório
zona_prioritaria = analise[:3]
zona_acompanhamento = analise[3:]

print(zona_prioritaria)