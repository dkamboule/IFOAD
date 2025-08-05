class GestionNotes:
    def __init__(self):
        self.etudiants = []
        self.matieres = []
        self.notes = []
    
    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)
    
    def supprimer_etudiant(self, matricule):
        # Supprimer l'étudiant et ses notes associées
        self.etudiants = [e for e in self.etudiants if e.matricule != matricule]
        self.notes = [n for n in self.notes if n.etudiant.matricule != matricule]
    
    def modifier_etudiant(self, matricule, new_data):
        for etudiant in self.etudiants:
            if etudiant.matricule == matricule:
                for key, value in new_data.items():
                    setattr(etudiant, key, value)
                return True
        return False
    
    def ajouter_matiere(self, matiere):
        self.matieres.append(matiere)
    
    def enregistrer_note(self, note):
        self.notes.append(note)
    
    def supprimer_note(self, etudiant_matricule, matiere_code):
        self.notes = [n for n in self.notes if not (n.etudiant.matricule == etudiant_matricule and n.matiere.code == matiere_code)]
    
    def modifier_note(self, etudiant_matricule, matiere_code, new_controle=None, new_tp=None, new_examen=None):
        for note in self.notes:
            if note.etudiant.matricule == etudiant_matricule and note.matiere.code == matiere_code:
                if new_controle is not None:
                    note.controle = new_controle
                if new_tp is not None:
                    note.tp = new_tp
                if new_examen is not None:
                    note.examen = new_examen
                return True
        return False
    
    def rechercher_etudiant(self, critere, valeur):
        if critere == "matricule":
            return [e for e in self.etudiants if e.matricule == valeur]
        elif critere == "nom":
            return [e for e in self.etudiants if e.nom.lower() == valeur.lower()]
        elif critere == "niveau":
            return [e for e in self.etudiants if e.niveau.lower() == valeur.lower()]
        return []
    
    def obtenir_notes_etudiant(self, etudiant):
        return [n for n in self.notes if n.etudiant.matricule == etudiant.matricule]
    
    def obtenir_notes_groupe(self, departement=None, niveau=None, matiere=None):
        result = self.notes
        if departement:
            result = [n for n in result if n.etudiant.departement == departement]
        if niveau:
            result = [n for n in result if n.etudiant.niveau == niveau]
        if matiere:
            result = [n for n in result if n.matiere.code == matiere.code]
        return result
    
    def calculer_moyennes_groupe(self, departement=None, niveau=None, matiere=None):
        notes_groupe = self.obtenir_notes_groupe(departement, niveau, matiere)
        moyennes = {}
        
        for note in notes_groupe:
            if note.etudiant.matricule not in moyennes:
                moyennes[note.etudiant.matricule] = {'etudiant': note.etudiant, 'matieres': {}}
            
            moyenne = note.calculer_moyenne()
            if moyenne is not None:
                moyennes[note.etudiant.matricule]['matieres'][note.matiere.code] = {
                    'matiere': note.matiere,
                    'moyenne': moyenne
                }
        
        # Calcul des moyennes générales
        for etud_data in moyennes.values():
            matieres = etud_data['matieres'].values()
            if matieres:
                etud_data['moyenne_generale'] = sum(m['moyenne'] for m in matieres) / len(matieres)
            else:
                etud_data['moyenne_generale'] = None
        
        return moyennes