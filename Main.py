from Conta import Conta

cc = Conta('1234', 'Juca', 1000)
print(f'Saldo: {cc.get_saldo()}')
#saque de 500

cc.saque(500)
cc.saque(700)

print(f'Saldo: {cc.get_saldo()}')

cc.deposito(-300)

#Usuario nao pode ter saldo negativo
print(f'Saldo: {cc.get_saldo()}')