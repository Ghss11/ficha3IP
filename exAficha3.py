listaDwight = []
listaJim = []
listaStanley = []
listaPhillips = []
listaMichel = []
continuar = True
while continuar:
    nomevendedor = (str(input(''))).upper()
    if nomevendedor == 'FIM':
        continuar = False
    else:
        nomempresa = (str(input('')))
        if nomevendedor == 'DWIGHT':
            listaDwight.append(nomempresa)
        elif nomevendedor == 'JIM':
            listaJim.append(nomempresa)
        elif nomevendedor == 'STANLEY':
            listaStanley.append(nomempresa)
        elif nomevendedor == 'PHILLIPS':
            listaPhillips.append(nomempresa)
        else:
            listaMichel.append(nomempresa)
# As vendas de cada um dos vendedores
if len(listaDwight) == 0:
    print('Dwight fez zero vendas hoje. Mais sorte amanhã!')
else:
    print(f'Dwight : {listaDwight}')

if len(listaJim) == 0:
    print('Jim passou o dia fazendo pegadinhas e não concluiu nenhuma venda!')
else:
    print(f'Jim : {listaJim}')

if len(listaStanley) == 0:
    print('Stanley acabou dormindo em serviço, amanhã ele estará mais descansado!')
else:
    print(f'Stanley : {listaStanley}')

if len(listaPhillips) == 0:
    print('Phillips se distraiu e acabou não fazendo vendas hoje!')
else:
    print(f'Phillips : {listaPhillips}')

if len(listaMichel) == 0:
    print('Michael não trabalhou como vendedor hoje, apenas foi um bom chefe.')
else:
    print('Michael realizou vendas hoje!')
    print(f'Michael : {listaMichel}')