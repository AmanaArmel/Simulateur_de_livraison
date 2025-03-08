import queue
from fichier_commande import Commande
class GestionCommandes:
    def __init__(self,reseau):
        self.file_commandes = queue.Queue()
        self.reseau = reseau  # Référence au réseau routier
        # Queue() est une mÃ©thode qui permet de crÃ©er une file

    def ajouter_commande(self, id_commande, adresse):
        """Ajoute une commande uniquement si l'adresse existe dans le réseau routier."""
        if adresse in self.reseau.graphe.nodes:
            commande = Commande(id_commande, adresse)
            self.file_commandes.put(commande)
            print(f"✅ Commande ajoutée : {commande}")
        else:
            print(f"❌ Adresse invalide : {adresse} n'existe pas dans le réseau routier.")

    def recuperer_commande(self):
        if not self.file_commandes.empty():
            return self.file_commandes.get()
            # get() RÃ©cupÃ¨re la premiÃ¨re commande en attente."""
        else:
            print("âŒ Aucune commande en attente.")
            return None

    def afficher_commandes(self):
        """Affiche toutes les commandes en attente."""
        print("\nðŸ“‹ Commandes en attente :")
        if self.file_commandes.empty():
            print("ðŸ“­ Aucune commande en attente.")
        else:
            for cmd in list(self.file_commandes.queue):
                 print(cmd)
        # self.file_commandes.queue permet d'accÃ©der directement Ã  la liste interne contenant les Ã©lÃ©ments stockÃ©s dans la file.

    def get_liste_commandes(self):
        """Retourne la liste des commandes en attente sous forme de liste."""
        return list(self.file_commandes.queue)  # 🔥 Ajout de cette méthode

    def annuler_commande(self, id_commande):
        """Annule une commande avant qu'elle ne soit prise par un livreur."""
        commandes_temp = []
        commande_annulee = None

        while not self.file_commandes.empty():
            commande = self.file_commandes.get()
            if commande.id_commande == id_commande:
                commande_annulee = commande
            else:
                commandes_temp.append(commande)

        # Remettre les commandes restantes dans la file
        for cmd in commandes_temp:
            self.file_commandes.put(cmd)

        if commande_annulee:
            print(f"❌ Commande {id_commande} annulée avec succès.")
            return True
        else:
            print(f"⚠ Commande {id_commande} introuvable ou déjà traitée.")
        return False