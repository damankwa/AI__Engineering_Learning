# Let's create a visual diagram
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def visualize_word_vectors():
    """Show words as points in 3D space"""

    # Our word vectors
    words_data = {
        'king':   [0.9, 0.9, 0.9],
        'queen':  [0.1, 0.9, 0.9], 
        'man':    [0.9, 0.1, 0.5],
        'woman':  [0.1, 0.1, 0.5],
        'cat':    [0.5, 0.0, 0.2],
        'dog':    [0.5, 0.0, 0.3]
    }

    # Create 3D plot
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot each word as a point
    for word, vector in words_data.items():
        x, y, z = vector
        ax.scatter(x, y, z, s=100, label=word)
        ax.text(x, y, z, '  ' + word, fontsize=12)

    # Label axes with meanings
    ax.set_xlabel('Masculine ← → Feminine')
    ax.set_ylabel('Common ← → Royal') 
    ax.set_zlabel('Weak ← → Powerful')

    ax.set_title('Words as Points in 3D Meaning Space')
    ax.legend()
    plt.tight_layout()
    plt.savefig('word_vectors_3d.png', dpi=150)
    plt.show()

# Run this to see the visualization
visualize_word_vectors()