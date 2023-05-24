
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
def warshallPO():
    # Read the list from the temp.txt file
    with open("temp.txt", "r") as fichier:
        lines = fichier.readlines()

    # Create the weighted graph from the list
    graph = collections.defaultdict(dict)
    for line in lines:
        node1, node2, weight = line.split()
        graph[node1][node2] = float(weight)

    # Create a directed graph from the weighted graph
    G = nx.DiGraph()
    for node1, neighbors in graph.items():
        for node2, weight in neighbors.items():
            G.add_edge(node1, node2, weight=weight)

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
    pos = nx.spring_layout(G)  # Layout for better node positioning
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10, arrows=True, ax=ax1)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax1)
    ax1.set_title("Graphe original")

    # Draw the transitive closure graph
    ax2 = fig.add_subplot(122)
    transitive_closure_edge_labels = nx.get_edge_attributes(transitive_closure, 'weight')
    nx.draw(transitive_closure, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10, arrows=True, ax=ax2)
    nx.draw_networkx_edge_labels(transitive_closure, pos, edge_labels=transitive_closure_edge_labels, ax=ax2)
    ax2.set_title("Fermeture transitive")

    # Draw the graphs on the canvas
    canvas.draw()

    # Display the window
    warshall_fenetre.mainloop()