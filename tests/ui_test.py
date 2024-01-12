import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
node_positions = {}  # Dictionary to store positions of nodes

def on_node_pick(event):
    if event.button == 1:  # Left click: add node
        new_node = len(G.nodes) + 1
        G.add_node(new_node, color='blue')
        node_positions[new_node] = (event.xdata, event.ydata)
        nx.draw(G, pos=node_positions, with_labels=True, node_color=[G.nodes[n]['color'] for n in G.nodes()])
        plt.draw()

def on_node_click(event):
    if event.button == 3:  # Right click: remove node
        if isinstance(event.artist, plt.Circle):
            node = int(event.artist.get_label())
            if node in G.nodes:
                G.remove_node(node)
                del node_positions[node]
                nx.draw(G, pos=node_positions, with_labels=True, node_color=[G.nodes[n]['color'] for n in G.nodes()])
                plt.draw()

fig, ax = plt.subplots()

nx.draw(G, pos=node_positions, with_labels=True)

# Assign pick event to nodes for interaction
for node in G.nodes:
    circle = nx.draw_networkx_nodes(G, pos=node_positions, nodelist=[node], node_size=200, node_color='blue', ax=ax)
    circle.set_picker(10)  # Set the radius for pickability
    label = ax.text(node_positions[node][0], node_positions[node][1], str(node), ha='center', va='center', fontsize=8)
    label.set_picker(10)

plt.gcf().canvas.mpl_connect('pick_event', on_node_pick)
plt.gcf().canvas.mpl_connect('button_press_event', on_node_click)

plt.show()