# depósito - valores positivos, 1 usuário, depósitos armazenados em uma viarável e exibidos na operação de extrato
# saque -  no maximo 3 saques diarios, limite de 500R$, caso não tenha saldo em conta, deve exibir uma msg informando que não será possível sacar o dinheiro por falta de saldo, saques devem ser exibidos na operação de extrato
# extrato - essa operação deve listar todos os depósitos e saques realizados na conta. no fim da listagem dever ser exibido o saldo atual da conta.
# formato a ser exibido R$ xxx.xx| Ex: 1500.45= R$1500.45
print("Bem vindo(a) ao Banco MTI, essas são as nossas opções de operação")
menu =( '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
             
Qual operação deseja realizar: ''')

saldo = 0
limite= 500
extrato= 0
numeroSaques = 0
depositosFeitos=0
saquesFeitos=0
numeroMaximoDeSaques=3
extratoDepositoList=[]
extratoSaquesList=[]
while True:
    opcao = input(menu)
    if opcao.lower() == "d":
        print("Depósito")
        while True:
            deposito=float(input("Insira aqui o valor que você deseja depositar: "))
            if deposito<0:
                print("Você precisa inserir um valor minimo de R$1")
            else:
                extrato+=deposito
                depositosFeitos+=1
                extratoDepositoList.append(deposito)
                break
          
        
    elif opcao.lower() == "s":
        print("Saque")
        while True:
            if saquesFeitos<numeroMaximoDeSaques:
                saque=float(input("Insira aqui o valor que você deseja sacar: "))
                if saque<0 or saque>500:
                    print("Você tem que inserir um valor maior que R$0 e até R$500 ")
                elif saque>extrato:
                    print("Você não tem saldo suficiente")
                else:
                    extrato-=saque
                    saquesFeitos+=1
                    extratoSaquesList.append(saque)
                    break
            else: 
                 print(f"Você atingiu o número máximo de saques: {numeroMaximoDeSaques}")
                 break
    elif opcao.lower() == "e":
            for i in extratoDepositoList:
                print(f"Segue anexo os seus depósitos: R${i}")
            for x in extratoSaquesList:
               print(f"Segue anexo os seus saques: R$: {x}")
            print(f"O seu saldo atual da conta é: R${extrato:.2f}")
    elif opcao.lower() == "q":
            break
    else:
        print("Você digitou uma opção inválida.")


    