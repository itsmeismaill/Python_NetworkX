import tkinter as tk
import collections
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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

def bfs():
    # Read the list from the temp.txt file
    with open("temp.txt", "r") as fichier:
        liste = fichier.read().split()

    # Create the graph from the list
    graph = collections.defaultdict(list)
    for i in range(0, len(liste), 2):
        node1, node2 = liste[i], liste[i + 1]
        graph[node1].append(node2)
        graph[node2].append(node1)

    # Execute the BFS algorithm
    visited = set()
    queue = collections.deque()

    bfs_fenetre = tk.Toplevel()
    bfs_fenetre.title("Résultats de BFS")
    bfs_fenetre.geometry("400x300")

    # Display graph information
    num_nodes = len(graph)
    num_edges = sum(len(neighbors) for neighbors in graph.values()) // 2
    info_label = tk.Label(bfs_fenetre, text=f"Nombre de nœuds: {num_nodes}\nNombre d'arêtes: {num_edges}")
    info_label.pack()


    # Select a starting node (via user selection)
    start_label = tk.Label(bfs_fenetre, text="Choisissez un nœud de départ:")
    start_label.pack()

    # Create a combobox to select the start node
    start_combobox = ttk.Combobox(bfs_fenetre, values=list(graph.keys()))
    start_combobox.pack()

    def start_bfs():
        start_node = start_combobox.get()
        visited.add(start_node)
        queue.append(start_node)

        # Perform BFS traversal
        while queue:
            current_node = queue.popleft()
            visited_label = tk.Label(bfs_fenetre, text=current_node)
            visited_label.pack()

            # Traverse all neighbors of the current node
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    # Add a button to start BFS
    start_button = tk.Button(bfs_fenetre, text="Démarrer BFS", command=start_bfs)
    start_button.pack()



def dfs():
    # Read the list from the temp.txt file
    with open("temp.txt", "r") as fichier:
        liste = fichier.read().split()

    # Create the graph from the list
    graph = collections.defaultdict(list)
    for i in range(0, len(liste), 2):
        node1, node2 = liste[i], liste[i + 1]
        graph[node1].append(node2)
        graph[node2].append(node1)

    # Function to perform recursive DFS
    def dfs_recursive(start, visited):
        visited.add(start)
        visited_label = tk.Label(dfs_fenetre, text=start)
        visited_label.pack()

        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs_recursive(neighbor, visited)

    # Create the window to display the DFS results
    dfs_fenetre = tk.Toplevel()
    dfs_fenetre.title("Résultats de DFS")
    dfs_fenetre.geometry("400x300")
    # Display graph information
    num_nodes = len(graph)
    num_edges = sum(len(neighbors) for neighbors in graph.values()) // 2
    info_label = tk.Label(dfs_fenetre, text=f"Nombre de nœuds: {num_nodes}\nNombre d'arêtes: {num_edges}")
    info_label.pack()

    # Create the Label widget to display the DFS results in dfs_fenetre
    result_label = tk.Label(dfs_fenetre, text="Résultats de DFS:")
    result_label.pack()

    # Choose a starting node (via user selection)
    start_label = tk.Label(dfs_fenetre, text="Choisissez un nœud de départ:")
    start_label.pack()

    # Create a combobox to select the start node
    start_combobox = ttk.Combobox(dfs_fenetre, values=list(graph.keys()))
    start_combobox.pack()

    def start_dfs():
        start_node = start_combobox.get()
        visited = set()
        dfs_recursive(start_node, visited)


    # Add a button to start DFS
    start_button = tk.Button(dfs_fenetre, text="Démarrer DFS", command=start_dfs)
    start_button.pack()

import collections
import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def kruskal():
    # Lire la liste depuis le fichier temp.txt
    with open("temp.txt", "r") as fichier:
        liste = fichier.read().split()

    # Créer le graphe à partir de la liste
    graph = collections.defaultdict(list)
    for i in range(0, len(liste), 3):
        node1, node2, weight = liste[i], liste[i + 1], int(liste[i + 2])
        graph[node1].append((node2, weight))
        graph[node2].append((node1, weight))

    # Exécuter l'algorithme de Kruskal
    edges = []
    for node in graph:
        for neighbor, weight in graph[node]:
            edges.append((node, neighbor, weight))
    edges.sort(key=lambda x: x[2])  # Trier les arêtes par poids croissant

    mst = nx.Graph()
    uf = {node: node for node in graph}

    for edge in edges:
        node1, node2, weight = edge
        if find(uf, node1) != find(uf, node2):
            union(uf, node1, node2)
            mst.add_edge(node1, node2, weight=weight)

    kruskal_fenetre = tk.Toplevel()
    kruskal_fenetre.title("Résultats de Kruskal")
    kruskal_fenetre.geometry("600x400")
    total_cost = sum(mst[u][v]['weight'] for u, v in mst.edges())
    cost_label = tk.Label(kruskal_fenetre, text=f"Coût total de l'ACM: {total_cost}")
    cost_label.pack()
    # Display graph information
    num_nodes = len(graph)
    num_edges = sum(len(neighbors) for neighbors in graph.values()) // 2
    info_label = tk.Label(kruskal_fenetre, text=f"Nombre de nœuds: {num_nodes}\nNombre d'arêtes: {num_edges}")
    info_label.pack()
    # Dessiner le graphe avec l'ACM
    fig = plt.figure()
    canvas = FigureCanvasTkAgg(fig, master=kruskal_fenetre)
    canvas.get_tk_widget().pack()

    pos = nx.spring_layout(mst)
    nx.draw_networkx(mst, pos, with_labels=True, node_size=300, node_color="blue", edge_color="red")
    edge_labels = nx.get_edge_attributes(mst, 'weight')
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=edge_labels)

    canvas.draw()



def find(uf, node):
    if uf[node] != node:
        uf[node] = find(uf, uf[node])
    return uf[node]

def union(uf, node1, node2):
    uf[find(uf, node1)] = find(uf, node2)





def dijkstra():
    # Lire la liste depuis le fichier temp.txt
    with open("temp.txt", "r") as fichier:
        liste = fichier.read().split()

    # Créer le graphe à partir de la liste
    graph = collections.defaultdict(list)
    for i in range(0, len(liste), 3):
        node1, node2, weight = liste[i], liste[i + 1], int(liste[i + 2])
        graph[node1].append((node2, weight))
        graph[node2].append((node1, weight))

    dijkstra_fenetre = tk.Tk()
    dijkstra_fenetre.title("Dijkstra Algorithm")
    dijkstra_fenetre.geometry("400x200")

   # Choose a starting node (via user selection)
    start_label = tk.Label(dijkstra_fenetre, text="Choisissez un nœud de départ:")
    start_label.pack()

    # Create a combobox to select the start node
    start_combobox = ttk.Combobox(dijkstra_fenetre, values=list(graph.keys()))
    start_combobox.pack()

    def run_dijkstra():
        start_node = start_combobox.get()
        # Exécuter l'algorithme de Dijkstra
        distances = {node: float('inf') for node in graph}
        distances[start_node] = 0
        visited = set()

        while len(visited) < len(graph):
            min_distance = float('inf')
            min_node = None

            # Trouver le nœud non visité avec la distance minimale
            for node in graph:
                if node not in visited and distances[node] < min_distance:
                    min_distance = distances[node]
                    min_node = node

            visited.add(min_node)

            # Mettre à jour les distances des voisins du nœud sélectionné
            for neighbor, weight in graph[min_node]:
                new_distance = distances[min_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

        # Construire l'Arbre Couvrant Minimum (ACM)
        mst = nx.Graph()
        for node in distances:
            if node != start_node:
                weight = distances[node]
                mst.add_edge(start_node, node, weight=weight)

        result_fenetre = tk.Toplevel(dijkstra_fenetre)
        result_fenetre.title("Résultats de Dijkstra")
        result_fenetre.geometry("600x400")
        total_cost = sum(mst[u][v]['weight'] for u, v in mst.edges())
        cost_label = tk.Label(result_fenetre, text=f"Coût total de l'ACM: {total_cost}")
        cost_label.pack()

        # Dessiner le graphe avec l'ACM
        fig = plt.figure()
        canvas = FigureCanvasTkAgg(fig, master=result_fenetre)
        canvas.get_tk_widget().pack()

        pos = nx.spring_layout(mst)
        nx.draw_networkx(mst, pos, with_labels=True, node_size=300, node_color="blue", edge_color="red")
        edge_labels = nx.get_edge_attributes(mst, 'weight')
        nx.draw_networkx_edge_labels(mst, pos, edge_labels=edge_labels)

        canvas.draw()

    run_button = tk.Button(dijkstra_fenetre, text="Run Dijkstra", command=run_dijkstra)
    run_button.pack()








