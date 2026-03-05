class Personne:
    def __init__(self, nom, age):
        self._nom = nom
        self._age = age

    @property
    def age(self):
        return self._age
   #PRINT ..
    @age.setter
    def age(self, valeur):
        if not isinstance(valeur, int):
            raise TypeError("Entrez une val INT")
        if valeur < 0:
            raise ValueError("La val ne peut pas etre moins que 0")
        if valeur > 140:
            raise ValueError("L'Age ici est irrealiste")
        
        self._age = valeur

    def se_presenter(self):
    
        return f"Je suis {self._nom}, {self._age} ans"

personne1 = Personne("Sara", 29)
personne2 = Personne("Ahmed", 19)
personne3 = Personne("Med", 32)

print(personne1.se_presenter()) 
print(personne2.se_presenter()) 
print(personne3.se_presenter()) 

personne1.age = 30 
print(f"Nouvel âge de Sara : {personne1.age}")