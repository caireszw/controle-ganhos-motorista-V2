from modulos import utils
from modulos import calculos
from time import sleep
while True:
    utils.menu('Registrar Corrida','Lista de corridas', 'Buscar corrida', 'Resumo financeiro', 'Configurações motorista', 'Sair' )
    resp = utils.selecionarOpção('Digite a opção desejada')
    if resp == 1:
        utils.registrarCorrida()

    elif resp == 2:
        utils.visualizarCorridas()

    elif resp == 3:
        utils.buscarCorridas()

    elif resp == 4:
        calculos.contabilidadeDinheiro()
    
    elif resp == 5:
        calculos.configuraçõesMotorista()

    elif resp == 6:
        print('FIM DO PROGRAMA MUITO OBRIGADO!')  
        break
    else:
       print('OPÇÃO INVALIDA')
    sleep(1)
   