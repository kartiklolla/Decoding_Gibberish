import numpy as np
from PIL import Image

img = Image.open('clueimg.png')
width, height = img.size

diagonal_pixels = []
for i in range(min(width, height)):
    pixel = img.getpixel((i, i)) 
    diagonal_pixels.append(pixel)

new_image = Image.new('RGB', (len(diagonal_pixels), 1))
new_image.putdata(diagonal_pixels)

new_image.save('diagonal_pixels_image.png')
print("Diagonal pixels visualized in 'diagonal_pixels_image.png'.")

