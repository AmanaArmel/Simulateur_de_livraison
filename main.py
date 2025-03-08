from fichier_commande import Commande
from fichier_livreur import Livreur
from fichier_ReseauRoutier import ReseauRoutier
from fichier_gestion_commande import GestionCommandes
from fichier_gestion_livreur import GestionLivreurs
import tkinter as tk

from interface import InterfaceApplication

# Initialisation
reseau = ReseauRoutier()
#gestion_commandes = GestionCommandes()
# 📌 Initialisation de la gestion des commandes avec le réseau routier
gestion_commandes = GestionCommandes(reseau)
gestion_livreurs = GestionLivreurs(reseau)

# Ajout des lieux et routes
reseau.ajouter_lieu("Entrepot")
reseau.ajouter_lieu("A")
reseau.ajouter_lieu("B")
reseau.ajouter_lieu("C")
reseau.ajouter_route("Entrepot", "A", 5)
reseau.ajouter_route("A", "B", 3)
reseau.ajouter_route("B", "C", 4)
reseau.ajouter_route("Entrepot", "C", 7)

# Ajout des livreurs et commandes
gestion_livreurs.ajouter_livreur(1)
gestion_livreurs.ajouter_livreur(2)
gestion_commandes.ajouter_commande(1, "A")
gestion_commandes.ajouter_commande(2, "C")

# Attribution et animation des trajets
#gestion_livreurs.attribuer_commande(gestion_commandes)
#gestion_livreurs.attribuer_commande(gestion_commandes)


# 📌 Lancement de l'interface Tkinter
root = tk.Tk()
app = InterfaceApplication(root, gestion_commandes,gestion_livreurs, reseau)
root.mainloop()