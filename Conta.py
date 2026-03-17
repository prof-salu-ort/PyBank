class Conta:
    # _  ==> protegido
    # __ ==> privado
    def __init__(self, numero, titular, saldo):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

    #Equivalente ao GET
    @property #decorator
    def titular(self):
        return self.__titular

    #Equivalente ao SET
    @titular.setter #decorator
    def titular(self, titular):
        if len(titular) > 1:
            self.__titular = titular
        else:
            print('O nome deve ter mais de 1 caractere')

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    #O usuario altera o saldo pelas funcoes de saque e deposito
    def saque(self, valor):
        if self.__saldo - valor > 0 and valor > 0:
            self.__saldo -= valor
            return True
        else:
            print('Saldo insuficiente ou valor invalido')
            return False

    def deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Valor invalido')

    def transfere(self, valor, favorecido):
        if self.saque(valor):
            favorecido.deposito(valor)


    '''
    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular
    '''