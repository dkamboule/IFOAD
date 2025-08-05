class Note:
    def __init__(self, etudiant, matiere, controle=None, tp=None, examen=None):
        self.etudiant = etudiant
        self.matiere = matiere
        self.controle = controle
        self.tp = tp
        self.examen = examen
    
    def calculer_moyenne(self):
        if not all([self.controle, self.tp, self.examen]):
            return None
        
        return (self.controle * self.matiere.coefficients['controle'] + 
                self.tp * self.matiere.coefficients['tp'] + 
                self.examen * self.matiere.coefficients['examen'])