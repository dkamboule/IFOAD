class Matiere:
    def __init__(self, code, nom, coefficients):
        self.code = code
        self.nom = nom
        self.coefficients = coefficients  # {'controle': 0.3, 'tp': 0.2, 'examen': 0.5}