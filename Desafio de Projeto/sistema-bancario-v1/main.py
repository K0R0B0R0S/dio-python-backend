EXTRATO_TXT = lambda txt: txt.ljust(10)
SAQUE_TXT = EXTRATO_TXT('Saque')
DEPOSITO_TXT = EXTRATO_TXT('Deposito')


OPCOES = f"""[0] Sair
[1] Sacar
[2] Depositar
[3] Extrato
"""

extrato = ""
saldo = 0.0
saques_diarios = 0
LIMITE_MAX_SAQUE = 500.0
LIMITE_SAQUE_DIARIO = 3


print(OPCOES)

while True:
    opcao = input("Selecione uma opção:")
    
    #Saque
    if opcao == '1':
        #Verifica o limite diário de saque
        if saques_diarios >= LIMITE_SAQUE_DIARIO:
            print("Limite de saques diários excedido")
            continue

        qnt = float(input("Quanto deseja sacar:"))
        #Verifica se o valor a sacar utrapassa o limite de saque
        if qnt > LIMITE_MAX_SAQUE:
            print(f"Valor inválido, o limite de saque é {LIMITE_MAX_SAQUE}")
            continue

        #Verifica se o saldo é suficiente
        if qnt > saldo:
            print(f"Não há saldo suficiente, seu saldo é {saldo}")
            continue

        saldo -= qnt
        extrato += SAQUE_TXT + f'R$ {qnt:.2f}' + '\n'
        saques_diarios += 1
        print("Saque efetuado com sucesso!")


    #Deposito
    elif opcao == '2':
        qnt = float(input("Quanto deseja depositar:"))
        if qnt < 0:
            print("Não é possível depositar valores negativos")
            continue
        
        saldo += qnt
        extrato += DEPOSITO_TXT + f'R$ {qnt:.2f}' + '\n'
        print("Deposito efetuado com sucesso")

    #Extrato
    elif opcao == '3':
        print("EXTRATO".center(100, '-'))
        print(extrato if extrato else "Não foram realizadas movimentações".center(100))
        print("-" * 100)
        continue

    #Sair
    elif opcao == '0':
        print("Saindo, tenha um bom dia!")
        break

    #Opção inválida
    else:
        print("Opção inválida")
        continue