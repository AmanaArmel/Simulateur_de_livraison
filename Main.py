from fichier_commande import Commande
from fichier_livreur import Livreur
from fichier_ReseauRoutier import ReseauRoutier
from fichier_gestion_commande import GestionCommandes
from fichier_gestion_livreur import GestionLivreurs

# Initialisation
reseau = ReseauRoutier()
gestion_commandes = GestionCommandes()
gestion_livreurs = GestionLivreurs(reseau)

# Ajout des lieux et routes
reseau.ajouter_lieu("EntrepÃ´t")
reseau.ajouter_lieu("Rue de Paris")
reseau.ajouter_lieu("Avenue des Champs")
reseau.ajouter_lieu("Place de la RÃ©publique")
reseau.ajouter_route("EntrepÃ´t", "Rue de Paris", 5)
reseau.ajouter_route("Rue de Paris", "Avenue des Champs", 3)
reseau.ajouter_route("Avenue des Champs", "Place de la RÃ©publique", 4)
reseau.ajouter_route("EntrepÃ´t", "Place de la RÃ©publique", 7)

# Ajout des livreurs et commandes
gestion_livreurs.ajouter_livreur(1)
gestion_livreurs.ajouter_livreur(2)
gestion_commandes.ajouter_commande(1, "Rue de Paris")
gestion_commandes.ajouter_commande(2, "Place de la RÃ©publique")

# Attribution et animation des trajets
gestion_livreurs.attribuer_commande(gestion_commandes)
gestion_livreurs.attribuer_commande(gestion_commandes)

