# Cabeçalho
print('Espaço: a fronteira final. Estas são as viagens da nave estelar Enterprise…')
print('Sua missão de cinco anos: explorar novos mundos, procurar novas vidas e novas civilizações, audaciosamente indo aonde nenhum homem jamais esteve.')
print('Dr. McCoy: Eu sou um médico, não um matemático. Mas tenho que fazer o que precisa ser feito.')
print('=====')


# Tamanho da amostra
tamanho_amostra = int(input(''))
while tamanho_amostra < 5 or tamanho_amostra > 12:
    print('Dr. McCoy: Esse número não é ideal, é possível trazer uma amostra de 5 a 12 indivíduos?')
    tamanho_amostra = int(input(''))

print(f'Dr. McCoy: Certo, {tamanho_amostra} indivíduos. É um número bom.')
print('=====')

# Leitura dos sinais vitais da amostra 
temp_lista = []
pulso_lista = []
gases_lista = []
pressao_lista = []
 
for i in range(tamanho_amostra):
    linha = input()
    partes = linha.split(" - ")
    temp_lista.append(float(partes[0].split(" ")[0]))
    pulso_lista.append(float(partes[1].split(" ")[0]))
    gases_lista.append(float(partes[2].split(" ")[0]))
    pressao_lista.append(float(partes[3].split(" ")[0]))

# Ordenar e calcular a mediana de cada sinal
temp_lista.sort()
pulso_lista.sort()
gases_lista.sort()
pressao_lista.sort()
 
n = tamanho_amostra
 
if n % 2 == 1:
    temp_mediana = temp_lista[n // 2]
else:
    temp_mediana = round((temp_lista[n // 2 - 1] + temp_lista[n // 2]) / 2, 1)
 
if n % 2 == 1:
    pulso_mediana = pulso_lista[n // 2]
else:
    pulso_mediana = round((pulso_lista[n // 2 - 1] + pulso_lista[n // 2]) / 2, 1)
 
if n % 2 == 1:
    gases_mediana = gases_lista[n // 2]
else:
    gases_mediana = round((gases_lista[n // 2 - 1] + gases_lista[n // 2]) / 2, 1)
 
if n % 2 == 1:
    pressao_mediana = pressao_lista[n // 2]
else:
    pressao_mediana = round((pressao_lista[n // 2 - 1] + pressao_lista[n // 2]) / 2, 1)
 
print("Relatório de dados da amostra:")
print(f"Temperatura: {temp_lista}")
print(f"Mediana: {temp_mediana}")
print(f"Frequência de pulso fluido: {pulso_lista}")
print(f"Mediana: {pulso_mediana}")
print(f"Frequência de troca gasosa: {gases_lista}")
print(f"Mediana: {gases_mediana}")
print(f"Pressão interna de homeostase: {pressao_lista}")
print(f"Mediana: {pressao_mediana}")
print("=====")

# Leitura dos sinais do paciente
print("Dr. McCoy: Agora irei medir os sinais do paciente.")
print("=====")

linha_paciente = input()
partes_paciente = linha_paciente.split(" - ")
temp_paciente = float(partes_paciente[0].split(" ")[0])
pulso_paciente = float(partes_paciente[1].split(" ")[0])
gases_paciente = float(partes_paciente[2].split(" ")[0])
pressao_paciente = float(partes_paciente[3].split(" ")[0])

# Diferença para a mediana
temp_diff = round(temp_paciente - temp_mediana, 1)
pulso_diff = round(pulso_paciente - pulso_mediana, 1)
gases_diff = round(gases_paciente - gases_mediana, 1)
pressao_diff = round(pressao_paciente - pressao_mediana, 1)

# Contagem de sinais críticos
sinais_criticos = 0
 
if temp_paciente > temp_lista[-1] or temp_paciente < temp_lista[0]:
    sinais_criticos += 1
 
if pulso_paciente > pulso_lista[-1] or pulso_paciente < pulso_lista[0]:
    sinais_criticos += 1
 
if gases_paciente > gases_lista[-1] or gases_paciente < gases_lista[0]:
    sinais_criticos += 1
 
if pressao_paciente > pressao_lista[-1] or pressao_paciente < pressao_lista[0]:
    sinais_criticos += 1
 
if sinais_criticos >= 2:
    avaliacao_final = "Alerta Crítico"
else:
    avaliacao_final = "Estável"
 
print("Relatório final:")
print(f"Temperatura do paciente: {temp_paciente}")
print(f"Diferença para a mediana: {temp_diff}")
print(f"Frequência de pulso fluido do paciente: {pulso_paciente}")
print(f"Diferença para a mediana: {pulso_diff}")
print(f"Frequência de troca gasosa: {gases_paciente}")
print(f"Diferença para a mediana: {gases_diff}")
print(f"Pressão interna de homeostase: {pressao_paciente}")
print(f"Diferença para a mediana: {pressao_diff}")
print(f"Quantidade de sinais críticos encontrados: {sinais_criticos}")
print(f"Avaliação final: {avaliacao_final}")
print("=====")
 
print("Dr. McCoy: Certo, agora sei o que fazer.")