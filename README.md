Executer le fichier main pour afficher l'interface Graphique.

Résumé du projet 

Le projet "Simulateur de Livraison" consiste à simuler un processus logistique complet de livraison de commandes en utilisant un réseau routier modélisé sous forme de graphe. L’objectif principal est de gérer les commandes, optimiser les trajets des livreurs, et afficher les livraisons en temps réel avec des visualisations dynamiques. Le simulateur inclut également un système de gestion des livreurs, qui suivent un itinéraire optimisé pour chaque commande. 

Les principales fonctionnalités du projet sont : 

Gestion des commandes : Permet d'ajouter, stocker et récupérer des commandes via une file d'attente FIFO. 

Optimisation des trajets : Utilisation de l'algorithme de Dijkstra pour calculer le chemin le plus court entre les lieux de livraison. 

Suivi des livreurs : Gestion des livreurs, suivi de leur position en temps réel, et mise à jour des livraisons en cours. 

Le simulateur permet de visualiser l’ensemble des livraisons à travers une interface graphique, tout en modélisant les routes, lieux et livraisons en temps réel. 

Fonctionnalités principales 

Gestion des commandes 

Ajout de commandes : Chaque commande est ajoutée avec un identifiant unique et une adresse de livraison. 

Stockage dans une file FIFO : Les commandes sont stockées dans une file d'attente, et la prochaine commande à traiter est toujours récupérée en suivant le principe FIFO. 

Affichage des commandes en attente : Il est possible de visualiser les commandes qui sont en attente de livraison. 

 Modélisation du réseau routier 

Le réseau routier est modélisé sous forme de graphe pondéré, où chaque lieu est un nœud et chaque route entre les lieux est un arc avec un poids représentant la distance ou le temps de trajet. 

Algorithme de Dijkstra : Utilisation de l'algorithme de Dijkstra pour calculer le chemin le plus court entre deux lieux. 

Affichage graphique : Le réseau routier est représenté graphiquement, et les trajets des livreurs sont animés en temps réel. 
Gestion des livreurs 

Chaque livreur est un objet avec un nom, une position et une commande en cours. 

Attribution des commandes : Une fois une commande récupérée, elle est automatiquement attribuée à un livreur disponible. 

Suivi de la position du livreur : La position du livreur est mise à jour en fonction du chemin qu’il prend. 

Mise à jour des livraisons : L'état des livraisons est mis à jour en fonction de l'avancement du livreur. 
Installation & Exécution 

Prérequis 

Avant de pouvoir exécuter la simulation, vous devez installer certaines bibliothèques Python nécessaires. 

Exécutez la commande suivante pour installer les dépendances : 

pip install networkx matplotlib 

Lancer la simulation 

Une fois les dépendances installées, vous pouvez exécuter le simulateur en utilisant la commande suivante dans un terminal : 

Python nom_du_fichier.py 

Cela démarrera la simulation, où le réseau routier sera créé, les commandes ajoutées, et les livreurs commenceront leurs livraisons. 

 

Exemple rapide d'utilisation 

Création du réseau routier : Vous définissez un ensemble de lieux et de routes entre eux. Le réseau est modélisé à l'aide d'un graphe pondéré. 

Ajout de commandes : Les commandes sont ajoutées à la file d'attente, et chaque commande est associée à une adresse de livraison. 

Attribution des commandes : Les commandes sont automatiquement attribuées aux livreurs disponibles. Le livreur prendra la prochaine commande de la file d'attente. 

Calcul des itinéraires optimisés : L'algorithme de Dijkstra est utilisé pour trouver le chemin le plus court entre le lieu de départ du livreur et la destination. 

Suivi des livraisons : La position du livreur est mise à jour en temps réel et le déplacement est animé sur la carte. 


Structure du projet 

Classes principales 

Commande : Représente une commande avec un identifiant, une adresse de livraison et un statut (en cours, livrée, etc.). 

GestionCommandes : Gère la file d'attente des commandes, permet d'ajouter des commandes, de récupérer la commande suivante, et d'afficher les commandes en attente. 

Livreur : Représente un livreur avec son nom, sa position actuelle et la commande qu'il est en train de livrer. 

ReseauRoutier : Modélise le réseau routier sous forme de graphe pondéré. Cette classe est responsable de la création du réseau, de l'ajout de routes et de lieux, ainsi que du calcul des itinéraires optimaux. 

GestionLivreurs : Gère l'attribution des commandes aux livreurs et le suivi de leur état. 

InterfaceApplication : Implémente une interface graphique pour afficher les informations relatives au réseau routier, aux livreurs, et à l'animation des livraisons. 


Le simulateur de livraison propose une modélisation complète du processus logistique, allant de la gestion des commandes à l'optimisation des trajets des livreurs, tout en fournissant une visualisation dynamique du réseau routier. Ce projet permet de comprendre et d'appliquer des concepts d'algorithmique, tels que les files d'attente et les graphes pondérés, tout en intégrant une interface graphique pour faciliter l'interaction avec le système. 
