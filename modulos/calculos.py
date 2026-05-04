def lin():
    print('-'*30)

def contabilidadeDinheiro():
    arq = open('dados/corridas.txt','r')
    conteudo = arq.readlines()
    somaganhos = 0
    somakm = 0 
    for v in conteudo:
        dados = v.strip().split(';')
        somaganhos += float(dados[2].replace(',','.')) 
        somakm += float(dados[3].replace(',','.')) 
    arq.close()

    arq2 = open('dados/motorista.txt', 'r')
    conteudo2 = arq2.readlines()
    mediaconsumo = 0 
    preçocombustivel = 0 
    for v in conteudo2:
        dados = v.strip().split(';') 
        preçocombustivel += float(dados[2].replace(',','.'))
        mediaconsumo += float(dados[1].replace(',','.'))
    arq2.close()
    litros = somakm/mediaconsumo
    valorgasto = litros * preçocombustivel
    lucro = somaganhos - valorgasto
    lin()
    print('RELATORIO DE GANHOS')
    print('')
    print(f'GANHO TOTAL: R${somaganhos:.2f} \nTOTAL RODADO: {somakm:.2f} Kms \nVALOR GASTO: R${valorgasto:.2f} \nLUCRO: R${lucro:.2f}')

def configuraçõesMotorista():
    veiculo = input('Digite o modelo do seu carro: ')
    media = input('Digite a media de consumo do veiculo: ').replace(',','.')
    preço = input('Digite o valor atual da gasolina: ').replace(',','.')
    arq = open('dados/motorista.txt', 'w')
    linha = f'{veiculo};{media};{preço}'
    arq.write(linha)
    arq.close()
    print('CONFIGURAÇÕES INSERIDAS')
