class Car:
    def __init__ (self, passageiros : int, km : int, gas: int):
        self.pas = passageiros
        self.km = 0
        self.gas = 0

    def passMax (self) -> int:
        if self.pas>2:
            self.pas = 2
        return 2
    
    def gasMax (self) -> int:
        if self.gas > 100:
            self.gas = 100
        return 100
    
    def enter (self) -> None:
        self.pas+=1
        if self.pas > self.passMax():
            print("fail: limite de pessoas atingido")
            self.pas = self.passMax()

    def leave(self) -> None:
        self.pas -= 1
        if self.pas < 0:
            print("fail: nao ha ninguem no carro")
            self.pas = 0
        
    
    def fuel(self, amount: int)-> int:
        self.gas += amount
        if self.gas > 100:
            self.gas = 100
        return 100
    
    def drive (self, amount:int)-> int:
        if self.pas == 0:
            print("fail: nao ha ninguem no carro")
        elif self.gas == 0:
            print("fail: tanque vazio")
        elif amount > self.gas:
            self.km += self.gas
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.gas = 0
        else:
            self.km += amount
            self.gas -= amount
        
    def __str__(self)-> str:
        return f"pass: {self.pas}, gas: {self.gas}, km: {self.km}"

def main():
    carro = Car(0, 0, 0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split()
        if args[0] == "enter":
            carro.enter()
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            amount: int = int(args[1])
            carro.fuel(amount)
        elif args[0] == "drive":
            amount:int = int(args[1])
            carro.drive(amount)
        elif args[0] == "show":
            print(carro)
        elif args[0] == "end":
            break
        else:
            print("fail: comando invalido")

main()
