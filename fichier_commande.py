import queue # module intÃ©grÃ© qui implÃ©mente plusieurs types de files
class Commande:
    def __init__(self, id_commande, adresse):
        self.id_commande = id_commande
        self.adresse = adresse
        self.statut = "En attente"

    def __str__(self): # sert Ã  afficher un objet sous forme lisible.
        return f"Commande {self.id_commande} - {self.adresse} [{self.statut}]"
