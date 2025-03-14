import time

from fichier_livreur import Livreur
import threading

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

    def get_livreurs_disponibles(self):
        """Retourne une liste des livreurs actuellement disponibles."""
        return [livreur for livreur in self.livreurs if livreur.statut == "Disponible"]

    def attribuer_commande(self, gestion_commandes, lieu_depart="Entrepot"):
        """Assigne les commandes aux livreurs en alternant."""
        while not gestion_commandes.file_commandes.empty():
            # Sélectionner un livreur en alternance

            livreursDisponibles = self.get_livreurs_disponibles()

            if not livreursDisponibles:
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
                        

                        # Démarrer un thread pour simuler le temps de livraison
                        thread = threading.Thread(target=self.simuler_livraison,
                                                  args=(livreur_disponible, distance, commande))
                        thread.start()
            else:
                print(f"🚫 Livreur {livreur_disponible.id_livreur} est occupé. On passe au suivant.")

    def simuler_livraison(self, livreur, distance, commande):
        """Simule la durée de la livraison avec un timer basé sur la distance."""
        print(f"⏳ Livraison en cours par le livreur {livreur.id_livreur}... (Durée estimée : {distance} secondes)")
        #time.sleep(distance)  # Attendre en arrière-plan sans bloquer l'exécution principale

        for i in range(1, distance + 1):
            time.sleep(1)  # Simuler la progression
            livreur.distance_parcourue = i  # Mise à jour de la distance parcourue

        livreur.livrer_commande()
        print(f"✅ Livreur {livreur.id_livreur} est maintenant disponible.")
