import cv2
import numpy as np
import matplotlib.pyplot as plt
from calulate_gradient import calculate_gradient

def directional_edge_detector(img, angle =45, tolerance=5 , threshold =100):
     grad_magnitude, grad_angle = calculate_gradient(img)
     lower = angle - tolerance
     upper = angle + tolerance

     mask = (grad_magnitude >= threshold) & ((grad_angle >= lower) & (grad_angle <= upper))

     edge_direction = np.zeros_like(grad_magnitude)
     edge_direction[mask] = 255

     return edge_direction









img = cv2.imread("images/building.jpg", cv2.IMREAD_GRAYSCALE)  

dir_map = directional_edge_detector(img, angle=45, tolerance=10, threshold=50)
edges_canny = cv2.Canny(img, 100, 200)


plt.figure(figsize=(18, 6))
plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Directional Edge Map")
plt.imshow(dir_map, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Canny Edge Map")
plt.imshow(edges_canny, cmap='gray')
plt.axis('off')



plt.tight_layout()
plt.show()


