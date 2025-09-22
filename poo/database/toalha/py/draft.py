
class Towel:
    def __init__(self, color: str, size: str): #construtor
        self.color = color #atributos
        self.size = size
        self.wetness = 0

    def __str__ (self):
        return f"color:{self.color}, tam: {self.size}, umi: {self.wetness}"

toalha = Towel("green", "g") #refrencia e objetos
toalha = Towel("pink", "p")

print(toalha.color) #red
toalha.color = "white" 
print(toalha.color) #white
print(toalha.size)
print(toalha.wetness)
print(toalha)