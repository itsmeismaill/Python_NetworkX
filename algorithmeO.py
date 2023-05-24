
import tkinter as tk
import collections
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.backends.backend_tkagg as tkagg
from tkinter import ttk
import collections
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
import networkx as nx
import collections
import tkinter as tk
from tkinter import ttk
def warshallO():
    # Read the list from the temp.txt file
    with open("temp.txt", "r") as fichier:
        liste = fichier.read().split()

    # Create the graph from the list
    graph = collections.defaultdict(list)
    for i in range(0, len(liste), 2):
        node1, node2 = liste[i], liste[i + 1]
        graph[node1].append(node2)

    # Create a directed graph from the adjacency list
    G = nx.DiGraph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Compute the transitive closure using Warshall's algorithm
    transitive_closure = nx.transitive_closure(G)

    # Create the window to display the graph
    warshall_fenetre = tk.Toplevel()
    warshall_fenetre.title("Graph après l'exécution de l'algorithme de Warshall")
    warshall_fenetre.geometry("800x600")

    # Create a figure and canvas to draw the graphs
    fig = plt.figure(figsize=(12, 6))
    canvas = tkagg.FigureCanvasTkAgg(fig, master=warshall_fenetre)
    canvas.get_tk_widget().pack()

    # Draw the original graph
    ax1 = fig.add_subplot(121)
    nx.draw(G, with_labels=True, node_color="lightblue", node_size=500, font_size=10, arrows=True, ax=ax1)
    ax1.set_title("Graphe original")

    # Draw the transitive closure graph
    ax2 = fig.add_subplot(122)
    nx.draw(transitive_closure, with_labels=True, node_color="lightblue", node_size=500, font_size=10, arrows=True, ax=ax2)
    ax2.set_title("Fermeture transitive")

    # Draw the graphs on the canvas
    canvas.draw()

    # Display the window
    warshall_fenetre.mainloop()