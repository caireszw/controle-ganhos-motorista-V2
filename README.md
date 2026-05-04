#  Controle de Ganhos - Motorista

Sistema simples em Python para controle de corridas e cálculo de ganhos de um motorista de aplicativo.

## Funcionalidades

- Registrar corridas (data, aplicativo, valor e km)
- Listar todas as corridas
- Buscar corridas por data
- Calcular resumo financeiro:
  - Total ganho
  - Total de km rodados
  - Gasto com combustível
  - Lucro final
- Configurar dados do motorista (veículo, consumo e preço do combustível)

## Tecnologias utilizadas

- Python 3
- Manipulação de arquivos `.txt`

## Estrutura do projeto
 projeto
│
├── main.py
├── modulos/
│ ├── utils.py
│ ├── calculos.py
│
├── dados/
│ ├── corridas.txt
│ ├── motorista.txt
## Como usar

Ao iniciar o programa, será exibido um menu com opções:

- Registrar corrida
- Visualizar corridas
- Buscar corrida
- Ver resumo financeiro
- Configurar motorista
- Sair

Basta digitar o número da opção desejada.

## Observações

- Os dados são armazenados em arquivos `.txt`
- Use ponto (`.`) ou vírgula (`,`) para valores decimais
- O sistema é simples e voltado para aprendizado

