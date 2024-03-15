saldo_total = 12500.30
count_saque = count_deposito = 0

def sacar(saldo):

    saque = float(input('Insira o valor a sacar: '))
    
    if saque <= 0:
        print('Valor de Saque invalido, tente novamente')
    
    elif saque > 500:
        print('Limite máximo de R$ 500,00 por saque!')

    elif saque > saldo:
        print('Não será possível realizado o saque por motivos de Saldo insuficiente!')
        
    else:
        saldo -= saque
        global count_saque
        count_saque += 1
        #print(f'Saldo atual: {saldo:.2f}')
    return saldo 

def depositar(saldo):
    
    deposito = float(input('\nValor a depositar: '))

    if deposito > 0:
        saldo += deposito
        global count_deposito
        count_deposito += 1
        #print(f'Saldo atual: {saldo: .2f}') 
        
    else: print('Valor de deposito invalido')
    return saldo

def exibir_extrato(depositos, saques, saldo):

    print('Atualizações diárias da conta: \n')
    print(f'Depositos realizados: {depositos}')
    print(f'Saques realizados: {saques}')
    print(f'\nSaldo total em conta: R$ {saldo:.2f}')

index = """
[s] - Sacar
[d] - Depositar
[e] - Extrato
[q] - Sair\n
"""

while True:
    
    opcao = input(index)

    if opcao in ['s', 'S']:
        if (count_saque >= 3):
            print('Limites de 3 saques diários já realizados!')
        else:
            saldo_total = sacar(saldo_total)
    elif opcao in ['d', 'D']:
        saldo_total = depositar(saldo_total)
    elif opcao in ['e', 'E']:
        exibir_extrato(count_deposito, count_saque, saldo_total)
    elif opcao in ['q', 'Q']:
        break
    else:
        print('Opção inválida, tente novamente!')