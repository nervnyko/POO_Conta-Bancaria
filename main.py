class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self._saldo = float(saldo_inicial)
        
    def depositar (self, valor):
        if valor <= 0:
            raise ValueError ("Depósito deve ser positivo.")
        self._saldo += valor

    def sacar (self, valor):
        if valor <= 0:
            raise ValueError ("Saque deve ser positivo.")
        if valor > self._saldo:
            raise RuntimeError ("Saldo insufienciente")
        self._saldo -= valor

    def ver_saldo (self):
        print(f"Saldo de {self.titular}: {self._saldo:.2f}")

    def pegar_saldo(self):
        return self._saldo

#Definindo a classe de conta corrente
class ContaCorrente (ContaBancaria):
    def __init__ (self, titular, saldo_inicial=0.0, limite=0.0):
        super().__init__(titular, saldo_inicial)
        self.limite = float (limite)
    
    def sacar (self, valor):
        if valor <= 0:
            raise ValueError ("Saque deve ser positivo.")
        if valor > self._saldo + self.limite:
            raise RuntimeError ("Limite excedido.")
        self._saldo -= valor

#Definindo a classe de conta poupança        
class ContaPoupanca (ContaBancaria):
    def __init__ (self, titular, saldo_inicial= 0.0, tax_rend = 0.0005 ):
        super ().__init__ (titular, saldo_inicial)
        self.taxa = float (tax_rend)

#Code para render o dinheiro
    def rendimento (self):
        if self._saldo > 0:
            self._saldo += self._saldo * self.taxa

conta1 = ContaCorrente ("Mateus Enter", 200, 400)
conta2 = ContaPoupanca ("Mateus Enter", 1000)


print ("Olá, seja bem-vinde a sua conta da WydenBank, como deseja continuar?")
print ("Digite o número da ação que deseja realizar e em seguida aperte Enter")
print ("1 - Conta Corrente \n2- Conta Poupança")
conta_type = int (input ())

#loop para conta corrente.
while conta_type == 1:
    print ("\nO que deseja fazer?")
    print ("\n1 - Exibir saldo \n2 - Depositar \n3 - Sacar \n4 - Mudar conta \n5 - Sair")
    action = int (input ())
    
    #match de ação de acordo com o input
    match action:
        case 1: 
            conta1.ver_saldo()

        case 2: 
            try:
                valor = float(input ("\nDigite o valor que deseja depositar: "))
                conta1.depositar(valor)
                conta = conta1
                print(f"Depósito realizado com sucesso! Seu saldo final é de: R$ {conta.pegar_saldo():.2f}")

            except ValueError as e:
                print ("\nErro.{e}")
                    
        case 3:
            try:
                valor = float (input("\nDigite o valor que deeseja sacar: "))
                conta1.sacar(valor)
                conta = conta1
                print (f"\nSaque realizado com sucesso, seu saldo final é de: R$ {conta.pegar_saldo():.2f}")

            except ValueError as e:
                print ("\nErro. {e}")
        
        case 4:
            print ("Mudando de conta...")
            conta_type = 2
                   
        case 5:
            break

#loop caso conta poupança
while conta_type == 2:                            
    print ("\nO que deseja fazer?")
    print ("\n1 - Exibir saldo \n2 - Depositar \n3 - Sacar \n4 - Mudar conta \n5 - Ver rendimento \n6 - Sair")
    action = int (input ())
    
    #match de ação de acordo com o input
    match action:
        case 1: 
            conta2.ver_saldo()
        #deposito
        case 2: 
            try:
                valor = float(input ("\nDigite o valor que deseja depositar: "))
                conta2.depositar(valor)
                conta = conta2
                print(f"Depósito realizado com sucesso! Seu saldo final é de: R$ {conta2.pegar_saldo():.2f}")

            except ValueError as e:
                print ("\nErro.{e}")
        #saque            
        case 3:
            try:
                valor = float (input("\nDigite o valor que deeseja sacar: "))
                conta2.sacar(valor)
                conta = conta2
                print (f"\nSaque realizado com sucesso, seu saldo final é de: R$ {conta.pegar_saldo():.2f}")

            except ValueError as e:
                print ("\nErro. {e}")
        
        case 4:
            print ("Mudando de conta...")
            conta_type = 1

        case 5: 
            conta2.rendimento ()
            print (f"Seu saldo com o rendimento fica: R$ {conta2._saldo}")

        case 6:
            break