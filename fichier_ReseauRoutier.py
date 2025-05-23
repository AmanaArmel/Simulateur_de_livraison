#pip install networkx

import networkx as nx
import matplotlib.pyplot as plt

class ReseauRoutier:
    def __init__(self):
        """Initialise un graphe pondéré pour représenter le réseau routier."""
        self.graphe = nx.Graph()

    def ajouter_lieu(self, nom):
        """Ajoute un point de livraison au graphe."""
        self.graphe.add_node(nom)
        print(f"📍 Lieu ajouté : {nom}")

    def ajouter_route(self, lieu1, lieu2, distance):
        """Ajoute une route entre deux lieux avec un poids (distance)."""
        if lieu1 in self.graphe.nodes and lieu2 in self.graphe.nodes:
            self.graphe.add_edge(lieu1, lieu2, weight=distance)
            print(f"🛣️ Route ajoutée : {lieu1} ↔ {lieu2} ({distance} km)")
        else:
            print(f"❌ Impossible d'ajouter la route : {lieu1} ou {lieu2} n'existe pas.")

    def trouver_chemin_optimal(self, depart, arrivee):
        """Trouve le chemin le plus court entre deux lieux avec Dijkstra."""
        if depart in self.graphe.nodes and arrivee in self.graphe.nodes:
            chemin = nx.shortest_path(self.graphe, source=depart, target=arrivee, weight="weight")
            distance = nx.shortest_path_length(self.graphe, source=depart, target=arrivee, weight="weight")
            print(f"🚀 Chemin optimal : {' → '.join(chemin)} (Distance : {distance} km)")
            return chemin, distance
        else:
            print(f"❌ Lieux invalides : {depart} ou {arrivee} n'existe pas.")
            return None, None

    def afficher_reseau(self):
        """Affiche le réseau routier avec Matplotlib."""
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(self.graphe)
        nx.draw(self.graphe, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_weight='bold', edge_color='gray')
        labels = nx.get_edge_attributes(self.graphe, 'weight')
        nx.draw_networkx_edge_labels(self.graphe, pos, edge_labels=labels, font_size=10, font_color='red')
        plt.title("📌 Réseau Routier des Livraisons")
        plt.show()

    
