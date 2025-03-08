from fichier_livreur import Livreur
class GestionLivreurs:
    def __init__(self, reseau_routier):
        """Initialise la gestion des livreurs avec accÃ¨s au rÃ©seau routier."""
        self.livreurs = []
        self.reseau_routier = reseau_routier
        self.index_livreur = 0

    def ajouter_livreur(self, id_livreur):
        """Ajoute un livreur Ã  la liste."""
        livreur = Livreur(id_livreur)
        self.livreurs.append(livreur)
        print(f"ðŸ§‘â€âœˆï¸ Livreur ajoutÃ© : {livreur}")

    # def attribuer_commande(self, gestion_commandes, lieu_depart="Entrepot"):
    #     """Affecte une commande disponible Ã  un livreur libre et anime le trajet."""
    #     livreur_disponible = next((livreur for livreur in self.livreurs if livreur.statut == "Disponible"), None)
    #     if livreur_disponible:
    #         commande = gestion_commandes.recuperer_commande()
    #         if commande:
    #             # Trouver l'itinÃ©raire optimal
    #             chemin, distance = self.reseau_routier.trouver_chemin_optimal(lieu_depart, commande.adresse)
    #             if chemin:
    #                 livreur_disponible.prendre_commande(commande)
    #                 print(f"ðŸ—ºï¸ ItinÃ©raire du livreur {livreur_disponible.id_livreur} : {' â†’ '.join(chemin)} (Distance : {distance} km)")
    #     else:
    #         print("ðŸš« Aucun livreur disponible.")

    def attribuer_commande(self, gestion_commandes, lieu_depart="Entrepot"):
        """Assigne les commandes aux livreurs en alternant."""
        while not gestion_commandes.file_commandes.empty():
            # Sélectionner un livreur en alternance
            if len(self.livreurs) == 0:
                print("❌ Aucun livreur disponible.")
                return

            livreur_disponible = self.livreurs[self.index_livreur % len(self.livreurs)]
            self.index_livreur += 1  # Passer au livreur suivant pour la prochaine commande

            if livreur_disponible.statut == "Disponible":
                commande = gestion_commandes.recuperer_commande()
                if commande:
                    chemin, distance = self.reseau_routier.trouver_chemin_optimal(lieu_depart, commande.adresse)
                    if chemin:
                        livreur_disponible.prendre_commande(commande)
                        print(
                            f"🗺 Itinéraire du livreur {livreur_disponible.id_livreur} : {' → '.join(chemin)} (Distance : {distance} km)")
                        #self.reseau_routier.animer_deplacement(chemin)

                        # Livraison terminée, le livreur redevient disponible
                        #livreur_disponible.livrer_commande()
            else:
                print(f"🚫 Livreur {livreur_disponible.id_livreur} est occupé. On passe au suivant.")
