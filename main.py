from modulos import utils
from time import sleep
while True:
    utils.menu('Registrar Corrida','Listar corridas', 'Buscar corrida', 'Resumo financeiro', 'Configurações do veículo', 'Remover corrida', 'Sair' )
    resp = int(input('Digite a opção desejada'))
    if resp == 1:
        utils.registrarCorrida()

    elif resp == 2:
        utils.visualizarCorridas()

    elif resp == 3:
        print('op3')

    elif resp == 4:
        print('op4')
    
    elif resp == 5:
     print('op5')

    elif resp == 6:
     print('op6')

    elif resp == 7:
        print('op7')  
        break
    else:
       print('OPÇÃO INVALIDA')
    sleep(0.5)
   