import numpy as np 
import cv2
from calulate_gradient import calculate_gradient
import matplotlib.pyplot as plt
import os

## Implementing Sobel Edge Detector
def sobel_edge_detector(img, threshold=100):
    grad_magnitude, grad_direction = calculate_gradient(img)

    edge_map = np.zeros_like(grad_magnitude)
    edge_map[grad_magnitude >= threshold] = 255

    return edge_map

## Load Image


sobel = cv2.imread("images/building.jpg")  # Update this path to your image location


sobel = cv2.cvtColor(sobel, cv2.COLOR_BGR2GRAY)
## Apply Sobel Edge Detector
sobel_map = sobel_edge_detector(sobel, threshold=100)

edges_canny = cv2.Canny(sobel, 100, 200)

plt.figure(figsize=(18, 6))
plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(sobel, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Sobel Edge Map")
plt.imshow(sobel_map, cmap='gray')
plt.axis('off')


plt.subplot(1, 3, 3)
plt.title("Canny Edge Map")
plt.imshow(edges_canny, cmap='gray')
plt.axis('off')


plt.tight_layout()
plt.show()
