#%%
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

original_image = Image.open('./Week-4/Img1.jpg')
gray_image = original_image.convert('L')
gray_image_array = np.array(gray_image)

normalized_image_array = gray_image_array / 255.0
gamma = 2.0

gamma_transformed = np.power(normalized_image_array, gamma)
gamma_transformed = np.array(255 * gamma_transformed, dtype=np.uint8)

gamma_image = Image.fromarray(gamma_transformed)
gamma_image.save('gamma_transformed_image.jpg')

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title('Original Grayscale Image')
axes[0].axis('off')

axes[1].imshow(gamma_image, cmap='gray')
axes[1].set_title(f'Gamma Transformed Image (γ={gamma})')
axes[1].axis('off')

plt.tight_layout()
plt.show()
