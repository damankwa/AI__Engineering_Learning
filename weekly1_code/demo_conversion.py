import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def demonstrate_conversion():
    """Show exactly what the conversion does"""

    print("🔄 CONVERSION PROCESS")
    print("=" * 50)

    # Starting data
    words_with_lists = {
        'king':   [0.9, 0.9, 0.9],
        'queen':  [0.1, 0.9, 0.9],
        'cat':    [0.5, 0.0, 0.2]
    }

    words_with_arrays = {}

    print("BEFORE conversion:")
    for word, vec in words_with_lists.items():
        print(f"  {word}: {vec} (type: {type(vec)})")

    print("\nDURING conversion:")

    # The actual loop (step by step)
    for word in words_with_lists:
        print(f"\n  Processing '{word}':")

        # Step 1: Get the list
        list_vector = words_with_lists[word]
        print(f"    1. Get list: {list_vector}")

        # Step 2: Convert to numpy
        numpy_vector = np.array(list_vector)
        print(f"    2. Convert to numpy: {numpy_vector}")

        # Step 3: Store in new dictionary
        words_with_arrays[word] = numpy_vector
        print(f"    3. Store in new dict: ✓")

    print("\nAFTER conversion:")
    for word, vec in words_with_arrays.items():
        print(f"  {word}: {vec} (type: {type(vec)})")

    print("\n✨ Now we can do fast math!")
    print(f"Dot product example: {np.dot(words_with_arrays['king'], words_with_arrays['queen'])}")

# Run this to see the complete process
demonstrate_conversion()