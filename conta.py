# __ --> PRIVATE
class Conta:
    def __init__(self,numero,saldo,titular,limite):#Metodos Constructor
        print("MGTOW {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extratir(self):#Metodo
        print("O Saldo do {} é R${},00".format(self.__titular,self.__saldo))

    def depositar(self,valor):#Metodo
        self.__saldo = self.__saldo + valor
    def sacar(self,valor):
        if(self.__pode_sacar(valor)):
            self.__saldo   = (self.__saldo + self.__limite) - valor
        else:
            print("Não é possivel sacar o valor")

    def transferir(self,valor,destino):#ACESSAR UM OBJETO QUE NÃO É SELF
        print("Transferencia")
        self.sacar(valor)
        destino.depositar(valor)



    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return  valor_a_sacar <= valor_disponivel

    def get_saldo(self):#Getter
        return self.__saldo
    def get_titular(self):#Getter
        return self.__titular
    def get_numero(self):#Getter
        return self.__numero
    def get_limite(self):#Getter
        return self.__limite

    def set_saldo(self,saldo):#Setter
        self.__saldo = saldo

    def set_titular(self,titular):#Setter
        self.__titular = titular

    def set_numero(self,numero):#Setter
        self.__numero = numero

    def set_limite(self,limite):#Setter
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return {"BB":"001","Caixa":"007","Bradesco":"23"}