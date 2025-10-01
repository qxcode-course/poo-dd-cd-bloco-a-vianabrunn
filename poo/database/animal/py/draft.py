class Animal:
    def __init__ (self, specie: str, sound: str):
        self.especie = specie
        self.som = sound 
        self.estagio = 0
    
    def __str__ (self) -> str:
        return f"especie: {self.especie}, estagio{self.estagio}, som?{self.som}"
    
    def estagio (self) -> int:
        if self.estagio == 0:
            return "filhote"
        elif self.estagio == 1:
            return "criança"
        elif self.estagio == 2:
             return "adulto"
        elif  self.estagio == 3:
            return "idoso"
        elif self.estagio == 4:
            return "morto"
        return 0
    
    def makeSound (self) ->str:
        if self.estagio == 0 :
            print("---")
        elif self.estagio>=4:
            print("RIP")
        else:
            print(self.som)

    def getMaxAge  (self) -> int:
        if self.estagio > 4:
          self.estagio = 4
        return 4
    
    def ageBy (self, increment: int) -> None:
        self.estagio += increment
        if self.estagio >= 4 :
            print(f"warning: {self.especie} morreu")
            self.estagio = 4

    def __str__(self)-> str:
        return f"{self.especie}:{self.estagio}:{self.som}"
    
def main():
    animal: Animal = ("", "")
    
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split()
        if args[0] == "end":
            break
        elif args[0] == "init":
            especie = args [1]
            som = args [2]
            animal = Animal(especie, som)
        elif args[0] == "show":
            print(animal)
        elif args[0] == "grow":
            increment: int = int(args[1])
            animal.ageBy(increment)
        elif args[0] == "noise":
            animal.makeSound()
        else:
            print("comando invalido")
main()