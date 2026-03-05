class Personne:
    def __init__(self):
        pass

class Etudiant(Personne):
    def __init__(self):
        super().__init__()

class Salarie(Personne):
    def __init__(self):
        super().__init__()


class Doctorant(Salarie, Etudiant):
    def __init__(self, nom, salaire, notes):
       
        super().__init__(nom, salaire, notes)