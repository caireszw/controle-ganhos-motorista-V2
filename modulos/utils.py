
def lin():
    print('-'*30)


def cabeçalho(msg):
    lin()
    print(msg)
    lin()

def menu(*opc):
    cabeçalho('CONTROLE DE GANHOS - MOTORISTA')
    cont = 1
    for m in opc:
        print(f'{cont} - {m} ')
        cont +=1
    lin()

def selecionarOpção(msg):
    while True:
        try:
            resp = int(input(msg))
            return resp
        except ValueError:
            print('Tente novamente! Opção inválida.')
        except KeyboardInterrupt:
            print('\nUsuário forçou encerramento do sistema.')
            return 0
    

def registrarCorrida():
    try:
        arq = open('dados/corridas.txt', 'at')
        data = input('Digite o dia: ')
        app = input('Digite o app: ').upper()
        valor = input('Digite o valor: ').replace(',','.')
        km = input('Digite a Km percorrida: ').replace(',','.')
        linha = f'{data};{app};{valor};{km}\n'
        arq.write(linha)
        arq.close()
    except (ValueError, NameError):
        print('Invalido! Tente Novamente.')
    except KeyboardInterrupt:
        print('Usuario não digitou nada!')
        print('Encerrando programa!')
    else:
        print('Corrida cadastrada')    

def visualizarCorridas():
    arq = open('dados/corridas.txt','r')
    conteudo = arq.readlines()
    for d in conteudo:
        dados = d.strip().split(';')
        print(f'Data: {dados[0]} | Plataforma: {dados[1]} | Valor: R${dados[2]} | Km: {dados[3]}')
    arq.close()

def buscarCorridas():
    resp = input('Digite a data da corrida:')
    arq = open('dados/corridas.txt',('r'))
    conteudo = arq.readlines()
    encontrou = False
    for d in conteudo:
        dados = d.strip().split(';')
        if resp == dados[0]:
            print(f'Data {dados[0]} | Plataforma {dados[1]} | Valor: R$ {dados[2]} | KM: {dados[3]}')
            encontrou = True
    if encontrou == False:
        print(f'Nenhuma corrida encotrada na data de {resp}')

    arq.close()

