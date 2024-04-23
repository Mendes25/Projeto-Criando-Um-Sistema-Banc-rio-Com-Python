# depósito - valores positivos, 1 usuário, depósitos armazenados em uma viarável e exibidos na operação de extrato
# saque -  no maximo 3 saques diarios, limite de 500R$, caso não tenha saldo em conta, deve exibir uma msg informando que não será possível sacar o dinheiro por falta de saldo, saques devem ser exibidos na operação de extrato
# extrato - essa operação deve listar todos os depósitos e saques realizados na conta. no fim da listagem dever ser exibido o saldo atual da conta.
# formato a ser exibido R$ xxx.xx| Ex: 1500.45= R$1500.45
# criar uma função para cada requisito acima
# a função saque deve receber somente keyword (valor=valor) | return saldo e extrato
# a função depósito deve receber argumentos por posição (saldo,extrato) |return saldo e extrato
# a função extrato deve receber argumentos keyword e por posição | argumentos posicionais: saldo, argumentos nomeados: extrato
#  novas funções: criar usuário e criar conta corrente (a partir do usuário)
# criar usuário: NOME, DATA DE NASCIMENTO, CPF E ENDEREÇO(LOGRADOURO,NRO- BAIRRO- CIDADE/SIGLA - ESTADO) somente cpf deve ser armazenado.
#  conta corrente: agencia, número da conta e usuario. numero da conta é sequencial, iniciando em 1| numero da agencia é fixo "0001". o Usuário pode ter mais de uma conta, mas uma onta pertence somente a um usuário


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
extratoDepositoList=[]
extratoSaquesList=[]
def function_saque(saldo, extrato):

    saquesFeitos=0
    numeroMaximoDeSaques=3
    if saquesFeitos<numeroMaximoDeSaques:
            while True:
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
          print("Você atingiu o número máximo de saques por dia: {numeroMaximoDeSaques}")
    return saldo,extrato,saque

def function_deposito(saldo, extrato):
      deposito=float(input("Insira aqui o valor que você deseja depositar: "))
      if deposito<0:
        print("Você precisa inserir um valor minimo de R$1")
      else:
        extrato+=deposito
        extratoDepositoList.append(deposito)
        saldo+= deposito
        
        return saldo,extrato,deposito
      
def function_extrato(extrato,saldo):
    for i in extratoDepositoList:
        print(f"Segue anexo os seus depósitos: R${i}")
    for x in extratoSaquesList:
        print(f"Segue anexo os seus saques: R$: {x}")
    print(f"O seu saldo atual da conta é: R${extrato:.2f}")
    return saldo, extrato





while True:
    opção=input(menu)
    if opção.lower()=="s":
        saqueFun=function_saque(saldo=saldo, extrato=extrato)
        print(saqueFun)
    elif opção.lower()=="d":
        depositoFun=function_deposito(saldo,extrato)
        print(depositoFun)
    elif opção.lower()=="e":
        extratoFun=function_extrato(extrato,saldo)
        print(extratoFun)
    elif opção.lower()=="q":
        break
    else: 
        print("Você digitou uma opção inválida")