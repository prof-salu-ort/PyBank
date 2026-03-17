from Conta import Conta

cc1 = Conta(1234, 'Juca', 1000)

#print(f'Titular com get: {cc1.get_titular()}')
print(f'Titular com property: {cc1.titular}')

#alterando o titular via funcao set
#cc1.set_titular('Juca Pereira')

#alterando o titular via property
cc1.titular = 'Juca Pereira'

#print(f'Titular alterado com set: {cc1.get_titular()}')
print(f'Titular alterado com property: {cc1.titular}')

cc1.titular = 'Li'

print(f'Titular alterado com property: {cc1.titular}')

#deposito de 500 reais
cc1.deposito(500)

#saque de 150 reais
cc1.saque(150)

print(f'Saldo atual: R${cc1.saldo:.2f}')

#cc1.numero = 5
print(f'Numero: {cc1.numero}')

cc2 = Conta(1111, 'Ana', 1000)
cc3 = Conta(2222, 'Mauro', 700)

print(f'Saldo antes da transferencia [cc2] {cc2.saldo}:')
print(f'Saldo antes da transferencia [cc3] {cc3.saldo}:')
#transferir 200 de cc2 para cc3
cc2.transfere(2000, cc3)
print(f'Saldo depois da transferencia [cc2] {cc2.saldo}:')
print(f'Saldo depois da transferencia [cc3] {cc3.saldo}:')