#%%
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def bit_plane_slicing(image):
    # Grayscale görüntüyü 8 bit düzlemi dilimlerine ayır
    bit_planes = []
    for i in range(8):
        bit_plane = (image >> i) & 1
        bit_planes.append(bit_plane * 255)  # Görselleştirme için 0 ve 255 arasında ölçekle
    return bit_planes

# Görüntüyü yükle ve gri seviyeye çevir
image_path = "./Week-4/Img3.jpg"
image = Image.open(image_path).convert('L')  # 'L' modu, grayscale (gri tonlama)
image_array = np.array(image)

# Bit düzlemi dilimleme
bit_planes = bit_plane_slicing(image_array)

# Görüntüleri göster
fig, axs = plt.subplots(2, 4, figsize=(16, 8))
for i in range(8):
    axs[i // 4, i % 4].imshow(bit_planes[i], cmap='gray')
    axs[i // 4, i % 4].set_title(f'Bit Plane {i}')
    axs[i // 4, i % 4].axis('off')

plt.tight_layout()
plt.show()
