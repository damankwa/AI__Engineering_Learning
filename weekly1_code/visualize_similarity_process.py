import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def visualize_similarity_process():
    """Show the complete similarity finding process"""
    
    # Our data
    words_data = {
        'king':   [0.9, 0.9, 0.9],
        'queen':  [0.1, 0.9, 0.9],
        'man':    [0.9, 0.1, 0.5],
        'woman':  [0.1, 0.1, 0.5],
        'cat':    [0.5, 0.0, 0.2]
    }
    
    target_word = 'king'
    target_vector = np.array(words_data[target_word])
    
    # Calculate similarities
    similarities = {}
    for word, vector in words_data.items():
        if word != target_word:
            similarity = np.dot(target_vector, np.array(vector))
            similarities[word] = similarity
    
    # Create visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Plot 1: All similarities
    words = list(similarities.keys())
    scores = list(similarities.values())
    colors = ['red' if score > 1.5 else 'orange' if score > 1.0 else 'lightblue' 
              for score in scores]
    
    bars = ax1.bar(words, scores, color=colors)
    ax1.set_title(f'Similarity to "{target_word}"')
    ax1.set_ylabel('Similarity Score')
    ax1.tick_params(axis='x', rotation=45)
    
    # Add value labels on bars
    for bar, score in zip(bars, scores):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{score:.2f}', ha='center', va='bottom')
    
    # Plot 2: Sorted ranking
    sorted_items = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    sorted_words = [item[0] for item in sorted_items]
    sorted_scores = [item[1] for item in sorted_items]
    
    ranks = range(1, len(sorted_words) + 1)
    ax2.barh(ranks, sorted_scores, color=['gold', 'silver', 'brown', 'gray'])
    ax2.set_yticks(ranks)
    ax2.set_yticklabels([f"{rank}. {word}" for rank, word in zip(ranks, sorted_words)])
    ax2.set_xlabel('Similarity Score')
    ax2.set_title('Ranked by Similarity')
    ax2.invert_yaxis()  # Highest rank at top
    
    plt.tight_layout()
    plt.savefig('similarity_process.png', dpi=150)
    plt.show()
    
    return sorted_items

# Run this
ranking = visualize_similarity_process()
print("Final ranking:")
for i, (word, score) in enumerate(ranking, 1):
    print(f"  {i}. {word}: {score:.2f}")