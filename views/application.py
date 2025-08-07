import tkinter as tk
from tkinter import messagebox, ttk
from models.gestion_notes import GestionNotes
from models.etudiant import Etudiant
from models.matiere import Matiere
from models.note import Note

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion des Notes d'Étudiants")
        self.geometry("1000x700")
        self.gestion_notes = GestionNotes()
        
        # Variables pour la sélection actuelle
        self.etudiant_selectionne = None
        self.note_selectionnee = None
        
        # Ajout de données de test
        self.initialiser_donnees_test()
        
        self.creer_interface()
        self.actualiser_toutes_vues()  # Nouvelle méthode pour tout actualiser
    
    def actualiser_toutes_vues(self):
        """Met à jour toutes les listes et combobox"""
        self.actualiser_liste_etudiants()
        self.actualiser_combos_notes()
        self.actualiser_liste_notes()
    
    def initialiser_donnees_test(self):
        # Ajout d'étudiants
        etudiants = [
            Etudiant("ET001", "Dupont", "Jean", "L1", "Informatique"),
            Etudiant("ET002", "Martin", "Sophie", "L1", "Informatique"),
            Etudiant("ET003", "Durand", "Pierre", "L2", "Mathématiques"),
            Etudiant("ET004", "Leroy", "Marie", "L2", "Mathématiques")
        ]
        
        for etudiant in etudiants:
            self.gestion_notes.ajouter_etudiant(etudiant)
        
        # Ajout de matières avec coefficients
        matieres = [
            Matiere("MATH101", "Algèbre Linéaire", {'controle': 0.3, 'tp': 0.2, 'examen': 0.5}),
            Matiere("INFO101", "Programmation Python", {'controle': 0.4, 'tp': 0.3, 'examen': 0.3}),
            Matiere("PHYS101", "Physique Générale", {'controle': 0.3, 'tp': 0.1, 'examen': 0.6})
        ]
        
        for matiere in matieres:
            self.gestion_notes.ajouter_matiere(matiere)
        
        # Ajout de notes
        notes = [
            Note(etudiants[0], matieres[0], 14, 16, 12),
            Note(etudiants[0], matieres[1], 15, 18, 14),
            Note(etudiants[1], matieres[0], 12, 14, 10),
            Note(etudiants[1], matieres[1], 16, 15, 13),
            Note(etudiants[2], matieres[2], 10, 12, 14),
            Note(etudiants[3], matieres[2], 15, 16, 18)
        ]
        
        for note in notes:
            self.gestion_notes.enregistrer_note(note)
    
    def creer_interface(self):
        # Notebook (onglets)
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Onglet Gestion Étudiants
        frame_etudiants = ttk.Frame(notebook)
        notebook.add(frame_etudiants, text="Gestion Étudiants")
        self.creer_interface_etudiants(frame_etudiants)
        
        # Onglet Gestion Notes
        frame_notes = ttk.Frame(notebook)
        notebook.add(frame_notes, text="Gestion Notes")
        self.creer_interface_notes(frame_notes)
        
        # Onglet Recherche
        frame_recherche = ttk.Frame(notebook)
        notebook.add(frame_recherche, text="Recherche")
        self.creer_interface_recherche(frame_recherche)
        
        # Onglet Statistiques
        frame_stats = ttk.Frame(notebook)
        notebook.add(frame_stats, text="Statistiques")
        self.creer_interface_statistiques(frame_stats)
    
    def creer_interface_etudiants(self, parent):
        # Frame pour le formulaire
        frame_form = ttk.LabelFrame(parent, text="Gestion des étudiants")
        frame_form.pack(padx=10, pady=5, fill=tk.X)
        
        # Champs du formulaire
        ttk.Label(frame_form, text="Matricule:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_matricule = ttk.Entry(frame_form)
        self.entry_matricule.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(frame_form, text="Nom:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_nom = ttk.Entry(frame_form)
        self.entry_nom.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(frame_form, text="Prénom:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_prenom = ttk.Entry(frame_form)
        self.entry_prenom.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(frame_form, text="Niveau:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_niveau = ttk.Entry(frame_form)
        self.entry_niveau.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(frame_form, text="Département:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_departement = ttk.Entry(frame_form)
        self.entry_departement.grid(row=4, column=1, padx=5, pady=5, sticky=tk.EW)
        
        # Boutons CRUD
        frame_boutons = ttk.Frame(frame_form)
        frame_boutons.grid(row=5, column=0, columnspan=2, pady=10)
        
        btn_ajouter = ttk.Button(frame_boutons, text="Ajouter", command=self.ajouter_etudiant)
        btn_ajouter.pack(side=tk.LEFT, padx=5)
        
        btn_modifier = ttk.Button(frame_boutons, text="Modifier", command=self.modifier_etudiant)
        btn_modifier.pack(side=tk.LEFT, padx=5)
        
        btn_supprimer = ttk.Button(frame_boutons, text="Supprimer", command=self.supprimer_etudiant)
        btn_supprimer.pack(side=tk.LEFT, padx=5)
        
        btn_effacer = ttk.Button(frame_boutons, text="Effacer", command=self.effacer_formulaire_etudiant)
        btn_effacer.pack(side=tk.LEFT, padx=5)
        
        # Frame pour la liste des étudiants
        frame_liste = ttk.LabelFrame(parent, text="Liste des étudiants")
        frame_liste.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        # Treeview pour afficher les étudiants
        columns = ("matricule", "nom", "prenom", "niveau", "departement")
        self.tree_etudiants = ttk.Treeview(frame_liste, columns=columns, show="headings")
        
        for col in columns:
            self.tree_etudiants.heading(col, text=col.capitalize())
            self.tree_etudiants.column(col, width=100)
        
        self.tree_etudiants.pack(fill=tk.BOTH, expand=True)
        
        # Barre de défilement
        scrollbar = ttk.Scrollbar(frame_liste, orient=tk.VERTICAL, command=self.tree_etudiants.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree_etudiants.configure(yscrollcommand=scrollbar.set)
        
        # Lier la sélection dans la treeview
        self.tree_etudiants.bind("<<TreeviewSelect>>", self.selectionner_etudiant)
        
        # Remplir la Treeview avec les étudiants existants
        self.actualiser_liste_etudiants()
    
    def selectionner_etudiant(self, event):
        selection = self.tree_etudiants.selection()
        if not selection:
            return
        
        item = self.tree_etudiants.item(selection[0])
        matricule = item['values'][0]
        
        # Trouver l'étudiant
        etudiants = self.gestion_notes.rechercher_etudiant("matricule", matricule)
        if not etudiants:
            return
        
        self.etudiant_selectionne = etudiants[0]
        
        # Remplir le formulaire avec les données de l'étudiant
        self.entry_matricule.delete(0, tk.END)
        self.entry_matricule.insert(0, self.etudiant_selectionne.matricule)
        
        self.entry_nom.delete(0, tk.END)
        self.entry_nom.insert(0, self.etudiant_selectionne.nom)
        
        self.entry_prenom.delete(0, tk.END)
        self.entry_prenom.insert(0, self.etudiant_selectionne.prenom)
        
        self.entry_niveau.delete(0, tk.END)
        self.entry_niveau.insert(0, self.etudiant_selectionne.niveau)
        
        self.entry_departement.delete(0, tk.END)
        self.entry_departement.insert(0, self.etudiant_selectionne.departement)
    
    def ajouter_etudiant(self):
        try:
            # Récupération des valeurs du formulaire
            matricule = self.entry_matricule.get()
            nom = self.entry_nom.get()
            prenom = self.entry_prenom.get()
            niveau = self.entry_niveau.get()
            departement = self.entry_departement.get()

            # Validation des champs
            if not all([matricule, nom, prenom, niveau, departement]):
                raise ValueError("Tous les champs sont obligatoires")

            # Vérification de l'unicité du matricule
            if any(e.matricule == matricule for e in self.gestion_notes.etudiants):
                raise ValueError("Un étudiant avec ce matricule existe déjà")

            # Création et ajout du nouvel étudiant
            nouvel_etudiant = Etudiant(matricule, nom, prenom, niveau, departement)
            self.gestion_notes.ajouter_etudiant(nouvel_etudiant)
            
            # Réinitialisation et actualisation
            self.effacer_formulaire_etudiant()
            self.actualiser_toutes_vues()  # Actualise toutes les vues
            
            messagebox.showinfo("Succès", "Étudiant ajouté avec succès")

        except Exception as e:
            messagebox.showerror("Erreur", str(e))
        
    def modifier_etudiant(self):
        if not self.etudiant_selectionne:
            messagebox.showerror("Erreur", "Aucun étudiant sélectionné")
            return
        
        matricule = self.entry_matricule.get()
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()
        niveau = self.entry_niveau.get()
        departement = self.entry_departement.get()
        
        if not all([matricule, nom, prenom, niveau, departement]):
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires")
            return
        
        # Vérifier si le matricule a changé et s'il existe déjà
        if matricule != self.etudiant_selectionne.matricule and self.gestion_notes.rechercher_etudiant("matricule", matricule):
            messagebox.showerror("Erreur", "Un étudiant avec ce matricule existe déjà")
            return
        
        new_data = {
            'matricule': matricule,
            'nom': nom,
            'prenom': prenom,
            'niveau': niveau,
            'departement': departement
        }
        
        if self.gestion_notes.modifier_etudiant(self.etudiant_selectionne.matricule, new_data):
            messagebox.showinfo("Succès", "Étudiant modifié avec succès")
            self.actualiser_liste_etudiants()
            self.etudiant_selectionne = None
            self.effacer_formulaire_etudiant()
        else:
            messagebox.showerror("Erreur", "Échec de la modification de l'étudiant")
    
    def supprimer_etudiant(self):
        if not self.etudiant_selectionne:
            messagebox.showerror("Erreur", "Aucun étudiant sélectionné")
            return
        
        if messagebox.askyesno("Confirmation", f"Voulez-vous vraiment supprimer l'étudiant {self.etudiant_selectionne.matricule} ?"):
            self.gestion_notes.supprimer_etudiant(self.etudiant_selectionne.matricule)
            messagebox.showinfo("Succès", "Étudiant supprimé avec succès")
            self.actualiser_liste_etudiants()
            self.etudiant_selectionne = None
            self.effacer_formulaire_etudiant()
    
    def effacer_formulaire_etudiant(self):
        self.entry_matricule.delete(0, tk.END)
        self.entry_nom.delete(0, tk.END)
        self.entry_prenom.delete(0, tk.END)
        self.entry_niveau.delete(0, tk.END)
        self.entry_departement.delete(0, tk.END)
        self.etudiant_selectionne = None
    
    def actualiser_liste_etudiants(self):
        # Vider la Treeview
        for item in self.tree_etudiants.get_children():
            self.tree_etudiants.delete(item)
        
        # Ajouter les étudiants
        for etudiant in self.gestion_notes.etudiants:
            self.tree_etudiants.insert("", tk.END, values=(
                etudiant.matricule,
                etudiant.nom,
                etudiant.prenom,
                etudiant.niveau,
                etudiant.departement
            ))
    
    def creer_interface_notes(self, parent):
        # Frame pour le formulaire
        frame_form = ttk.LabelFrame(parent, text="Gestion des notes")
        frame_form.pack(padx=10, pady=5, fill=tk.X)
        
        # Combobox pour sélectionner l'étudiant
        ttk.Label(frame_form, text="Étudiant:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_etudiant = ttk.Combobox(frame_form, state="readonly")
        self.combo_etudiant.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        
        # Combobox pour sélectionner la matière
        ttk.Label(frame_form, text="Matière:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_matiere = ttk.Combobox(frame_form, state="readonly")
        self.combo_matiere.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
        
        # Notes
        ttk.Label(frame_form, text="Contrôle:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_controle = ttk.Entry(frame_form)
        self.entry_controle.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(frame_form, text="TP:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_tp = ttk.Entry(frame_form)
        self.entry_tp.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(frame_form, text="Examen:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_examen = ttk.Entry(frame_form)
        self.entry_examen.grid(row=4, column=1, padx=5, pady=5, sticky=tk.EW)
        
        # Boutons CRUD
        frame_boutons = ttk.Frame(frame_form)
        frame_boutons.grid(row=5, column=0, columnspan=2, pady=10)
        
        btn_enregistrer = ttk.Button(frame_boutons, text="Enregistrer", command=self.enregistrer_note)
        btn_enregistrer.pack(side=tk.LEFT, padx=5)
        
        btn_modifier_note = ttk.Button(frame_boutons, text="Modifier", command=self.modifier_note)
        btn_modifier_note.pack(side=tk.LEFT, padx=5)
        
        btn_supprimer_note = ttk.Button(frame_boutons, text="Supprimer", command=self.supprimer_note)
        btn_supprimer_note.pack(side=tk.LEFT, padx=5)
        
        btn_effacer_note = ttk.Button(frame_boutons, text="Effacer", command=self.effacer_formulaire_note)
        btn_effacer_note.pack(side=tk.LEFT, padx=5)
        
        # Actualiser les combobox
        self.actualiser_combos_notes()
        
        # Frame pour la liste des notes
        frame_liste = ttk.LabelFrame(parent, text="Liste des notes")
        frame_liste.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        # Treeview pour afficher les notes
        columns = ("etudiant", "matiere", "controle", "tp", "examen", "moyenne")
        self.tree_notes = ttk.Treeview(frame_liste, columns=columns, show="headings")
        
        for col in columns:
            self.tree_notes.heading(col, text=col.capitalize())
            self.tree_notes.column(col, width=100)
        
        self.tree_notes.pack(fill=tk.BOTH, expand=True)
        
        # Barre de défilement
        scrollbar = ttk.Scrollbar(frame_liste, orient=tk.VERTICAL, command=self.tree_notes.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree_notes.configure(yscrollcommand=scrollbar.set)
        
        # Lier la sélection dans la treeview
        self.tree_notes.bind("<<TreeviewSelect>>", self.selectionner_note)
        
        # Remplir la Treeview avec les notes existantes
        self.actualiser_liste_notes()
    
    def selectionner_note(self, event):
        selection = self.tree_notes.selection()
        if not selection:
            return
        
        item = self.tree_notes.item(selection[0])
        etudiant_str = item['values'][0]
        matiere_str = item['values'][1]
        
        # Trouver l'étudiant et la matière
        matricule = etudiant_str.split(" - ")[0]
        code_matiere = matiere_str.split(" - ")[0]
        
        # Stocker la note sélectionnée
        self.note_selectionnee = (matricule, code_matiere)
        
        # Remplir les combobox et les champs
        # Trouver l'index de l'étudiant et de la matière dans les combobox
        etudiants = [f"{e.matricule} - {e.nom} {e.prenom}" for e in self.gestion_notes.etudiants]
        matieres = [f"{m.code} - {m.nom}" for m in self.gestion_notes.matieres]
        
        try:
            index_etudiant = etudiants.index(f"{matricule} - {etudiant_str.split(' - ')[1]}")
            index_matiere = matieres.index(f"{code_matiere} - {matiere_str.split(' - ')[1]}")
            
            self.combo_etudiant.current(index_etudiant)
            self.combo_matiere.current(index_matiere)
            
            # Remplir les notes
            controle = item['values'][2]
            tp = item['values'][3]
            examen = item['values'][4]
            
            self.entry_controle.delete(0, tk.END)
            self.entry_controle.insert(0, controle if controle != "N/A" else "")
            
            self.entry_tp.delete(0, tk.END)
            self.entry_tp.insert(0, tp if tp != "N/A" else "")
            
            self.entry_examen.delete(0, tk.END)
            self.entry_examen.insert(0, examen if examen != "N/A" else "")
        except ValueError:
            pass
    
    def actualiser_combos_notes(self):
        """Met à jour les ComboBox de l'onglet Notes"""
        # Liste des étudiants formatée
        etudiants = [f"{e.matricule} - {e.nom} {e.prenom}" for e in self.gestion_notes.etudiants]
        self.combo_etudiant['values'] = etudiants
        
        # Sélection du premier étudiant si la liste n'est pas vide
        if etudiants and not self.combo_etudiant.get():
            self.combo_etudiant.current(0)
        
        # Liste des matières formatée
        matieres = [f"{m.code} - {m.nom}" for m in self.gestion_notes.matieres]
        self.combo_matiere['values'] = matieres
        
        # Sélection de la première matière si la liste n'est pas vide
        if matieres and not self.combo_matiere.get():
            self.combo_matiere.current(0)
    
    def enregistrer_note(self):
        try:
            # Vérification de la sélection d'un étudiant et d'une matière
            etudiant_str = self.combo_etudiant.get()
            matiere_str = self.combo_matiere.get()
            
            if not etudiant_str or not matiere_str:
                raise ValueError("Veuillez sélectionner un étudiant et une matière")
            
            # Extraction du matricule et du code matière
            matricule = etudiant_str.split(" - ")[0]
            code_matiere = matiere_str.split(" - ")[0]
            
            # Récupération des objets correspondants
            etudiant = next(e for e in self.gestion_notes.etudiants if e.matricule == matricule)
            matiere = next(m for m in self.gestion_notes.matieres if m.code == code_matiere)
            
            # Validation des notes
            controle = float(self.entry_controle.get()) if self.entry_controle.get() else None
            tp = float(self.entry_tp.get()) if self.entry_tp.get() else None
            examen = float(self.entry_examen.get()) if self.entry_examen.get() else None
            
            for note in [controle, tp, examen]:
                if note is not None and not (0 <= note <= 20):
                    raise ValueError("Les notes doivent être entre 0 et 20")
            
            # Création et enregistrement de la note
            nouvelle_note = Note(etudiant, matiere, controle, tp, examen)
            self.gestion_notes.enregistrer_note(nouvelle_note)
            
            # Réinitialisation et actualisation
            self.effacer_formulaire_note()
            self.actualiser_liste_notes()
            
            messagebox.showinfo("Succès", "Note enregistrée avec succès")
            
        except ValueError as ve:
            messagebox.showerror("Erreur de valeur", str(ve))
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue: {str(e)}")

    
    def modifier_note(self):
        if not self.note_selectionnee:
            messagebox.showerror("Erreur", "Aucune note sélectionnée")
            return
        
        matricule, code_matiere = self.note_selectionnee
        
        # Récupérer les nouvelles valeurs
        try:
            new_controle = float(self.entry_controle.get()) if self.entry_controle.get() else None
            new_tp = float(self.entry_tp.get()) if self.entry_tp.get() else None
            new_examen = float(self.entry_examen.get()) if self.entry_examen.get() else None
        except ValueError:
            messagebox.showerror("Erreur", "Les notes doivent être des nombres")
            return
        
        # Vérifier que les notes sont entre 0 et 20
        for note in [new_controle, new_tp, new_examen]:
            if note is not None and (note < 0 or note > 20):
                messagebox.showerror("Erreur", "Les notes doivent être entre 0 et 20")
                return
        
        if self.gestion_notes.modifier_note(matricule, code_matiere, new_controle, new_tp, new_examen):
            messagebox.showinfo("Succès", "Note modifiée avec succès")
            self.actualiser_liste_notes()
            self.note_selectionnee = None
            self.effacer_formulaire_note()
        else:
            messagebox.showerror("Erreur", "Échec de la modification de la note")
    
    def supprimer_note(self):
        if not self.note_selectionnee:
            messagebox.showerror("Erreur", "Aucune note sélectionnée")
            return
        
        matricule, code_matiere = self.note_selectionnee
        
        if messagebox.askyesno("Confirmation", "Voulez-vous vraiment supprimer cette note ?"):
            self.gestion_notes.supprimer_note(matricule, code_matiere)
            messagebox.showinfo("Succès", "Note supprimée avec succès")
            self.actualiser_liste_notes()
            self.note_selectionnee = None
            self.effacer_formulaire_note()
    
    def effacer_formulaire_note(self):
        self.entry_controle.delete(0, tk.END)
        self.entry_tp.delete(0, tk.END)
        self.entry_examen.delete(0, tk.END)
        self.note_selectionnee = None
    
    def actualiser_liste_notes(self):
        # Vider la Treeview
        for item in self.tree_notes.get_children():
            self.tree_notes.delete(item)
        
        # Ajouter les notes
        for note in self.gestion_notes.notes:
            moyenne = note.calculer_moyenne()
            moyenne_str = f"{moyenne:.2f}" if moyenne is not None else "N/A"
            
            self.tree_notes.insert("", tk.END, values=(
                f"{note.etudiant.nom} {note.etudiant.prenom}",
                note.matiere.nom,
                note.controle if note.controle is not None else "N/A",
                note.tp if note.tp is not None else "N/A",
                note.examen if note.examen is not None else "N/A",
                moyenne_str
            ))
    
    def creer_interface_recherche(self, parent):
        # Frame pour les critères de recherche
        frame_criteres = ttk.LabelFrame(parent, text="Critères de recherche")
        frame_criteres.pack(padx=10, pady=5, fill=tk.X)
        
        # Options de recherche
        ttk.Label(frame_criteres, text="Rechercher par:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.recherche_var = tk.StringVar(value="matricule")
        
        ttk.Radiobutton(frame_criteres, text="Matricule", variable=self.recherche_var, value="matricule").grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        ttk.Radiobutton(frame_criteres, text="Nom", variable=self.recherche_var, value="nom").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        ttk.Radiobutton(frame_criteres, text="Niveau", variable=self.recherche_var, value="niveau").grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)
        
        # Champ de recherche
        ttk.Label(frame_criteres, text="Valeur:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_recherche = ttk.Entry(frame_criteres)
        self.entry_recherche.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky=tk.EW)
        
        # Bouton de recherche
        btn_rechercher = ttk.Button(frame_criteres, text="Rechercher", command=self.rechercher_etudiants)
        btn_rechercher.grid(row=2, column=0, columnspan=4, pady=10)
        
        # Frame pour les résultats
        frame_resultats = ttk.LabelFrame(parent, text="Résultats")
        frame_resultats.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        # Treeview pour afficher les résultats
        columns = ("matricule", "nom", "prenom", "niveau", "departement")
        self.tree_recherche = ttk.Treeview(frame_resultats, columns=columns, show="headings")
        
        for col in columns:
            self.tree_recherche.heading(col, text=col.capitalize())
            self.tree_recherche.column(col, width=100)
        
        self.tree_recherche.pack(fill=tk.BOTH, expand=True)
        
        # Barre de défilement
        scrollbar = ttk.Scrollbar(frame_resultats, orient=tk.VERTICAL, command=self.tree_recherche.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree_recherche.configure(yscrollcommand=scrollbar.set)
        
        # Frame pour les notes de l'étudiant sélectionné
        frame_notes = ttk.LabelFrame(parent, text="Notes de l'étudiant")
        frame_notes.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        # Treeview pour afficher les notes
        columns = ("matiere", "controle", "tp", "examen", "moyenne")
        self.tree_notes_etudiant = ttk.Treeview(frame_notes, columns=columns, show="headings")
        
        for col in columns:
            self.tree_notes_etudiant.heading(col, text=col.capitalize())
            self.tree_notes_etudiant.column(col, width=100)
        
        self.tree_notes_etudiant.pack(fill=tk.BOTH, expand=True)
        
        # Barre de défilement
        scrollbar_notes = ttk.Scrollbar(frame_notes, orient=tk.VERTICAL, command=self.tree_notes_etudiant.yview)
        scrollbar_notes.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree_notes_etudiant.configure(yscrollcommand=scrollbar_notes.set)
        
        # Lier la sélection dans la treeview de recherche
        self.tree_recherche.bind("<<TreeviewSelect>>", self.afficher_notes_etudiant)
    
    def rechercher_etudiants(self):
        critere = self.recherche_var.get()
        valeur = self.entry_recherche.get()
        
        if not valeur:
            messagebox.showerror("Erreur", "Veuillez entrer une valeur de recherche")
            return
        
        etudiants = self.gestion_notes.rechercher_etudiant(critere, valeur)
        
        # Vider la Treeview
        for item in self.tree_recherche.get_children():
            self.tree_recherche.delete(item)
        
        # Ajouter les résultats
        for etudiant in etudiants:
            self.tree_recherche.insert("", tk.END, values=(
                etudiant.matricule,
                etudiant.nom,
                etudiant.prenom,
                etudiant.niveau,
                etudiant.departement
            ))
    
    def afficher_notes_etudiant(self, event):
        # Vider la Treeview des notes
        for item in self.tree_notes_etudiant.get_children():
            self.tree_notes_etudiant.delete(item)
        
        # Récupérer l'étudiant sélectionné
        selection = self.tree_recherche.selection()
        if not selection:
            return
        
        item = self.tree_recherche.item(selection[0])
        matricule = item['values'][0]
        
        # Trouver l'étudiant
        etudiant = next(e for e in self.gestion_notes.etudiants if e.matricule == matricule)
        
        # Récupérer les notes de l'étudiant
        notes = self.gestion_notes.obtenir_notes_etudiant(etudiant)
        
        # Ajouter les notes à la Treeview
        for note in notes:
            moyenne = note.calculer_moyenne()
            moyenne_str = f"{moyenne:.2f}" if moyenne is not None else "N/A"
            
            self.tree_notes_etudiant.insert("", tk.END, values=(
                note.matiere.nom,
                note.controle if note.controle is not None else "N/A",
                note.tp if note.tp is not None else "N/A",
                note.examen if note.examen is not None else "N/A",
                moyenne_str
            ))
    
    def creer_interface_statistiques(self, parent):
        # Frame pour les critères
        frame_criteres = ttk.LabelFrame(parent, text="Critères statistiques")
        frame_criteres.pack(padx=10, pady=5, fill=tk.X)
        
        # Département
        ttk.Label(frame_criteres, text="Département:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_departement = ttk.Combobox(frame_criteres, state="readonly")
        self.combo_departement.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        
        # Niveau
        ttk.Label(frame_criteres, text="Niveau:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_niveau = ttk.Combobox(frame_criteres, state="readonly")
        self.combo_niveau.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
        
        # Matière
        ttk.Label(frame_criteres, text="Matière:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_matiere_stats = ttk.Combobox(frame_criteres, state="readonly")
        self.combo_matiere_stats.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)
        
        # Bouton pour générer les statistiques
        btn_generer = ttk.Button(frame_criteres, text="Générer Statistiques", command=self.generer_statistiques)
        btn_generer.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Actualiser les combobox
        self.actualiser_combos_statistiques()
        
        # Frame pour les résultats
        frame_resultats = ttk.LabelFrame(parent, text="Statistiques")
        frame_resultats.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        # Treeview pour afficher les statistiques
        columns = ("matricule", "nom", "prenom", "matiere", "moyenne", "moyenne_generale")
        self.tree_stats = ttk.Treeview(frame_resultats, columns=columns, show="headings")
        
        for col in columns:
            self.tree_stats.heading(col, text=col.capitalize().replace("_", " "))
            self.tree_stats.column(col, width=100)
        
        self.tree_stats.pack(fill=tk.BOTH, expand=True)
        
        # Barre de défilement
        scrollbar = ttk.Scrollbar(frame_resultats, orient=tk.VERTICAL, command=self.tree_stats.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree_stats.configure(yscrollcommand=scrollbar.set)
    
    def actualiser_combos_statistiques(self):
        # Départements uniques
        departements = list(set(e.departement for e in self.gestion_notes.etudiants))
        self.combo_departement['values'] = departements
        if departements:
            self.combo_departement.current(0)
        
        # Niveaux uniques
        niveaux = list(set(e.niveau for e in self.gestion_notes.etudiants))
        self.combo_niveau['values'] = niveaux
        if niveaux:
            self.combo_niveau.current(0)
        
        # Matières
        matieres = [f"{m.code} - {m.nom}" for m in self.gestion_notes.matieres]
        self.combo_matiere_stats['values'] = matieres
        if matieres:
            self.combo_matiere_stats.current(0)
    
    def generer_statistiques(self):
        # Récupérer les critères
        departement = self.combo_departement.get()
        niveau = self.combo_niveau.get()
        matiere_str = self.combo_matiere_stats.get()
        
        # Convertir la matière sélectionnée en objet Matiere
        matiere = None
        if matiere_str:
            code_matiere = matiere_str.split(" - ")[0]
            matiere = next(m for m in self.gestion_notes.matieres if m.code == code_matiere)
        
        # Calculer les moyennes
        moyennes = self.gestion_notes.calculer_moyennes_groupe(
            departement if departement else None,
            niveau if niveau else None,
            matiere if matiere else None
        )
        
        # Vider la Treeview
        for item in self.tree_stats.get_children():
            self.tree_stats.delete(item)
        
        # Ajouter les résultats
        for etud_data in moyennes.values():
            etudiant = etud_data['etudiant']
            moyenne_generale = etud_data['moyenne_generale']
            moyenne_generale_str = f"{moyenne_generale:.2f}" if moyenne_generale is not None else "N/A"
            
            if etud_data['matieres']:
                for matiere_data in etud_data['matieres'].values():
                    self.tree_stats.insert("", tk.END, values=(
                        etudiant.matricule,
                        etudiant.nom,
                        etudiant.prenom,
                        matiere_data['matiere'].nom,
                        f"{matiere_data['moyenne']:.2f}",
                        moyenne_generale_str
                    ))
            else:
                self.tree_stats.insert("", tk.END, values=(
                    etudiant.matricule,
                    etudiant.nom,
                    etudiant.prenom,
                    "N/A",
                    "N/A",
                    moyenne_generale_str
                ))

if __name__ == "__main__":
    app = Application()
    app.mainloop()