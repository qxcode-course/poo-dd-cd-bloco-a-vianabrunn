
class Towel:
    def __init__ (self, color: str, size: str):
        self.color = color
        self.size = size
        self.wetness = 0
    
    def dry (self, amount: int)-> int:
        self.wetness += amount
        if self.wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()
    
    def getMaxWetness (self) ->int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0
    
    def wringOut (self) -> None:
        self.wetness = 0

    def isDry(self)->bool:
        seco = self.wetness == 0
        print("sim" if seco else "nao")
        return seco

    
    def __str__ (self)-> str:
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"
    
    
def main():
    toalha: Towel = (" ", " ")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split()
        if args[0] == "end":
            break        
        elif args[0] == "criar":
            color = args[1]
            size = args[2]
            toalha = Towel(color, size)
        elif args[0]  == "mostrar":
            print(toalha)
        elif args[0] == "enxugar":
            amount : int = int(args[1])
            toalha.dry(amount)
        elif args[0] == "torcer":
            toalha.wringOut()
        elif args[0] == "seca":
            toalha.isDry()
       
        else:
            print("comando invalido")
main()
