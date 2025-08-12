# week1_code/day1_vectors_clear.py
import numpy as np
import matplotlib.pyplot as plt

print("🚀 Starting your AI journey - Day 1!")
print("=" * 50)

# Exercise 1: Create word vectors
def create_word_vectors():
    """
    Represent words as 3D vectors: [masculine/feminine, royalty, power]

    Think of each dimension as capturing some aspect of meaning:
    - Dimension 0: Masculine(1.0) vs Feminine(0.0) 
    - Dimension 1: Royal(1.0) vs Common(0.0)
    - Dimension 2: Powerful(1.0) vs Weak(0.0)
    """

    # Step 1: Create a regular dictionary with words as keys and lists as values
    words_with_lists = {}
    words_with_lists['king'] = [0.9, 0.9, 0.9]      # Masculine, royal, powerful
    words_with_lists['queen'] = [0.1, 0.9, 0.9]     # Feminine, royal, powerful
    words_with_lists['man'] = [0.9, 0.1, 0.5]       # Masculine, common, medium power
    words_with_lists['woman'] = [0.1, 0.1, 0.5]     # Feminine, common, medium power  
    words_with_lists['prince'] = [0.9, 0.7, 0.6]    # Masculine, somewhat royal, medium-high power
    words_with_lists['cat'] = [0.5, 0.0, 0.2]       # Neutral gender, not royal, low power
    words_with_lists['dog'] = [0.5, 0.0, 0.3]       # Neutral gender, not royal, low power

    # Step 2: Convert each list to a numpy array (for easier math)
    words_with_arrays = {}

    for word in words_with_lists:
        list_vector = words_with_lists[word]
        numpy_vector = np.array(list_vector)
        words_with_arrays[word] = numpy_vector

    return words_with_arrays

# Exercise 2: Calculate similarities
def word_similarity(word1_vec, word2_vec):
    """
    How similar are two words?
    Uses dot product: a·b = a₁×b₁ + a₂×b₂ + a₃×b₃
    """
    similarity = np.dot(word1_vec, word2_vec)
    return similarity

# Exercise 3: Find most similar words
def find_most_similar_to(target_word, word_vectors, top_n):
    """Find the most similar words to a target word"""

    # Step 1: Get the vector for our target word
    target_vec = word_vectors[target_word]

    # Step 2: Calculate similarity with each other word
    similarities = {}

    for word in word_vectors:
        if word != target_word:  # Don't compare word to itself
            other_vec = word_vectors[word]
            sim = word_similarity(target_vec, other_vec)
            similarities[word] = sim

    # Step 3: Find the words with highest similarity
    # First, get all the (word, similarity) pairs
    word_similarity_pairs = []
    for word in similarities:
        similarity_score = similarities[word]
        pair = (word, similarity_score)
        word_similarity_pairs.append(pair)

    # Step 4: Sort them by similarity score (highest first)
    def get_similarity_score(pair):
        word = pair[0]
        similarity = pair[1]
        return similarity

    sorted_pairs = sorted(word_similarity_pairs, key=get_similarity_score, reverse=True)

    # Step 5: Take only the top N
    top_pairs = []
    for i in range(top_n):
        if i < len(sorted_pairs):  # Make sure we don't go past the end
            top_pairs.append(sorted_pairs[i])

    return top_pairs

# Main execution
if __name__ == "__main__":

    # Step 1: Create our word vectors
    words = create_word_vectors()

    print("📚 Our word vectors:")
    for word in words:
        vec = words[word]
        print("  " + word + ": " + str(vec))

    print("\n🔍 Testing similarity calculations:")

    # Step 2: Test specific pairs
    test_pairs = []
    test_pairs.append(('king', 'queen'))
    test_pairs.append(('king', 'man'))
    test_pairs.append(('cat', 'dog'))
    test_pairs.append(('king', 'cat'))

    for pair in test_pairs:
        word1 = pair[0]
        word2 = pair[1]
        word1_vec = words[word1]
        word2_vec = words[word2]
        sim = word_similarity(word1_vec, word2_vec)
        print("  " + word1 + " ↔ " + word2 + ": " + str(round(sim, 2)))

    print("\n🏆 Most similar words to 'king':")
    similar_to_king = find_most_similar_to('king', words, 3)

    for i in range(len(similar_to_king)):
        pair = similar_to_king[i]
        word = pair[0]
        similarity = pair[1]
        rank = i + 1
        print("  " + str(rank) + ". " + word + ": " + str(round(similarity, 2)))

    print("\n🏆 Most similar words to 'cat':")  
    similar_to_cat = find_most_similar_to('cat', words, 3)

    for i in range(len(similar_to_cat)):
        pair = similar_to_cat[i]
        word = pair[0]
        similarity = pair[1]
        rank = i + 1
        print("  " + str(rank) + ". " + word + ": " + str(round(similarity, 2)))

    print("\n💡 Key insight: Words with similar meanings have higher dot products!")
    print("   This is the foundation of how AI understands language.")