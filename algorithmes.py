import tkinter as tk
import collections
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def bfs():
    # Lire la liste depuis le fichier temp.txt
    with open("temp.txt", "r") as fichier:
        liste = fichier.read().split()

    # Créer le graphe à partir de la liste
    graph = collections.defaultdict(list)
    for i in range(0, len(liste), 2):
        node1, node2 = liste[i], liste[i + 1]
        graph[node1].append(node2)
        graph[node2].append(node1)

    # Exécuter l'algorithme BFS
    visited = set()
    queue = collections.deque()

    # Choisir un nœud de départ (par exemple, le premier nœud dans la liste)
    start_node = liste[0]
    visited.add(start_node)
    queue.append(start_node)

    # Créer la fenêtre pour afficher les résultats de BFS
    bfs_fenetre = tk.Toplevel()
    bfs_fenetre.title("Résultats de BFS")
    bfs_fenetre.geometry("400x300")
    
    # Créer le widget Label pour afficher les résultats de BFS dans bfs_fenetre
    result_label = tk.Label(bfs_fenetre, text="Résultats de BFS:")
    result_label.pack()

    # Afficher les nœuds visités au milieu de bfs_fenetre
    while queue:
        current_node = queue.popleft()
        visited_label = tk.Label(bfs_fenetre, text=current_node)
        visited_label.pack()

        # Parcourir tous les voisins du nœud en cours
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)





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

    # Execute the DFS algorithm
    visited = set()

    # Function to perform recursive DFS
    def dfs_recursive(start):
        visited.add(start)
        visited_label = tk.Label(dfs_fenetre, text=start)
        visited_label.pack()

        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs_recursive(neighbor)

    # Create the window to display the DFS results
    dfs_fenetre = tk.Toplevel()
    dfs_fenetre.title("Résultats de DFS")
    dfs_fenetre.geometry("400x300")

    # Create the Label widget to display the DFS results in dfs_fenetre
    result_label = tk.Label(dfs_fenetre, text="Résultats de DFS:")
    result_label.pack()

    # Choose a starting node (e.g., the first node in the list)
    start_node = liste[0]
    dfs_recursive(start_node)


