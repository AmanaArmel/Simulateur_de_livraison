from fichier_livreur import Livreur
class GestionLivreurs:
    def __init__(self, reseau_routier):
        """Initialise la gestion des livreurs avec accÃ¨s au rÃ©seau routier."""
        self.livreurs = []
        self.reseau_routier = reseau_routier

    def ajouter_livreur(self, id_livreur):
        """Ajoute un livreur Ã  la liste."""
        livreur = Livreur(id_livreur)
        self.livreurs.append(livreur)
        print(f"ðŸ§‘â€âœˆï¸ Livreur ajoutÃ© : {livreur}")

    def attribuer_commande(self, gestion_commandes, lieu_depart="EntrepÃ´t"):
        """Affecte une commande disponible Ã  un livreur libre et anime le trajet."""
        livreur_disponible = next((livreur for livreur in self.livreurs if livreur.statut == "Disponible"), None)
        if livreur_disponible:
            commande = gestion_commandes.recuperer_commande()
            if commande:
                # Trouver l'itinÃ©raire optimal
                chemin, distance = self.reseau_routier.trouver_chemin_optimal(lieu_depart, commande.adresse)
                if chemin:
                    livreur_disponible.prendre_commande(commande)
                    print(f"ðŸ—ºï¸ ItinÃ©raire du livreur {livreur_disponible.id_livreur} : {' â†’ '.join(chemin)} (Distance : {distance} km)")
                    self.reseau_routier.animer_deplacement(chemin)  # Animation du trajet
        else:
            print("ðŸš« Aucun livreur disponible.")
