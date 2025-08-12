import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def explain_dot_product_intuition():
    """Show why dot product = similarity"""

    print("🎯 Dot Product Intuition:")
    print("=" * 40)

    # Case 1: Very similar words
    king = np.array([0.9, 0.9, 0.9])
    queen = np.array([0.1, 0.9, 0.9])

    print(f"King:  {king}")
    print(f"Queen: {queen}")
    print(f"Similarity: {np.dot(king, queen):.2f}")
    print("→ High score because they share 'royal' and 'powerful'")
    print()

    # Case 2: Different words  
    cat = np.array([0.5, 0.0, 0.2])
    print(f"King: {king}")
    print(f"Cat:  {cat}")
    print(f"Similarity: {np.dot(king, cat):.2f}")
    print("→ Low score because cat is not royal or powerful")
    print()

    # Case 3: Opposite words
    weak_commoner = np.array([0.1, 0.1, 0.1])
    print(f"King:         {king}")
    print(f"Weak person:  {weak_commoner}")
    print(f"Similarity: {np.dot(king, weak_commoner):.2f}")
    print("→ Very low score - they're opposites!")

# Run this
explain_dot_product_intuition()