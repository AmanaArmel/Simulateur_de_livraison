from fichier_commande import Commande
class Livreur:
    def __init__(self, id_livreur):
        self.id_livreur = id_livreur
        self.statut = "Disponible"
        self.commande_actuelle = None
        self.distance_parcourue = 0  # Distance initiale


    def __str__(self):
        return f"Livreur {self.id_livreur} - {self.statut}"

    def prendre_commande(self, commande):
        """Attribue une commande au livreur et met Ã  jour son statut."""
        self.commande_actuelle = commande
        commande.statut = "En livraison"
        self.distance_parcourue = 0  # Réinitialiser la distance
        self.statut = "En livraison"
        print(f"ðŸšš Livreur {self.id_livreur} prend la {commande}")

    def livrer_commande(self):
        """Marque la commande comme livrÃ©e et libÃ¨re le livreur."""
        if self.commande_actuelle:
            self.commande_actuelle.statut = "LivrÃ©e"
            print(f"âœ… {self.commande_actuelle} a Ã©tÃ© livrÃ©e par le livreur {self.id_livreur}")
            self.commande_actuelle = None
            self.statut = "Disponible"
            self.distance_parcourue = 0  # Réinitialiser la distance après livraison
