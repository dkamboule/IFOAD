from models.personne import Personne

class Etudiant(Personne):
    def __init__(self, matricule, nom, prenom, niveau, departement):
        super().__init__(nom, prenom)
        self.matricule = matricule
        self.niveau = niveau
        self.departement = departement
    
    def __str__(self):
        return f"{self.matricule}: {self.prenom} {self.nom} - {self.departement}/{self.niveau}"