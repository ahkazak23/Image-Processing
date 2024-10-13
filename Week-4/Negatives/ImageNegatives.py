# %%
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

original_image = Image.open('./Week-4/Img1.jpg')
gray_image = original_image.convert('L')
gray_image_array = np.array(gray_image)

L = 256
inverted_array = L - 1 - gray_image_array

inverted_image = Image.fromarray(inverted_array)


gray_image.save('gray_image.jpg')
inverted_image.save('inverted_image.jpg')


fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(original_image)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(gray_image, cmap='gray')
axes[1].set_title('Grayscale Image')
axes[1].axis('off')

axes[2].imshow(inverted_image, cmap='gray')
axes[2].set_title('Inverted Image')
axes[2].axis('off')

plt.tight_layout()
plt.show()
