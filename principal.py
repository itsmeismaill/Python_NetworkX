import tkinter as tk
import collections
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from algorithmes import *
from pathlib import Path
from tkinter import Canvas , PhotoImage
from PIL import Image, ImageTk
from algorithmesSP import *
from algorithmesPO import *
from algorithmeO import *

def passer_algo():
    global num
    num=tk.IntVar() 
    def num1():
        num.set(1)
        return num
    def num2():
        num.set(2)
        return num
    def num3():
        num.set(3)
        return num
    def num4():
        num.set(4)
        return num
    # def voir():
    #     print(num.get())
    def votre_algo():
        nv_fenetre1.destroy()
        nv_fenetre = tk.Tk()
        nv_fenetre.title("Mon Application")
        nv_fenetre.geometry("400x300")  # Set the width to 400 pixels and height to 300 pixels
        if(num.get()==1):
            radiobutton1 = tk.Radiobutton(nv_fenetre, text="BFS",command=bfs, background = "light blue")
            radiobutton2 = tk.Radiobutton(nv_fenetre, text="DFS",command=dfs,background = "light blue")
            radiobutton5 = tk.Radiobutton(nv_fenetre, text="WARSHALL",command=warshall,background = "light blue")
            radiobutton1.pack(pady=8)
            radiobutton2.pack(pady=8)
            radiobutton5.pack(pady=8)
        elif(num.get()==2):
            radiobutton1 = tk.Radiobutton(nv_fenetre, text="BFS",command=bfs, background = "light blue")
            radiobutton2 = tk.Radiobutton(nv_fenetre, text="DFS",command=dfs,background = "light blue")
            radiobutton5 = tk.Radiobutton(nv_fenetre, text="WARSHALL",command=warshallO,background = "light blue")
            radiobutton1.pack(pady=8)
            radiobutton2.pack(pady=8)
            radiobutton5.pack(pady=8)            
        elif(num.get()==3):
            radiobutton1p = tk.Radiobutton(nv_fenetre, text="BFS",command=bfsP, background = "light blue")
            radiobutton2p = tk.Radiobutton(nv_fenetre, text="DFS",command=dfsP,background = "light blue")
            radiobutton4 = tk.Radiobutton(nv_fenetre, text="DIJKSTRA",background = "light blue")
            radiobutton5 = tk.Radiobutton(nv_fenetre, text="WARSHALL",command=warshallPO,background = "light blue")
            radiobutton6 = tk.Radiobutton(nv_fenetre, text="BELLMAN-FORD",background = "light blue")
            radiobutton7 = tk.Radiobutton(nv_fenetre, text="FORD-FORKENSON",background = "light blue")
            radiobutton1p.pack(pady=8)
            radiobutton2p.pack(pady=8)
            radiobutton4.pack(pady=8)
            radiobutton5.pack(pady=8)
            radiobutton6.pack(pady=8)
            radiobutton7.pack(pady=8)
        elif(num.get()==4):   
            radiobutton1p = tk.Radiobutton(nv_fenetre, text="BFS",command=bfsP, background = "light blue")
            radiobutton2p = tk.Radiobutton(nv_fenetre, text="DFS",command=dfsP,background = "light blue")
            radiobutton3 = tk.Radiobutton(nv_fenetre, text="KRUSKAL & PRIME",command=kruskal,background = "light blue")
            radiobutton4 = tk.Radiobutton(nv_fenetre, text="DIJKSTRA",background = "light blue")
            radiobutton5 = tk.Radiobutton(nv_fenetre, text="WARSHALL",command=warshallPNO,background = "light blue")
            radiobutton6 = tk.Radiobutton(nv_fenetre, text="BELLMAN-FORD",background = "light blue")
            radiobutton7 = tk.Radiobutton(nv_fenetre, text="FORD-FORKENSON",background = "light blue")
            radiobutton1p.pack(pady=8)
            radiobutton2p.pack(pady=8)
            radiobutton3.pack(pady=8)
            radiobutton4.pack(pady=8)
            radiobutton5.pack(pady=8)
            radiobutton6.pack(pady=8)
            radiobutton7.pack(pady=8)
        nv_fenetre.mainloop()
    
     
    global nv_fenetre1 
    nv_fenetre1 = tk.Tk()
    nv_fenetre1.title("Choisir votre algorithme")
    nv_fenetre1.geometry("400x300")  # Set the width to 400 pixels and height to 300 pixels

    label = tk.Label(nv_fenetre1, text="Type de graph:",font=("Arial", 20),background = "gold")
   

    
    Checkbutton1 = tk.Checkbutton(nv_fenetre1, text="Graph non oriente", background = "light blue" ,command=num1)
    Checkbutton2 = tk.Checkbutton(nv_fenetre1, text="Graph oriente",background = "light blue",command=num2 )
    Checkbutton3 = tk.Checkbutton(nv_fenetre1, text="Graph pondere oriente",background = "light blue",command=num3)
    Checkbutton4 = tk.Checkbutton(nv_fenetre1, text="Graph pondere non oriente",background = "light blue",command=num4)
    check_button = tk.Button(nv_fenetre1, text="Valider",command=votre_algo,background = "light blue")
    
    label.pack(pady=8)
    Checkbutton1.pack(pady=8)
    Checkbutton2.pack(pady=8)
    Checkbutton3.pack(pady=8)
    Checkbutton4.pack(pady=8)
    check_button.pack(pady=8)
    nv_fenetre1.mainloop()
    

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
    fig = plt.figure(figsize=(4, 4))
    canvas = FigureCanvasTkAgg(fig, master=fenetre)
    canvas.draw()
    canvas.get_tk_widget().place(x=400,y=100)

    # Dessiner le graphe
    nx.draw(G, with_labels=True, node_size=500, node_color="blue", ax=fig.gca())
    info_label = tk.Label(fenetre, text=f"Informations du graphe : \n Nombre de nœuds = {G.number_of_nodes()} \n Nombre d'arêtes = {G.number_of_edges()}",fg="blue")
    info_label.place(x=520, y=20)
    
    

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
    fig = plt.figure(figsize=(4, 4))
    canvas = FigureCanvasTkAgg(fig, master=fenetre)
    canvas.draw()
    canvas.get_tk_widget().place(x=400,y=100)

    # Dessiner le graphe
    nx.draw(G, with_labels=True, node_size=500, node_color="blue", ax=fig.gca())

    info_label = tk.Label(fenetre, text=f"Informations du graphe : \n Nombre de nœuds = {G.number_of_nodes()} \n Nombre d'arêtes = {G.number_of_edges()}",fg="blue")
    info_label.place(x=520, y=20)
def charger_graphe3():
    global canvas
    
    contenu = champ_texte.get("1.0", tk.END)

    with open("temp.txt", "w") as fichier:
        fichier.write(contenu)

    G = nx.read_edgelist("temp.txt", data=[('weight', int)], create_using=nx.DiGraph())
    pos = nx.spring_layout(G)

    if canvas:
        canvas.get_tk_widget().destroy()

    fig = plt.figure(figsize=(4, 4))
    canvas = FigureCanvasTkAgg(fig, master=fenetre)
    canvas.draw()
    canvas.get_tk_widget().place(x=400,y=100)

        # Dessiner le graphe avec les poids
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="blue")
    nx.draw_networkx_edge_labels(G, pos, font_size=10, edge_labels=nx.get_edge_attributes(G, 'weight'))
    poids_total = sum(nx.get_edge_attributes(G, 'weight').values())
    info_label = tk.Label(fenetre, text=f"Informations du graphe : \n Nombre de nœuds = {G.number_of_nodes()} \n Nombre d'arêtes = {G.number_of_edges()} \n Poids total = {poids_total}",fg="blue") 
    info_label.place(x=520, y=20)


    
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
    fig = plt.figure(figsize=(4, 4))
    canvas = FigureCanvasTkAgg(fig, master=fenetre)
    canvas.draw()
    canvas.get_tk_widget().place(x=400,y=100)
    # Dessiner le graphe
    nx.draw(G,pos,with_labels=True,node_size=500,node_color="blue")
    nx.draw_networkx_edge_labels(G,pos,font_size=10, edge_labels=nx.get_edge_attributes(G,'weight'))
    poids_total = sum(nx.get_edge_attributes(G, 'weight').values())
    info_label = tk.Label(fenetre, text=f"Informations du graphe : \n Nombre de nœuds = {G.number_of_nodes()} \n Nombre d'arêtes = {G.number_of_edges()} \n Poids total = {poids_total}",fg="blue") 
    info_label.place(x=520, y=20)
    

# Créer la fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Mon Application")  # Ajouter un titre à la fenêtre
load = Image.open("C:/Users/pc/Desktop/th/tik+net/Projet_th_graphes/asset/image.png")
photo = ImageTk.PhotoImage(load) 
label = tk.Label(image=photo, bg ="#F0FFF0")
label.image=photo
label.place(x=0,y=0,height = 581,width = 845)
# get wigth & height of screen
width = 845
height = 581

# set screensize as fullscreen and not resizable
fenetre.geometry("%dx%d" % (width, height))
fenetre.resizable(False, False)
flash_label = tk.Label(fenetre, text="", fg="red")
flash_label.pack()

def update_flash_message(message):

    flash_label.config(text=message)
    flash_label.configure(bg="#F0FFFF")
    flash_label.place(x=20,y=30)

update_flash_message(" AIDE: \n Pour créer un graph ou un digraph, utilisez la syntaxe suivante : \n  noeud1 noeud2 \n Exemple : 1 2 \n Pour créer un graph pondéré, utilisez la syntaxe suivante : \n noeud1 noeud2 cout \n Exemple : 1 2 4 (le cout:4)")

# Créer le champ de texte pour le contenu du fichier
champ_texte = tk.Text(fenetre)
champ_texte.place(x=40,y=150 ,height=300, width=300)


# Créer le bouton pour charger le graphe
bouton_charger = tk.Button(fenetre, text="Charger Digraph", command=charger_graphe)
bouton_charger.place(x=70,y=470)  # Ajouter un espacement vertical (padding) entre les éléments
# Créer le bouton pour charger le graphe
bouton_charger2 = tk.Button(fenetre, text="Charger Graph", command=charger_graphe2)
bouton_charger2.place(x=220,y=470)  # Ajouter un espacement vertical (padding) entre les éléments
# Créer le bouton pour charger le graphe
bouton_charger3 = tk.Button(fenetre, text="Charger Graph pondere oriente", command=charger_graphe3)
bouton_charger3.place(x=100,y=500)  # Ajouter un espacement vertical (padding) entre les éléments
# Créer le bouton pour charger le graphe
bouton_charger4 = tk.Button(fenetre, text="Charger Graph pondere non-oriente", command=charger_graphe4)
bouton_charger4.place(x=85,y=530)   # Ajouter un espacement vertical (padding) entre les éléments
# creer le bouton pour passer a la fenetre des algorithme
bouton_passer_algo = tk.Button( fenetre, text="Choisir algorithme" , command=passer_algo)
bouton_passer_algo.place(x=550,y=530)
# Créer le canvas

# # Créer le canvas pour afficher le graphe
fig = plt.figure(figsize=(4, 4))  # Définir la taille du graphe (8 pouces de largeur, 6 pouces de hauteur)
canvas = FigureCanvasTkAgg(fig, master=fenetre)
canvas.draw()
canvas.get_tk_widget().place(x=400,y=100)


# Lancer la boucle d'événements Tkinter
fenetre.mainloop()
