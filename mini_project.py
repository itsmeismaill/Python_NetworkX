import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Initialiser la variable canvas à None
canvas = None

def charger_graphe():
    global canvas  # Ajouter la déclaration pour utiliser la variable globale canvas
    # Récupérer le contenu du champ de texte
    contenu = champ_texte.get("1.0", tk.END)

    # Écrire le contenu dans un fichier texte temporaire
    with open("temp.txt", "w") as fichier:
        fichier.write(contenu)

    # Charger le graphe à partir du fichier temporaire
    G = nx.read_edgelist("temp.txt", create_using=nx.DiGraph())

    #  Effacer le contenu du champ de texte
    # champ_texte.delete("1.0", tk.END)

    # Effacer le contenu du canvas s'il existe
    if canvas:
        canvas.get_tk_widget().destroy()

    # Dessiner le graphe dans le canvas
    fig = plt.figure()
    canvas = FigureCanvasTkAgg(fig, master=fenetre)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Dessiner le graphe
    nx.draw(G, with_labels=True, node_size=500, node_color="blue", ax=fig.gca())
    

def charger_graphe2():
    global canvas  # Ajouter la déclaration pour utiliser la variable globale canvas
    # Récupérer le contenu du champ de texte
    contenu = champ_texte.get("1.0", tk.END)

    # Écrire le contenu dans un fichier texte temporaire
    with open("temp.txt", "w") as fichier:
        fichier.write(contenu)

    # Charger le graphe à partir du fichier temporaire
    G = nx.read_edgelist("temp.txt", create_using=nx.Graph())

    # Effacer le contenu du champ de texte
    # champ_texte.delete("1.0", tk.END)

    # Effacer le contenu du canvas s'il existe
    if canvas:
        canvas.get_tk_widget().destroy()

    # Dessiner le graphe dans le canvas
    fig = plt.figure()
    canvas = FigureCanvasTkAgg(fig, master=fenetre)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Dessiner le graphe
    nx.draw(G, with_labels=True, node_size=500, node_color="blue", ax=fig.gca())
def charger_graphe3():
    global canvas  # Ajouter la déclaration pour utiliser la variable globale canvas
    # Récupérer le contenu du champ de texte
    contenu = champ_texte.get("1.0", tk.END)

    # Écrire le contenu dans un fichier texte temporaire
    with open("temp.txt", "w") as fichier:
        fichier.write(contenu)

    # Charger le graphe à partir du fichier temporaire
    G =  nx.read_edgelist("temp.txt",data=[('weight',int)],create_using=nx.DiGraph())
    pos=nx.spring_layout(G)

    # Effacer le contenu du champ de texte
    # champ_texte.delete("1.0", tk.END)

    # Effacer le contenu du canvas s'il existe
    if canvas:
        canvas.get_tk_widget().destroy()

    # Dessiner le graphe dans le canvas
    fig = plt.figure()
    canvas = FigureCanvasTkAgg(fig, master=fenetre)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Dessiner le graphe
    nx.draw(G,pos,with_labels=True,node_size=500,node_color="blue")
    nx.draw_networkx_edge_labels(G,pos,font_size=10, edge_labels=nx.get_edge_attributes(G,'weight'))
    
def charger_graphe4():
    global canvas  # Ajouter la déclaration pour utiliser la variable globale canvas
    # Récupérer le contenu du champ de texte
    contenu = champ_texte.get("1.0", tk.END)

    # Écrire le contenu dans un fichier texte temporaire
    with open("temp.txt", "w") as fichier:
        fichier.write(contenu)

    # Charger le graphe à partir du fichier temporaire
    G =  nx.read_edgelist("temp.txt",data=[('weight',int)],create_using=nx.Graph())
    pos=nx.spring_layout(G)

    # Effacer le contenu du champ de texte
    # champ_texte.delete("1.0", tk.END)

    # Effacer le contenu du canvas s'il existe
    if canvas:
        canvas.get_tk_widget().destroy()

    # Dessiner le graphe dans le canvas
    fig = plt.figure()
    canvas = FigureCanvasTkAgg(fig, master=fenetre)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Dessiner le graphe
    nx.draw(G,pos,with_labels=True,node_size=500,node_color="blue")
    nx.draw_networkx_edge_labels(G,pos,font_size=10, edge_labels=nx.get_edge_attributes(G,'weight'))

def passer_algo():
    fenetre.destroy()
    nv_fenetre = tk.Tk()
    nv_fenetre.title("Mon Application")
    nv_fenetre.mainloop()
    
    



# Créer la fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Mon Application")  # Ajouter un titre à la fenêtre

# Créer le champ de texte pour le contenu du fichier
champ_texte = tk.Text(fenetre, height=10, width=40)
champ_texte.pack()      

# Créer le bouton pour charger le graphe
bouton_charger = tk.Button(fenetre, text="Charger Digraph", command=charger_graphe)
bouton_charger.pack(pady=10)  # Ajouter un espacement vertical (padding) entre les éléments
# Créer le bouton pour charger le graphe
bouton_charger2 = tk.Button(fenetre, text="Charger Graph", command=charger_graphe2)
bouton_charger2.pack(pady=10)  # Ajouter un espacement vertical (padding) entre les éléments
# Créer le bouton pour charger le graphe
bouton_charger3 = tk.Button(fenetre, text="Charger Graph pondere oriente", command=charger_graphe3)
bouton_charger3.pack(pady=10)  # Ajouter un espacement vertical (padding) entre les éléments
# Créer le bouton pour charger le graphe
bouton_charger4 = tk.Button(fenetre, text="Charger Graph pondere non-oriente", command=charger_graphe4)
bouton_charger4.pack(pady=10)  # Ajouter un espacement vertical (padding) entre les éléments
# creer le bouton pour passer a la fenetre des algorithme
bouton_passer_algo = tk.Button( fenetre, text="Choisir algorithme" , command=passer_algo)
bouton_passer_algo.pack(pady=10)
# Créer le canvas

# Créer le canvas pour afficher le graphe
fig = plt.figure()
canvas = FigureCanvasTkAgg(fig, master=fenetre)
canvas.draw()
canvas.get_tk_widget().pack()

# Lancer la boucle d'événements Tkinter
fenetre.mainloop()

