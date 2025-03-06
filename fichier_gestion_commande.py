import queue
from fichier_commande import Commande
class GestionCommandes:
    def __init__(self):
        self.file_commandes = queue.Queue()
        # Queue() est une mÃ©thode qui permet de crÃ©er une file
        
    def ajouter_commande(self, id_commande, adresse):
        commande = Commande(id_commande, adresse)
        self.file_commandes.put(commande)
        # put() permet d'ajouter une commande dans la file dâ€™attente.
        print(f"âœ… Commande ajoutÃ©e : {commande}")

    def recuperer_commande(self):
        if not self.file_commandes.empty():
            return self.file_commandes.get()
            # get() RÃ©cupÃ¨re la premiÃ¨re commande en attente."""
        else:
            print("âŒ Aucune commande en attente.")
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
           
                  