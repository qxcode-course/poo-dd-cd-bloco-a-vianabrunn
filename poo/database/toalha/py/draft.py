
class Towel:
    def __init__(self, color: str, size: str): #construtor
        self.color = color #atributos
        self.size = size
        self.wetness = 0

    def dry(self, amount:int) -> None:
        self.wetness += amount
        if self.wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()
    
    def getMaxWetness(self) -> int:
        if self.size == "p":
            return 10
        if self.size == "m":
            return 20
        if self.size == "g":
            return 30
        return 0
    
    def isDry(self) -> bool:
        return self.wetness == 0
    
    def wringOut (self) -> None :
        self.wetness = 0

    def __str__ (self):
        return f"color:{self.color}, tam: {self.size}, umi: {self.wetness}"
    

toalha_g = Towel("green", "g") #refrencia e objetos
toalha_p = Towel("pink", "p")

def main():
    toalha = Towel("", "")
    while True:
        line: str = input()
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break 
        if args[0] == "new":
            color = args[1]
            size = args [2]
            toalha = Towel(color, size)
        elif args[0] == "show":
            print(toalha)
        elif args[0] == "dry":
            amount: int = int(args[1])
            toalha.dry(amount)
        else:
            print("Comando invalido")
main()