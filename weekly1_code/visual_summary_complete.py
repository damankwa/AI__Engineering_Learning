import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np



def create_complete_summary():
    """Create a comprehensive visual summary"""

    fig = plt.figure(figsize=(16, 12))

    # Main title
    fig.suptitle('How AI Understands Word Similarity', fontsize=16, fontweight='bold')

    words_data = {
        'king':   [0.9, 0.9, 0.9],
        'queen':  [0.1, 0.9, 0.9],
        'man':    [0.9, 0.1, 0.5],
        'woman':  [0.1, 0.1, 0.5],
        'cat':    [0.5, 0.0, 0.2]
    }

    # Subplot 1: Word vectors as bars
    ax1 = plt.subplot(2, 3, 1)
    dimensions = ['Gender', 'Royalty', 'Power']
    x = np.arange(len(dimensions))
    width = 0.15

    for i, (word, vector) in enumerate(words_data.items()):
        ax1.bar(x + i*width, vector, width, label=word, alpha=0.8)

    ax1.set_xlabel('Dimensions')
    ax1.set_ylabel('Values')
    ax1.set_title('1. Words as Vectors')
    ax1.set_xticks(x + width * 2)
    ax1.set_xticklabels(dimensions)
    ax1.legend()

    # Subplot 2: Similarity matrix
    ax2 = plt.subplot(2, 3, 2)
    words = list(words_data.keys())
    similarity_matrix = np.zeros((len(words), len(words)))

    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            vec1 = np.array(words_data[word1])
            vec2 = np.array(words_data[word2])
            similarity_matrix[i, j] = np.dot(vec1, vec2)

    im = ax2.imshow(similarity_matrix, cmap='Blues')
    ax2.set_xticks(range(len(words)))
    ax2.set_yticks(range(len(words)))
    ax2.set_xticklabels(words)
    ax2.set_yticklabels(words)
    ax2.set_title('2. Similarity Matrix')

    # Add similarity scores to cells
    for i in range(len(words)):
        for j in range(len(words)):
            ax2.text(j, i, f'{similarity_matrix[i, j]:.1f}',
                    ha="center", va="center", color="black")

    # Subplot 3: Focus on king similarities
    ax3 = plt.subplot(2, 3, 3)
    king_similarities = {}
    king_vec = np.array(words_data['king'])

    for word, vector in words_data.items():
        if word != 'king':
            similarity = np.dot(king_vec, np.array(vector))
            king_similarities[word] = similarity

    sorted_words = sorted(king_similarities.items(), key=lambda x: x[1], reverse=True)
    words_sorted = [item[0] for item in sorted_words]
    scores_sorted = [item[1] for item in sorted_words]

    colors = ['gold', 'silver', 'brown', 'gray']
    ax3.bar(words_sorted, scores_sorted, color=colors[:len(words_sorted)])
    ax3.set_title('3. Most Similar to "King"')
    ax3.set_ylabel('Similarity Score')
    ax3.tick_params(axis='x', rotation=45)

    # Subplot 4: The dot product explained
    ax4 = plt.subplot(2, 3, 4)
    king_vec = [0.9, 0.9, 0.9]
    queen_vec = [0.1, 0.9, 0.9]
    multiplications = [k*q for k, q in zip(king_vec, queen_vec)]

    ax4.bar(dimensions, multiplications, color='green', alpha=0.7)
    ax4.set_title('4. Dot Product Calculation')
    ax4.set_ylabel('king[i] × queen[i]')
    for i, v in enumerate(multiplications):
        ax4.text(i, v + 0.01, f'{v:.2f}', ha='center')

    total = sum(multiplications)
    ax4.text(1, max(multiplications) * 0.8, f'Sum = {total:.2f}', 
            ha='center', fontsize=12, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow"))

    # Subplot 5: Why it works
    ax5 = plt.subplot(2, 3, 5)
    ax5.text(0.1, 0.8, "Why Dot Product = Similarity?", fontsize=14, fontweight='bold')
    ax5.text(0.1, 0.6, "• High values in same dimensions\n  → High dot product\n  → Similar meaning", fontsize=12)
    ax5.text(0.1, 0.3, "• Different values\n  → Low dot product\n  → Different meaning", fontsize=12)
    ax5.set_xlim(0, 1)
    ax5.set_ylim(0, 1)
    ax5.axis('off')
    ax5.set_title('5. The Intuition')

    # Subplot 6: Real AI connection
    ax6 = plt.subplot(2, 3, 6)
    ax6.text(0.1, 0.8, "In Real AI Systems:", fontsize=14, fontweight='bold')
    ax6.text(0.1, 0.6, "• Vectors have 1000+ dimensions\n• Learned from massive text data\n• Same math, bigger scale!", fontsize=12)
    ax6.text(0.1, 0.2, "This is how ChatGPT understands\nword relationships!", fontsize=12, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue"))
    ax6.set_xlim(0, 1)
    ax6.set_ylim(0, 1)
    ax6.axis('off')
    ax6.set_title('6. Real World Connection')

    plt.tight_layout()
    plt.savefig('complete_day1_summary.png', dpi=150, bbox_inches='tight')
    plt.show()

# Create the complete summary
create_complete_summary()