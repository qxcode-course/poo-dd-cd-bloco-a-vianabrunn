
class Towel:
    def __init__(self, color: str, size: str): #construtor
        self.color = color #atributos
        self.size = size
        self.wetness = 0

    def __str__ (self):
        return f"color:{self.color}, tam: {self.size}, umi: {self.wetness}"

towel = Towel("green", "g") #refrencia e objetos
towel2 = Towel("pink", "p")

print(towel.color) #red
towel.color = "white" 
print(towel.color) #white
print(towel.size)
print(towel.wetness)
print(towel)