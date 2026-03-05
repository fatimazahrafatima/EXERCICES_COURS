class Vehicule:
    def demarrer(self):
        print("Vehicule")

class Voiture(Vehicule):
    def demarrer(self):
        print("Voiture")

class Moto(Vehicule):
    def demarrer(self):
        print("Moto")


Vehicules = [voiture(), Moto()]

for v in vehicules:
    v.demarrer()