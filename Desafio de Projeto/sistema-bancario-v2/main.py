EXTRATO_TXT = lambda txt: txt.ljust(10)
SAQUE_TXT = EXTRATO_TXT('Saque')
DEPOSITO_TXT = EXTRATO_TXT('Deposito')

def menu():
    opcoes = f"""   [0] Sair
    [1] Criar Usuario
    [2] Criar Conta
    [3] Extrato
    [4] Deposito
    [5] Saque
    [6] Lista Contas
    [7] Lista Usuarios
"""
    print(opcoes)

def filtra_usuario(cpf, usuarios):
    return [usr for usr in usuarios if cpf == usr.get("cpf")]

def listar_contas(contas):
    for conta in contas:
        print(conta)

def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(usuario)

def cria_conta(cpf, contas):
    sequencial_conta = max([cnt.get("numero_conta") for cnt in contas], default=0) + 1
    conta = {
        "agencia" : "0001",
        "numero_conta": sequencial_conta,
        "usuario": cpf,
        "status": "Ativa",
        "saldo": 0,
        "extrato": "",
        "saques_diarios": 0
    }

    contas.append(conta)

def cria_usuario(nome, dt_nasc, cpf, logradouro, nro, bairro, cidade, sigla, usuarios):
    usuario = filtra_usuario(cpf, usuarios)
    if usuario:
        print("Já existe um usuário com esse CPF cadastrado!")
        return None
    
    usuario = {
        "nome": nome,
        "dt_nasc": dt_nasc,
        "cpf": cpf,
        "endereco": f"{logradouro},{nro} - {bairro} - {cidade}/{sigla}"
    }

    usuarios.append(usuario)

def exibe_extrato(saldo, /, *, extrato):
    print("EXTRATO".center(100, '-'))
    print(extrato if extrato else "Não foram realizadas movimentações".center(100))
    print(f"Saldo: R$ {saldo:.2f}".rjust(100))
    print("-" * 100)

def deposita(saldo, valor, extrato):
    if valor < 0:
        print("Não é possível depositar valores negativos")
    else:
        saldo += valor
        extrato += DEPOSITO_TXT + f'R$ {valor:.2f}' + '\n'

    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, saques_diarios, limite_saques):
    if saques_diarios >= limite_saques:
        print("Limite de saques diários excedido")
    elif valor > limite:
        print(f"Valor inválido, o limite de saque é {limite}")
    elif valor > saldo:
        print(f"Não há saldo suficiente, seu saldo é {saldo}")
    else:
        saldo -= valor
        extrato += SAQUE_TXT + f'R$ {valor:.2f}' + '\n'
        saques_diarios += 1

    return saldo, extrato, saques_diarios

def main():
    contas = []
    usuarios = []
    LIMITE_MAX_SAQUE = 500.0
    LIMITE_SAQUE_DIARIO = 3

    while True:
        menu()
        opcao = input("Selecione uma opção:")
        if opcao == '0':
            break
        elif opcao == '1':
            cpf = input("Informe um CPF para ser cadastrado: ")
            nome = input("Informe um Nome: ")
            dt_nasc = input("Informe uma data de nascimento: ")
            logradouro = input("Informe um logradouro: ")
            nro = input("Informe o número da casa: ")
            bairro = input("Informe um bairro: ")
            cidade = input("Informe uma cidade: ")
            sigla = input("Informe uma sigla: ")
            cria_usuario(nome, dt_nasc, cpf, logradouro, nro, bairro, cidade, sigla, usuarios)
            print("Usuário cadastrado com sucesso!")
        elif opcao == '2':
            cpf = input("Informe um CPF para criar uma conta: ")
            usuario = filtra_usuario(cpf, usuarios)
            if not usuario:
                print("Usuário não existe!")
                continue
            cria_conta(cpf, contas)
            print("Conta criada com sucesso!")
        elif opcao == '3':
            cpf = input("Informe um CPF para exibir o extrato das contas: ")
            usuario = filtra_usuario(cpf, usuarios)
            if not usuario:
                print("Usuário não existe!")
                continue

            contas_usuario = [cnt for cnt in contas if cpf == cnt.get('usuario')]
            if not contas_usuario:
                print("Nenhuma conta encontrada para este usuário.")
                continue

            for conta in contas_usuario:
                exibe_extrato(conta['saldo'], extrato=conta['extrato'])
        elif opcao == '4':
            cpf = input("Informe um CPF para depositar: ")
            usuario = filtra_usuario(cpf, usuarios)
            if not usuario:
                print("Usuário não existe!")
                continue

            contas_usuario = [cnt for cnt in contas if cpf == cnt.get('usuario')]
            if not contas_usuario:
                print("Nenhuma conta encontrada para este usuário.")
                continue

            numero_conta = int(input("Informe o número da conta para depósito: "))
            conta = [cnt for cnt in contas_usuario if cnt.get('numero_conta') == numero_conta][:1]
            if not conta:
                print("Conta não encontrada.")
                continue
            else:
                conta = conta[0]

            valor = float(input("Informe o valor do depósito: "))
            conta['saldo'], conta['extrato'] = deposita(conta['saldo'], valor, conta['extrato'])
            print("Depósito realizado com sucesso!")
        elif opcao == '5':
            cpf = input("Informe um CPF para saque: ")
            usuario = filtra_usuario(cpf, usuarios)
            if not usuario:
                print("Usuário não existe!")
                continue

            contas_usuario = [cnt for cnt in contas if cpf == cnt.get('usuario')]
            if not contas_usuario:
                print("Nenhuma conta encontrada para este usuário.")
                continue

            numero_conta = int(input("Informe o número da conta para saque: "))
            conta = [cnt for cnt in contas_usuario if cnt.get('numero_conta') == numero_conta][:1]
            if not conta:
                print("Conta não encontrada.")
                continue
            else:
                conta = conta[0]

            valor = float(input("Informe o valor do saque: "))
            conta['saldo'], conta['extrato'], conta['saques_diarios'] = saque(
                saldo=conta['saldo'], 
                valor=valor, 
                extrato=conta['extrato'], 
                limite=LIMITE_MAX_SAQUE, 
                saques_diarios=conta['saques_diarios'], 
                limite_saques=LIMITE_SAQUE_DIARIO
            )
            print("Saque realizado com sucesso!")
        elif opcao == "6":
            listar_contas(contas)
        elif opcao == "7":
            listar_usuarios(usuario)
        else:
            print("Opção inválida, tente novamente.")
    

if __name__ == "__main__":
    main()
