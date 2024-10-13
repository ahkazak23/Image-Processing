# %%
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

original_image = Image.open('./Week-4/Img1.jpg')
gray_image = original_image.convert('L')
gray_image_array = np.array(gray_image)

c = 255 / np.log(1 + np.max(gray_image_array))
log_transformed = c * np.log(1 + gray_image_array)

log_transformed = np.array(log_transformed, dtype=np.uint8)
log_image = Image.fromarray(log_transformed)

log_image.save('log_transformed_image.jpg')

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title('Original Grayscale Image')
axes[0].axis('off')

axes[1].imshow(log_image, cmap='gray')
axes[1].set_title('Log Transformed Image')
axes[1].axis('off')

plt.tight_layout()
plt.show()
