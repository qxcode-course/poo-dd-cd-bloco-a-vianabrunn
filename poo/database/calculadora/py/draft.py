class Cal:
    def __init__ (self, battery: int, display: int, batteryMax: int):
        self.battery = battery
        self.display = display
        self.batteryMax = batteryMax

    def charge(self, amount:int)->int:
        self.battery += amount
        if self.battery >= self.batteryMax:
            self.battery = self.batteryMax
    
    def sum(self, a:int, b:int) -> None:
        if self.battery == 0:
            print("fail: bateria insuficiente")
           
        else:
            self.display = a+b
            self.battery -= 1

            return a+b
    
    def division (self, num: int, den:int) ->None :
        if self.battery == 0:
            print("fail: bateria insuficiente")
           
        elif den == 0 :
            print("fail: divisao por zero")
            self.battery -= 1
        else:
            self.display = num / den
            self.battery -=1
            return num / den

    def __str__(self) ->str:
        return f"display = {self.display:.2f}, battery = {self.battery}"

def main():
    calculadora = Cal(0, 0, 0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split()
        if args[0] == "end":
            break
        elif args[0] == "init":
            batteryMax = int(args[1])
            calculadora = Cal(0, 0, batteryMax)
        elif args[0] == "show":
            print(calculadora)
        elif args[0] == "charge":
            amount: int = int(args[1])
            calculadora.charge(amount)
        elif args[0] == "sum":
            a: int = int(args[1])
            b: int = int(args[2])
            calculadora.sum(a, b)
        elif args[0] == "div":
            num: int = int(args[1])
            den: int = int(args[2])
            calculadora.division(num, den)
        
main()        