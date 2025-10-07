import cv2
import numpy as np
import matplotlib.pyplot as plt

def median_filter(img, size):

    pad = size // 2
    padded_img = np.pad(img, pad, mode='edge')
    new_img = np.zeros_like(img)


    for i in range(img.shape[0]):
        for j in range(img.shape[1]):

            window = padded_img[i:i+size, j:j+size]

            median_val = np.median(window)

            new_img[i, j] = median_val

    return new_img


img = cv2.imread("images/noise.png")  # Update this path to your image location

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


filtered_img = median_filter(img, 3)



plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Median Filtered Image")
plt.imshow(filtered_img, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()