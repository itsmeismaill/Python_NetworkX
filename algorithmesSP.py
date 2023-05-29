import tkinter as tk
import collections
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.backends.backend_tkagg as tkagg
from tkinter import ttk
def bfsP():
    # Read the list from the temp.txt file
    with open("temp.txt", "r") as fichier:
        liste = fichier.read().split()

    # Create the graph from the list
    graph = collections.defaultdict(list)
    weights = {}
    for i in range(0, len(liste), 3):
        node1, node2, weight = liste[i], liste[i + 1], int(liste[i + 2])
        graph[node1].append(node2)
        graph[node2].append(node1)
        weights[(node1, node2)] = weight
        weights[(node2, node1)] = weight

    # Execute the BFS algorithm
    visited = set()
    queue = collections.deque()

    bfs_fenetre = tk.Toplevel()
    bfs_fenetre.title("Résultats de BFS")
    bfs_fenetre.geometry("400x300")

    # Display graph information
    num_nodes = len(graph)
    num_edges = sum(len(neighbors) for neighbors in graph.values()) // 2
    info_label = tk.Label(bfs_fenetre, text=f"Nombre de nœuds: {num_nodes}\nNombre d'arêtes: {num_edges}", fg="blue")
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

def dfsP():
    # Read the list from the temp.txt file
    with open("temp.txt", "r") as fichier:
        liste = fichier.read().split()

    # Create the graph from the list
    graph = collections.defaultdict(list)
    weights = {}
    for i in range(0, len(liste), 3):
        node1, node2, weight = liste[i], liste[i + 1], int(liste[i + 2])
        graph[node1].append(node2)
        graph[node2].append(node1)
        weights[(node1, node2)] = weight
        weights[(node2, node1)] = weight

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
    info_label = tk.Label(dfs_fenetre, text=f"Nombre de nœuds: {num_nodes}\nNombre d'arêtes: {num_edges}", fg="blue")
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

def warshallPNO():
    # Read the list from the temp.txt file
    with open("temp.txt", "r") as fichier:
        lines = fichier.readlines()

    # Create the weighted graph from the list
    graph = collections.defaultdict(dict)
    for line in lines:
        node1, node2, weight = line.split()
        graph[node1][node2] = float(weight)

    # Create a directed graph from the weighted graph
    G = nx.Graph()
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
def Dijkstra2():
    # Read the list from the temp.txt file
    with open("temp.txt", "r") as fichier:
        lines = fichier.readlines()

    # Create the weighted undirected graph from the list
    graph = collections.defaultdict(dict)
    for line in lines:
        node1, node2, weight = line.split()
        graph[node1][node2] = float(weight)
        graph[node2][node1] = float(weight)

    # Check if the graph has negative weights
    has_negative_weights = any(weight < 0 for weights in graph.values() for weight in weights.values())

    if has_negative_weights:
        # Display the error message in a new window
        error_message = "Le graphe contient des poids négatifs. L'algorithme de Dijkstra ne peut pas être appliqué."
        messagebox.showerror("Erreur", error_message)
        return

    # Create a undirected weighted graph
    G = nx.Graph()
    for node1, neighbors in graph.items():
        for node2, weight in neighbors.items():
            G.add_edge(node1, node2, weight=weight)

    # Create the window to display the graph
    import tkinter as tk
    dijkstrawindow = tk.Toplevel()
    dijkstrawindow.title("Graph avant et après l'algorithme de Dijkstra")
    dijkstrawindow.geometry("800x600")

    # Create a figure and canvas to draw the graphs
    fig = plt.figure(figsize=(12, 4.5))
    canvas = tkagg.FigureCanvasTkAgg(fig, master=dijkstrawindow)
    canvas.get_tk_widget().pack()

    # Create a new frame for node selection
    node_selection_frame = ttk.Frame(dijkstrawindow)
    node_selection_frame.pack(side="top", padx=20, pady=20)

    # Draw the original graph
    ax1 = fig.add_subplot(121)
    pos = nx.spring_layout(G)  # Layout for better node positioning
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10, ax=ax1)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax1)
    ax1.set_title("Graphe original")

    # Get the list of nodes
    nodes = list(G.nodes())

    # Create comboboxes to select source and target nodes
    source_var = tk.StringVar()
    source_label = ttk.Label(node_selection_frame, text="Source Node:")
    source_label.pack()
    source_combobox = ttk.Combobox(node_selection_frame, textvariable=source_var, values=nodes)
    source_combobox.pack()

    target_var = tk.StringVar()
    target_label = ttk.Label(node_selection_frame, text="Target Node:")
    target_label.pack()
    target_combobox = ttk.Combobox(node_selection_frame, textvariable=target_var, values=nodes)
    target_combobox.pack()

    def apply_dijkstra():
        # Clear the previous graph
        fig.clear()

        # Draw the original graph
        ax1 = fig.add_subplot(121)
        pos = nx.spring_layout(G)  # Layout for better node positioning
        nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10, ax=ax1)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax1)
        ax1.set_title("Graphe original")

        # Get the selected source and target nodes
        start_node = source_combobox.get()
        target_node = target_combobox.get()

        # Apply Dijkstra's algorithm
        shortest_path = nx.dijkstra_path(G, source=start_node, target=target_node, weight='weight')

        # Reset the color attribute for all edges
        for edge in G.edges():
            G[edge[0]][edge[1]]['color'] = 'lightblue'

        # Update the graph with the shortest path
        for i in range(len(shortest_path) - 1):
            node1 = shortest_path[i]
            node2 = shortest_path[i + 1]
            G[node1][node2]['color'] = 'red'

        # Draw the graph after Dijkstra
        ax2 = fig.add_subplot(122)
        edge_colors = nx.get_edge_attributes(G, 'color').values()
        nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10,
                edge_color=edge_colors, ax=ax2)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax2)
        ax2.set_title("Plus court chemin de {} à {}".format(start_node, target_node))

        # Draw the graphs on the canvas
        canvas.draw()

    # Create a button to apply Dijkstra's algorithm
    apply_button = ttk.Button(node_selection_frame, text="Appliquer", command=apply_dijkstra)
    apply_button.pack()

    # Display the window
    dijkstrawindow.mainloop()


def bellman_ford2():
    # Read the list from the temp.txt file
    with open("temp.txt", "r") as fichier:
        lines = fichier.readlines()

    # Create the weighted graph from the list
    graph = collections.defaultdict(dict)
    for line in lines:
        node1, node2, weight = line.split()
        graph[node1][node2] = float(weight)
        graph[node2][node1] = float(weight)  # Add the reverse edge for the undirected graph

    # Create an undirected graph from the weighted graph
    G = nx.Graph()
    for node1, neighbors in graph.items():
        for node2, weight in neighbors.items():
            G.add_edge(node1, node2, weight=weight)
    if nx.negative_edge_cycle(G):
        # Display error message if negative cycle exists
        error_message = "Le graphe contient des cycles négatifs. L'algorithme de Bellman-Ford ne peut pas être appliqué."
        messagebox.showerror("Erreur", error_message)
        return

    # Create the window to display the graph
    bellmanfordwidow = tk.Toplevel()
    bellmanfordwidow.title("Graph avant et après l'algorithme de Bellman-Ford")
    bellmanfordwidow.geometry("800x600")

    # Create a figure and canvas to draw the graphs
    fig = plt.figure(figsize=(12, 4.5))
    canvas = tkagg.FigureCanvasTkAgg(fig, master=bellmanfordwidow)
    canvas.get_tk_widget().pack()

    # Create a new frame for node selection
    node_selection_frame = ttk.Frame(bellmanfordwidow)
    node_selection_frame.pack(side="top", padx=20, pady=20)

    # Draw the original graph
    ax1 = fig.add_subplot(121)
    pos = nx.spring_layout(G)  # Layout for better node positioning
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10, ax=ax1)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax1)
    ax1.set_title("Graphe original")

    # Get the list of nodes
    nodes = list(G.nodes())

    # Create comboboxes to select source and target nodes
    source_var = tk.StringVar()
    source_label = ttk.Label(node_selection_frame, text="Source Node:")
    source_label.pack()
    source_combobox = ttk.Combobox(node_selection_frame, textvariable=source_var, values=nodes)
    source_combobox.pack()

    target_var = tk.StringVar()
    target_label = ttk.Label(node_selection_frame, text="Target Node:")
    target_label.pack()
    target_combobox = ttk.Combobox(node_selection_frame, textvariable=target_var, values=nodes)
    target_combobox.pack()

    def apply_bellmanford():
        # Get the selected source and target nodes
        start_node = source_combobox.get()
        target_node = target_combobox.get()

        # Apply Bellman-Ford's algorithm
        shortest_path = nx.bellman_ford_path(G, source=start_node, target=target_node, weight='weight')

        # Reset the color attribute for all edges
        for edge in G.edges():
            G[edge[0]][edge[1]]['color'] = 'lightblue'

        # Update the graph with the shortest path
        for i in range(len(shortest_path) - 1):
            node1 = shortest_path[i]
            node2 = shortest_path[i + 1]
            G[node1][node2]['color'] = 'red'

        # Draw the graph after Bellman-Ford's algorithm
        ax2 = fig.add_subplot(122)
        edge_colors = nx.get_edge_attributes(G, 'color').values()
        nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10,
                edge_color=edge_colors, ax=ax2)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax2)
        ax2.set_title("Plus court chemin entre {} et {}".format(start_node, target_node))

        # Draw the graphs on the canvas
        canvas.draw()

    # Create a button to apply Bellman-Ford's algorithm
    apply_button = ttk.Button(node_selection_frame, text="Appliquer", command=apply_bellmanford)
    apply_button.pack()

    # Display the window
    bellmanfordwidow.mainloop()






