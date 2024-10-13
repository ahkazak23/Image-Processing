#%%
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
import numpy as np

image_path = "./Week-4//Img3.jpg"
image = Image.open(image_path)

enhancer = ImageEnhance.Contrast(image)
contrast_image = enhancer.enhance(2.0)

stretched_image_path = "contrast_stretched_image.jpg"
contrast_image.save(stretched_image_path)

image_array = np.array(image)
contrast_image_array = np.array(contrast_image)

def plot_histogram(ax, image_array, title):
    ax.hist(image_array.ravel(), bins=256, color='black', alpha=0.7)
    ax.set_title(title)
    ax.set_xlim([0, 256])
    ax.set_xlabel('Pixel Intensity')
    ax.set_ylabel('Frequency')
    ax.set_facecolor('white')

fig, axs = plt.subplots(2, 2, figsize=(12, 12), facecolor='white')

axs[0, 0].imshow(image)
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')

axs[0, 1].imshow(contrast_image)
axs[0, 1].set_title('Contrast Stretched Image')
axs[0, 1].axis('off')

plot_histogram(axs[1, 0], image_array, 'Original Image Histogram')
plot_histogram(axs[1, 1], contrast_image_array, 'Contrast Stretched Image Histogram')

plt.tight_layout()
plt.show()
