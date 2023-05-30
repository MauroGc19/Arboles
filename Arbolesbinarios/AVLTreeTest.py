from AVLlibTree import AVLTree
import matplotlib.pyplot as plt

def plot_tree(node, X=0, Y=0, delta_x=20,delta_y=50):
    if node is None:
        return
    text = str(node.data)
    plt.text(X, Y, text, color="white", fontweight="bold", horizontalalignment="center",
             fontsize=10, bbox=dict(facecolor='green', edgecolor='black', boxstyle='round,pad=0.5'))
    if node.left_node is not None:
        plt.plot([X,X-delta_x],[Y,Y-delta_y], color='black')
        plot_tree(node.left_node, X-delta_x, Y-delta_y, delta_x/2, delta_y-10)
    if node.right is not None:
        plt.plot([X,X-delta_x],[Y,Y-delta_y], color='black')
        plot_tree(node.right_node, X-delta_x, Y-delta_y, delta_x/2, delta_y-10)
tree = AVLTree(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.insert(4)
tree.insert(6)
tree.insert(7)