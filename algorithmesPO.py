
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

import collections
import matplotlib.backends.backend_tkagg as tkagg
import matplotlib.pyplot as plt
import networkx as nx
import tkinter as tk
from tkinter import ttk

def run_bellman_ford():
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

    # Create the window to display the graph
    bellmanfordwindow = tk.Toplevel()
    bellmanfordwindow.title("Graph avant et après l'algorithme de Bellman-Ford")
    bellmanfordwindow.geometry("800x600")

    # Create a figure and canvas to draw the graphs
    fig = plt.figure(figsize=(12, 6))
    canvas = tkagg.FigureCanvasTkAgg(fig, master=bellmanfordwindow)
    canvas.get_tk_widget().pack()

    # Draw the original graph
    ax1 = fig.add_subplot(121)
    pos = nx.spring_layout(G)  # Layout for better node positioning
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10, arrows=True, ax=ax1)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax1)
    ax1.set_title("Graphe original")

    # Create a new window for node selection
    node_selection_window = tk.Toplevel(bellmanfordwindow)
    node_selection_window.title("Sélection des nœuds source et cible")
    node_selection_window.geometry("400x200")

    # Get the list of nodes
    nodes = list(G.nodes())

    # Create comboboxes to select source and target nodes
    source_var = tk.StringVar()
    source_label = ttk.Label(node_selection_window, text="Source Node:")
    source_label.pack()
    source_combobox = ttk.Combobox(node_selection_window, textvariable=source_var, values=nodes)
    source_combobox.pack()

    target_var = tk.StringVar()
    target_label = ttk.Label(node_selection_window, text="Target Node:")
    target_label.pack()
    target_combobox = ttk.Combobox(node_selection_window, textvariable=target_var, values=nodes)
    target_combobox.pack()

    def apply_bellman_ford():
        # Get the selected source and target nodes
        start_node = source_combobox.get()
        target_node = target_combobox.get()

        # Apply Bellman-Ford algorithm
        shortest_path = nx.shortest_path(G, source=start_node, target=target_node)

        # Update the graph with the shortest path
        for i in range(len(shortest_path) - 1):
            node1 = shortest_path[i]
            node2 = shortest_path[i + 1]
            G[node1][node2]['color'] = 'red'

        # Draw the graph after Bellman-Ford
        ax2 = fig.add_subplot(122)
        edge_colors = nx.get_edge_attributes(G, 'color').values()
        nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10, arrows=True,
                edge_color=edge_colors, ax=ax2)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax2)
        ax2.set_title("Graph après Bellman-Ford")

        # Draw the graphs on the canvas
        canvas.draw()

    # Create a button to apply the Bellman-Ford algorithm
    apply_button = ttk.Button(node_selection_window, text="Appliquer", command=apply_bellman_ford)
    apply_button.pack()

    # Display the windows
    node_selection_window.mainloop()
    bellmanfordwindow.mainloop()













