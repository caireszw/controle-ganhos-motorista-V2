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
    

def registrarCorrida():
    arquivo = 'corridas.txt' 
    arq = open('dados/corridas.txt', 'at')
    data = input('Digite o dia: ')
    app = input('Digite o app: ')
    valor = input('Digite o valor: ')
    km = input('Digite a Km percorrida: ')
    linha = f'{data};{app};{valor};{km}\n'
    arq.write(linha)
    arq.close()
    
def visualizarCorridas():
    arq = open('dados/corridas.txt','r')
    conteudo = arq.readlines()
    for d in conteudo:
        dados = d.strip().split(';')
        print(f'Data {d[0]}, Plataforma {d[1]}, Valor {d[2]}, Km {d[3]}')
    arq.close()
