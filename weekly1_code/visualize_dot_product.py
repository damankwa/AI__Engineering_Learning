import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def visualize_dot_product():
    """Show how dot product calculates similarity"""

    # Example: king vs queen
    king = np.array([0.9, 0.9, 0.9])
    queen = np.array([0.1, 0.9, 0.9])

    # Calculate each multiplication
    multiplications = king * queen  # Element-wise multiplication
    dot_product = np.sum(multiplications)

    # Create visualization
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

    # Plot 1: The vectors
    dimensions = ['Gender', 'Royalty', 'Power']
    x_pos = np.arange(len(dimensions))

    ax1.bar(x_pos - 0.2, king, 0.4, label='king', alpha=0.7)
    ax1.bar(x_pos + 0.2, queen, 0.4, label='queen', alpha=0.7)
    ax1.set_xlabel('Dimensions')
    ax1.set_ylabel('Values')
    ax1.set_title('Original Vectors')
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(dimensions)
    ax1.legend()

    # Plot 2: Element-wise multiplication
    ax2.bar(dimensions, multiplications, color='green', alpha=0.7)
    ax2.set_ylabel('Multiplication Result')
    ax2.set_title('Element-wise Multiplication')
    for i, v in enumerate(multiplications):
        ax2.text(i, v + 0.01, f'{v:.2f}', ha='center')

    # Plot 3: Final sum
    ax3.bar(['Dot Product'], [dot_product], color='red', alpha=0.7)
    ax3.set_ylabel('Similarity Score')
    ax3.set_title('Final Similarity')
    ax3.text(0, dot_product + 0.02, f'{dot_product:.2f}', ha='center')

    plt.tight_layout()
    plt.savefig('dot_product_explanation.png', dpi=150)
    plt.show()

    return dot_product

# Run this
similarity = visualize_dot_product()
print(f"King and Queen similarity: {similarity:.2f}")