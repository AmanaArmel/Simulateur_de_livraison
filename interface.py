import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class InterfaceApplication:
    def __init__(self, root, gestion_commandes, gestion_livreurs, reseau_routier):
        self.root = root
        self.root.title("Gestion des Commandes et du Réseau Routier")

        self.gestion_commandes = gestion_commandes
        self.gestion_livreurs = gestion_livreurs
        self.reseau_routier = reseau_routier

        # Création des onglets
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')

        # Onglet Commandes
        self.frame_commandes = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_commandes, text="Commandes")

        # Utilisation d'une grille pour la disposition en colonnes
        self.frame_form = ttk.Frame(self.frame_commandes)
        self.frame_form.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        self.frame_list = ttk.Frame(self.frame_commandes)
        self.frame_list.grid(row=0, column=1, padx=20, pady=20, sticky="n")

        # Formulaire de création de commande
        self.label_commande = ttk.Label(self.frame_form, text="Nouvelle Commande", font=("Arial", 14, "bold"))
        self.label_commande.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")

        self.label_id_commande = ttk.Label(self.frame_form, text="Id", font=("Arial", 12))
        self.label_id_commande.grid(row=1, column=0, pady=5, sticky="w")
        self.entry_id_commande = ttk.Entry(self.frame_form, font=("Arial", 12))
        self.entry_id_commande.grid(row=1, column=1, pady=5, ipadx=10, ipady=5, sticky="w")

        self.label_adresse = ttk.Label(self.frame_form, text="Adresse", font=("Arial", 12))
        self.label_adresse.grid(row=2, column=0, pady=5, sticky="w")
        self.entry_adresse = ttk.Entry(self.frame_form, font=("Arial", 12))
        self.entry_adresse.grid(row=2, column=1, pady=5, ipadx=10, ipady=5, sticky="w")

        self.bouton_ajouter_commande = ttk.Button(self.frame_form, text="Ajouter Commande",
                                                  command=self.ajouter_commande)
        self.bouton_ajouter_commande.grid(row=3, column=0, columnspan=2, pady=10, sticky="w")

        # Liste des commandes
        # self.label_liste_commandes = ttk.Label(self.frame_list, text="Liste des Commandes", font=("Arial", 14, "bold"))
        # self.label_liste_commandes.pack(pady=5)
        #
        # self.liste_commandes = tk.Listbox(self.frame_list, font=("Arial", 12), height=10, width=40)
        # self.liste_commandes.pack()

        # Liste des commandes
        self.label_liste_commandes = ttk.Label(self.frame_list, text="Liste des Commandes", font=("Arial", 14, "bold"))
        self.label_liste_commandes.pack(pady=5)

        self.frame_table = ttk.Frame(self.frame_list)
        self.frame_table.pack()

        self.table_commandes = ttk.Treeview(self.frame_table, columns=("ID", "Adresse"), show="headings")
        self.table_commandes.heading("ID", text="ID")
        self.table_commandes.heading("Adresse", text="Adresse")
        self.table_commandes.column("ID", width=100, anchor="center")
        self.table_commandes.column("Adresse", width=200, anchor="w")
        self.table_commandes.pack()

        # Onglet Livreurs
        # self.frame_livreurs = ttk.Frame(self.notebook)
        # self.notebook.add(self.frame_livreurs, text="Livreurs")
        #
        # self.label_livreurs = tk.Label(self.frame_livreurs, text="Liste des Livreurs")
        # self.label_livreurs.pack()
        #
        # self.entry_id_livreur = tk.Entry(self.frame_livreurs)
        # self.entry_id_livreur.pack()
        #
        # self.bouton_ajouter_livreur = tk.Button(self.frame_livreurs, text="Ajouter Livreur",
        #                                         command=self.ajouter_livreur)
        # self.bouton_ajouter_livreur.pack()
        #
        # self.liste_livreurs = tk.Listbox(self.frame_livreurs)
        # self.liste_livreurs.pack()
        #
        # self.bouton_attribuer = tk.Button(self.frame_livreurs, text="Attribuer Commande",
        #                                   command=self.attribuer_commande)
        # self.bouton_attribuer.pack()

        # Onglet Livreurs
        self.frame_livreurs = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_livreurs, text="Livreurs")

        self.frame_form_livreur = ttk.Frame(self.frame_livreurs)
        self.frame_form_livreur.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        self.frame_list_livreur = ttk.Frame(self.frame_livreurs)
        self.frame_list_livreur.grid(row=0, column=1, padx=20, pady=20, sticky="n")

        # Formulaire d'ajout de livreur
        self.label_livreur = ttk.Label(self.frame_form_livreur, text="Nouveau Livreur", font=("Arial", 14, "bold"))
        self.label_livreur.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")

        self.label_id_livreur = ttk.Label(self.frame_form_livreur, text="Id", font=("Arial", 12))
        self.label_id_livreur.grid(row=1, column=0, pady=5, sticky="w")
        self.entry_id_livreur = ttk.Entry(self.frame_form_livreur, font=("Arial", 12))
        self.entry_id_livreur.grid(row=1, column=1, pady=5, ipadx=10, ipady=5, sticky="w")

        self.bouton_ajouter_livreur = ttk.Button(self.frame_form_livreur, text="Ajouter Livreur",command=self.ajouter_livreur)
        self.bouton_ajouter_livreur.grid(row=2, column=0, columnspan=2, pady=10, sticky="w")

        # Liste des livreurs
        self.label_liste_livreurs = ttk.Label(self.frame_list_livreur, text="Liste des Livreurs",
                                              font=("Arial", 14, "bold"))
        self.label_liste_livreurs.pack(pady=5)

        self.frame_table_livreur = ttk.Frame(self.frame_list_livreur)
        self.frame_table_livreur.pack()

        self.table_livreurs = ttk.Treeview(self.frame_table_livreur, columns=("ID", "Statut"), show="headings")
        self.table_livreurs.heading("ID", text="ID")
        self.table_livreurs.heading("Statut", text="Statut")
        self.table_livreurs.column("ID", width=100, anchor="center")
        self.table_livreurs.column("Statut", width=200, anchor="w")
        self.table_livreurs.pack()

        self.bouton_attribuer_commande = ttk.Button(self.frame_list_livreur, text="Attribuer Commande",command=self.attribuer_commande)
        self.bouton_attribuer_commande.pack(pady=10)

        # Onglet Réseau Routier
        self.frame_reseau = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_reseau, text="Réseau Routier")

        self.frame_form_reseau = ttk.Frame(self.frame_reseau)
        self.frame_form_reseau.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        self.frame_graph_reseau = ttk.Frame(self.frame_reseau)
        self.frame_graph_reseau.grid(row=0, column=1, padx=20, pady=20, sticky="n")

        # Formulaire de gestion du réseau routier
        self.label_reseau = ttk.Label(self.frame_form_reseau, text="Gestion du Réseau Routier",
                                      font=("Arial", 14, "bold"))
        self.label_reseau.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")

        self.label_lieu = ttk.Label(self.frame_form_reseau, text="Ajouter un Lieu", font=("Arial", 12))
        self.label_lieu.grid(row=1, column=0, pady=5, sticky="w")
        self.entry_lieu = ttk.Entry(self.frame_form_reseau, font=("Arial", 12))
        self.entry_lieu.grid(row=1, column=1, pady=5, ipadx=10, ipady=5, sticky="w")
        self.bouton_ajouter_lieu = ttk.Button(self.frame_form_reseau, text="Ajouter Lieu", command=self.ajouter_lieu)
        self.bouton_ajouter_lieu.grid(row=2, column=0, columnspan=2, pady=10, sticky="w")

        self.label_route = ttk.Label(self.frame_form_reseau, text="Ajouter une Route", font=("Arial", 12))
        self.label_route.grid(row=3, column=0, columnspan=2, pady=5, sticky="w")

        self.label_route1 = ttk.Label(self.frame_form_reseau, text="Lieu 1", font=("Arial", 12))
        self.label_route1.grid(row=4, column=0, pady=5, sticky="w")
        self.entry_route1 = ttk.Entry(self.frame_form_reseau, font=("Arial", 12))
        self.entry_route1.grid(row=4, column=1, pady=5, ipadx=10, ipady=5, sticky="w")

        self.label_route2 = ttk.Label(self.frame_form_reseau, text="Lieu 2", font=("Arial", 12))
        self.label_route2.grid(row=5, column=0, pady=5, sticky="w")
        self.entry_route2 = ttk.Entry(self.frame_form_reseau, font=("Arial", 12))
        self.entry_route2.grid(row=5, column=1, pady=5, ipadx=10, ipady=5, sticky="w")

        self.label_distance = ttk.Label(self.frame_form_reseau, text="Distance", font=("Arial", 12))
        self.label_distance.grid(row=6, column=0, pady=5, sticky="w")
        self.entry_distance = ttk.Entry(self.frame_form_reseau, font=("Arial", 12))
        self.entry_distance.grid(row=6, column=1, pady=5, ipadx=10, ipady=5, sticky="w")

        self.bouton_ajouter_route = ttk.Button(self.frame_form_reseau, text="Ajouter Route", command=self.ajouter_route)
        self.bouton_ajouter_route.grid(row=7, column=0, columnspan=2, pady=10, sticky="w")

        # Zone d'affichage du graphe
        self.canvas_frame = ttk.Frame(self.frame_graph_reseau)
        self.canvas_frame.pack()

        self.mise_a_jour_affichage()

    def ajouter_commande(self):
        id_commande = self.entry_id_commande.get()
        adresse = self.entry_adresse.get()
        if adresse in self.reseau_routier.graphe.nodes:
            self.gestion_commandes.ajouter_commande(id_commande, adresse)
            self.mise_a_jour_affichage()
            # self.attribuer_commande()
            # self.mise_a_jour_affichage()
        else:
            print("Adresse non valide")

    def attribuer_commande(self):
        self.gestion_livreurs.attribuer_commande(self.gestion_commandes,)
        self.mise_a_jour_affichage()

    def ajouter_lieu(self):
        lieu = self.entry_lieu.get()
        self.reseau_routier.ajouter_lieu(lieu)
        self.mise_a_jour_affichage()

    def ajouter_route(self):
        lieu1 = self.entry_route1.get()
        lieu2 = self.entry_route2.get()
        distance = int(self.entry_distance.get())
        self.reseau_routier.ajouter_route(lieu1, lieu2, distance)
        self.mise_a_jour_affichage()

    def mise_a_jour_affichage(self):
        #self.liste_commandes.delete(0, tk.END)
        for row in self.table_commandes.get_children():
            self.table_commandes.delete(row)
        for cmd in list(self.gestion_commandes.file_commandes.queue):
            #self.liste_commandes.insert(tk.END, str(cmd))
            self.table_commandes.insert("", "end", values=(cmd.id_commande, cmd.adresse))

        #self.liste_livreurs.delete(0, tk.END)
        for row in self.table_livreurs.get_children():
            self.table_livreurs.delete(row)
        for livreur in self.gestion_livreurs.livreurs:
            if livreur.commande_actuelle:
                info = f"{livreur} - {livreur.commande_actuelle.id_commande} ({livreur.commande_actuelle.adresse})"
            else:
                info = str(livreur)
            #self.liste_livreurs.insert(tk.END, info)
            self.table_livreurs.insert("", "end", values=(livreur.id_livreur, livreur.statut))

        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(5, 4))
        pos = nx.spring_layout(self.reseau_routier.graphe)
        nx.draw(self.reseau_routier.graphe, pos, with_labels=True, node_color='skyblue', edge_color='gray', ax=ax)
        labels = nx.get_edge_attributes(self.reseau_routier.graphe, 'weight')
        nx.draw_networkx_edge_labels(self.reseau_routier.graphe, pos, edge_labels=labels, ax=ax)

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.get_tk_widget().pack()
        canvas.draw()

    def ajouter_livreur(self):
        id_livreur = self.entry_id_livreur.get()
        if id_livreur:
            self.gestion_livreurs.ajouter_livreur(id_livreur)
            self.mise_a_jour_affichage()

