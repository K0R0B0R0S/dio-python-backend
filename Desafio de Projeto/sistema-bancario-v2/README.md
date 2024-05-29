# Sistema Bancário v2 --- READ ME DESATUALIZADO

Bem-vindo à primeira versão do sistema bancário! Este projeto implementa um conjunto básico de funcionalidades bancárias, incluindo saque, depósito e extrato.

Esse projeto tem como objetivo exercitar os `operadores`, `estuturas condicionais`, `estruturas de repetição` e `manipular strings`

## Funcionalidades

### Saque
- **Limite de Saques:** O sistema permite realizar até 3 saques diários.
- **Limite por Saque:** Cada saque possui um limite máximo de R$ 500,00.
- **Saldo Insuficiente:** Caso o usuário não tenha saldo suficiente, o sistema exibirá uma mensagem informando que não é possível realizar o saque.
- **Registro de Saques:** Todos os saques são armazenados e exibidos na operação de extrato.

### Depósito
- **Depósitos Positivos:** É possível depositar valores positivos na conta bancária.
- **Registro de Depósitos:** Todos os depósitos são armazenados e exibidos na operação de extrato.

### Extrato
- **Listagem de Movimentações:** Lista todos os depósitos e saques realizados na conta.
- **Saldo Atual:** Exibe o saldo atual da conta no final da listagem.
- **Sem Movimentações:** Caso não haja movimentações, o sistema exibe a mensagem "Não foram realizadas movimentações".
- **Formato dos Valores:** Os valores são exibidos no formato `R$ xxx,xx`.

## Como Executar

1. Clone este repositório:
    ```bash
    git clone https://github.com/K0R0B0R0S/dio-python-backend.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd Desafio de Projeto/sistema-bancario-v1
    ```
3. Execute o script principal (certifique-se de ter Python instalado):
    ```bash
    python main.py
    ```

## Exemplo de Uso

Aqui está um exemplo de como utilizar o sistema bancário:

1. **Realizar um Depósito:**
    ```
    >> Selecione uma opção: 
    << 2
    >> Quanto deseja depositar: 
    << 100
    >> Deposito efetuado com sucesso
    ```

2. **Realizar um Saque:**
    ```
    >> Selecione uma opção: 
    << 1
    >> Quanto deseja sacar: 
    << 501
    >> Valor inválido, o limite de saque é 500.0
    ```

3. **Exibir o Extrato:**
    ```
    >> Selecione uma opção: 
    << 3
    >> 
    ----------------------------------------------EXTRATO-----------------------------------------------
    Deposito  R$ 100.00
    Deposito  R$ 200.00
    ----------------------------------------------------------------------------------------------------
    ```

## Estrutura do Projeto

- `main.py`: Arquivo principal contendo a lógica do sistema bancário.
- `README.md`: Este arquivo, contendo informações sobre o projeto.

