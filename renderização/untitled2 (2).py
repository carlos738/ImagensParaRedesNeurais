# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13mZp0MBqkDrbkmuA26-T46G-ci-cF-fp
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# carregar a imagem
img = cv2.imread('superhomem.jpg')
img = cv2.imread('mayshiranui.jpg')
img = cv2.imread('cheetara.jpg')
# converter de BGR para RGB (inverter os canais)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# converter para níveis de cinza
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar binarização com threshold 128
threshold_value = 128
_, img_binary = cv2.threshold(img_gray, threshold_value, 255, cv2.THRESH_BINARY)

# Exibir as imagens lado a lado
plt.figure(figsize=(12, 6))

# Imagem colorida
plt.subplot(1,3,1)
plt.imshow(img_rgb)
plt.title('Imagem Colorida')
plt.axis('off')

# imagens níveis de cinza
plt.subplot(1,3,2)
plt.imshow(img_gray, cmap='gray')
plt.title('Imagens em níveis de cinza')
plt.axis('off')

# imagem binarizada
plt.subplot(1,3,3)
plt.imshow(img_binary,cmap='gray')
plt.title('Imagem binarizada')
plt.axis('off')

plt.show()
