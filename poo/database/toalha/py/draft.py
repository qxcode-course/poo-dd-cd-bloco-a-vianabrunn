
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


toalha_p.dry(5)
print(toalha_p.wetness)
toalha_p.dry(10)
print(toalha_p.wetness)