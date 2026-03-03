class Conta:
    def __init__(self, numero, titular, saldo):
        #Encapsulando os atributos
        #_  protegido (protected) (apenas as classes filhas tem acesso)
        #__ privado (private) (apenas a propria classe tem acesso)
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

    #GET ==> captura a variavel (sempre com retorno)
    def get_saldo(self):
        return self.__saldo

    #SET ==> altera uma variavel (sempre sem retorno)
    def saque(self, valor):
        if self.__saldo - valor <= 0 or valor < 0:
            print('Saldo insuficiente ou valor invalido para o saque')
        else:
            self.__saldo -= valor

    def deposito(self, valor):
        if valor <= 0:
            print('Valor inválido para deposito')
        else:
            self.__saldo += valor