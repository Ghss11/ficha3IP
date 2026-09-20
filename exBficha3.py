kit_rick = ["colt_357", "distintivo", "radio_comunicador", "cantil", "curativo"]
kit_michonne = ["katana", "amolador", "binoculo", "faixa_curativo", "mapa"]
kit_daryl = ["arco e flecha","flechas","faca_de_caca", "corda", "carne_seca"]
kit_carol = ["facao", "bomba_de_fumaca", "sangue_zumbi", "fosforos", "biscoito"]
seukit  = ["taco_beisebol","besta","kit_medico", "feijao_enlatado", "walkie_talkie", "garrafa_agua","biscoito"]
sobrevivente = str(input(''))
# Escolha de companheiros e Primeiro dia
if sobrevivente == 'Rick':
    print('Um grande líder sempre ajuda sua equipe, Rick lhe dá uma lanterna para a noite')
    seukit.append('lanterna')

 # Primeiro Dia
    seukit.remove('taco_beisebol')
    kit_rick.append('taco_beisebol')
    print(f'Kit atual sobrevivente: {seukit}')

 # Segundo Dia
    recortados = seukit[2:]
    seukit = seukit[:2]
    for intem in recortados:
         kit_rick.append(intem)
    print('Agora com as costas mais leves, podemos continuar com a nossa caminhada\n')

elif sobrevivente == 'Michonne':
    print('Michonne é uma ótima combatente, ela te dá uma arma para você não passar apertos.')
    seukit.append('faca_afiada')

 # Primeiro Dia
    seukit.remove('kit_medico')
    print('Você usou o kit médico para socorrer Michonne!')
    print(f'Kit atual sobrevivente: {seukit}')

 # Segundo Dia
    recortados = seukit[2:]
    seukit = seukit[:2]
    for intem in recortados:
        kit_michonne.append(intem)
    print('Agora com as costas mais leves, podemos continuar com a nossa caminhada\n')
    
elif sobrevivente == 'Daryl':
    print('Daryl é um ótimo caçador. Ele te dá carne para comer na refeição')
    seukit.append('carne')

 # Primeiro Dia
    pos_seukit = seukit.index('besta')
    pos_daryl = kit_daryl.index('arco e flecha')

    seukit[pos_seukit] = 'arco e flecha'
    kit_daryl[pos_daryl] = 'besta'
    
    print(f'Kit atual sobrevivente: {seukit}')
    print(f'Kit atual Daryl: {kit_daryl}')

 # Segundo Dia
    recortados = seukit[2:]
    seukit = seukit[:2]
    for intem in recortados:
        kit_daryl.append(intem)
    print('Agora com as costas mais leves, podemos continuar com a nossa caminhada\n')

else: 
    print('Carol sabe como se esconder dos zumbis. Ela te dá uma ajuda.')
    seukit.append('roupa_de_camuflagem')

#  Primeiro Dia
    itens_para_remover = ["bomba_de_fumaca", "sangue_zumbi", "fosforos"]
    kit_carol = [item for item in kit_carol if item not in itens_para_remover]

    itens_para_carol = seukit[2:4]
    seukit = seukit[:2] + seukit[4:]
    for item in itens_para_carol:
        kit_carol.append(item)

 # Segundo Dia
    recortados = seukit[2:]
    seukit = seukit[:2]
    for intem in recortados:
        kit_carol.append(intem)
    print('Agora com as costas mais leves, podemos continuar com a nossa caminhada\n')

# Terceiro Dia
print('Finalmente chegamos em Alexandria!\n')
print(f'Ufa, podemos ficar aqui por um tempo,{sobrevivente}\n')

if sobrevivente == 'Rick':
    print(f'Kit do sobrevivente: {seukit}\n')
    print(f'Kit do {sobrevivente}: {kit_rick}')

elif sobrevivente == 'Michonne':
    print(f'Kit do sobrevivente: {seukit}\n')
    print(f'Kit do {sobrevivente}: {kit_michonne}')

elif sobrevivente == 'Daryl':
    print(f'Kit do sobrevivente: {seukit}\n')
    print(f'Kit do {sobrevivente}: {kit_daryl}')

else:
    print(f'Kit do sobrevivente: {seukit}\n')
    print(f'Kit do {sobrevivente}: {kit_carol}')
