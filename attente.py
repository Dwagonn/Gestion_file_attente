# Variables globales :
nb_clients = 100000 # nb clients de l'échantillon
nb_guichets = 5 # nb guichets
tick = 0 # horloge
dispo_guichets = [0] * nb_guichets # Tableau de disponibilité des guichets
file_unique = File() # file créée avec 2 piles, contenant l'heure d'arrivée des chaque client
file_guichet = [File()] * nb_guichets # une file par guichet
temps_total = 0 # temps d'attente global
clients_servis = 0 # nb clients servis

# Gestion d'une pile avec une liste chaînée :
class Cellule:
    """ Une cellule d'une liste chaînée """
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s

class Pile:
    """ Structure de pile """

    def __init__(self):
        self.contenu = None

    def est_vide(self):
        return self.contenu is None

    def empiler(self, v):
        self.contenu = Cellule(v, self.contenu)

    def depiler(self):
        if self.est_vide():
            raise IndexError("depiler sur une pile vide")
        v = self.contenu.valeur
        self.contenu = self.contenu.suivante
        return v

def creer_pile():
    """ Création d'une pile avec liste chaînée """
    return Pile()
# Gestion d'une file avec deux piles :

class File:
    """ Structure de file constituée de deux piles"""

    def __init__(self):
        self.entree = creer_pile()
        self.sortie = creer_pile()

    def est_vide(self):
        return self.entree.est_vide() \
            and self.sortie.est_vide()

    def ajouter(self, x):
        self.entree.empiler(x)

    def retirer(self):
        if self.sortie.est_vide():
            while not self.entree.est_vide():
                self.sortie.empiler(self.entree.depiler())
        if self.sortie.est_vide():
            raise IndexError("retirer sur une file vide")
        return self.sortie.depiler()