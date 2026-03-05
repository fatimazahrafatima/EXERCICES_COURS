class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    def se_presenter(self):
        return f"Je suis {self.nom}, {self.age}"

personne1 = Personne("Sara", 29)
personne2 = Personne("Ahmed", 19)
personne3 = Personne("Med", 32)

print(personne1.se_presenter())
print(personne2.se_presenter())
print(personne3.se_presenter())