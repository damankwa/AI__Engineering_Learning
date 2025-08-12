# Images are just NumPy arrays!
from PIL import Image
import numpy as np

# Load an image
img = Image.open('photo.jpg')
img_array = np.array(img)  # Convert to NumPy array

print(f"Image shape: {img_array.shape}")  # e.g., (1080, 1920, 3) = height, width, colors
print(f"Image is just numbers: {img_array[0, 0, :]}") # First pixel's RGB values

# Every pixel is just numbers that NumPy can manipulate!