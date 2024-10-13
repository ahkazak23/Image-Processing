# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def histogram_equalization(image):
    equalized_image = cv2.equalizeHist(image)
    return equalized_image

image_path = "./Week-4/Img3.jpg"
image = Image.open(image_path).convert('L')
image_array = np.array(image)

equalized_image = histogram_equalization(image_array)

fig, axs = plt.subplots(2, 2, figsize=(14, 12))

axs[0, 0].imshow(image_array, cmap='gray')
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')

axs[0, 1].imshow(equalized_image, cmap='gray')
axs[0, 1].set_title('Histogram Equalized Image')
axs[0, 1].axis('off')

axs[1, 0].hist(image_array.ravel(), bins=256, range=(0, 256), color='black')
axs[1, 0].set_title('Original Histogram')

axs[1, 1].hist(equalized_image.ravel(), bins=256, range=(0, 256), color='black')
axs[1, 1].set_title('Equalized Histogram')

plt.tight_layout()
plt.show()

