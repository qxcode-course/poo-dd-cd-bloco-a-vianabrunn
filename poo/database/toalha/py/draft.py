class Towel:
    def __init__ (self, color: str, size: str):
        self.cor = color
        self.tamanho = size
        self.wetness = 0

    def dry (self, amount: int) -> None:
         self.wetness += amount
         if self.wetness >= self.getMaxWetness():
            print("Toalha encharcada")
            self.wetness = self.getMaxWetness()
    
    def wringOut (self) -> None :
        self.wetness = 0

    def getMaxWetness (self) -> int:
        if self.tamanho == "p":
            return 10
        if self.tamanho == "m":
            return 20
        if self.tamanho == "g":
            return 30
        return 0

    def isDry (self) -> bool:
        return self.wetness == 0

    def show(self) -> None:
        print(self)
    
    def __str__ (self) -> str:
        return f"color:{self.cor}, tam:{self.tamanho}, umi:{self.wetness}"

def main():
    toalha = Towel("", "")
    while True:
        line: str = input()
        args: list[str] = line.split()
        if args[0] == "end":
            break        
        elif args[0] == "new":
            color = args[1]
            size = args[2]
            toalha = Towel(color, size)
        elif args[0]  == "show":
            print(toalha)
        elif args[0] == "dry":
            amount : int = int(args[1])
            toalha.dry(amount)
        elif args[0] == "secar":
            toalha.wringOut()
            print("a toalha secou por completo")
        else:
            print("comando invalido")
main()
