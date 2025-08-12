Key Takeaways with Visuals

Words → Numbers: We convert words to lists of numbers that capture meaning
Dimensions = Aspects: Each number represents an aspect (gender, power, etc.)
Dot Product = Similarity: Multiplying and adding measures how alike words are
Higher Score = More Similar: Math gives us similarity rankings
This is Real AI: Same principle used in ChatGPT, just with bigger vectors!

Run these visualization functions to see the diagrams. They'll help you understand what's happening behind the math!

In Simple Terms
What the code does:

Take each word from the dictionary
Get its list of numbers (like [0.9, 0.9, 0.9])
Convert the list to a NumPy array (for faster math)
Put the NumPy array back in a new dictionary
Repeat for all words
Return the new dictionary with NumPy arrays instead of lists

Why we do this:

Python lists: Good for storing data, bad for math
NumPy arrays: Optimized for mathematical operations
We need to do lots of math (dot products), so we convert!