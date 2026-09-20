reagentes_base = ("Metilamina", "Fenilacetona", "Hidróxido de Sódio", "Ácido Clorídrico", "Metilamina")
quantidades_ml = (500, 250, 150, 100, 300)
continuar = True
print('Sistema HeisenbergOS v2.0 - Monitor do Reator Inicializado...\n')
                                      
operador = str(input(''))
pressao_tanque = str(input(''))
status_mike = str(input(''))

# Fase 1: Verificação de Pressão do Tanque
if not pressao_tanque.isnumeric():
    print('Yo Jesse! Você colocou tempero onde devia ter um número de pressão! O reator pifou!')
    continuar = False
else:
    pressao_tanque = int(pressao_tanque)

    # Fase 2: Informações do Operador e Status
    if operador == 'Hank Schrader' or operador == 'Gomez':
        print('Alerta Vermelho: Agente do DEA detectado no laboratório!')
    status_limpo = status_mike.replace(" ", "")
    if status_limpo.isupper():
        print('Abaixe o tom de voz! Mike está escutando no microfone!')

    while continuar == True:
        acao_tupla = str(input(''))

        # Fase 3: Loop de Ações sobre a Tupla
        if acao_tupla == 'FIM':
            continuar = False
        elif acao_tupla == 'contar':
            ingrediente_alvo = str(input(''))
            quantidade = reagentes_base.count(ingrediente_alvo)
            if quantidade > 0:
                    print(f"O ingrediente {ingrediente_alvo} aparece {quantidade} vez(es) na receita base.")
            else:
                print(f'O Ingrediente {ingrediente_alvo} não foi encontrado, precisamos melhorar o nosso estoque!')

        elif acao_tupla == 'posicao':
            ingrediente_alvo = str(input(''))
        
            if ingrediente_alvo in reagentes_base:
                posicao = reagentes_base.index(ingrediente_alvo)
                print(f"O ingrediente {ingrediente_alvo} foi encontrado primeiro na posicao {posicao} da tupla.")
            else:
                print(f"Ingrediente {ingrediente_alvo} nao encontrado no registro fixo!")

        elif acao_tupla == "varrer":
                ingrediente_alvo = input()
                soma_total = 0
                for i in range(len(reagentes_base)):
                    if reagentes_base[i] == ingrediente_alvo:
                        ml = quantidades_ml[i]
                        print(f"Lote encontrado: {ingrediente_alvo} - {ml}ml")
                        soma_total = soma_total + ml
                print(f"Volume total de {ingrediente_alvo} no reator: {soma_total}ml")

        elif acao_tupla == 'concatenar':
            novo_ingrediente = str(input(''))  
            nova_quantidade = int(input(''))

            reagentes_base = reagentes_base + (novo_ingrediente,)
            quantidades_ml = quantidades_ml + (nova_quantidade,)
            print(f"Ingrediente adicionado à nova tupla! Tamanho atualizado: {len(reagentes_base)}")

        elif acao_tupla == "desempacotar":
                r1, r2, r3 = reagentes_base[-3], reagentes_base[-2], reagentes_base[-1]
                m1, m2, m3 = quantidades_ml[-3], quantidades_ml[-2], quantidades_ml[-1]
                print(f"Últimos 3 reativos do registro: {r1} ({m1}ml), {r2} ({m2}ml) e {r3} ({m3}ml).")

    # Fase 4: Regras de Operação do Reator (Decisão Final)

    if pressao_tanque >= 50 and status_limpo.upper() == 'TRANQUILO':
            print("Reação perfeita! Lote de 99.1% de pureza pronto para distribuição.")
    elif pressao_tanque < 15:
        print("Pressão crítica muito baixa! A mistura estragou, descarte o lote!")
    elif status_limpo.upper() == 'ALERTA' and len(reagentes_base) > 5:
        print("A receita ficou muito complexa para o tempo hábil! Limpe o reator antes que Mike chegue!")
    else:
        print("Ajustando exaustores... Mantenha o reator sob observação!")

    
