import cv2
import numpy as np
import matplotlib.pyplot as plt


def apply_convolution(image,kernel):
  #Odd
    k = kernel.shape[0]
    pad = k // 2
    height, width = image.shape
   

    padded_image = np.pad(image, pad, mode='constant', constant_values=0)
    output  = np.zeros((height, width), dtype=np.float32)
   
    for i in range(height):
        for j in range(width):
           region = padded_image[i:i+k, j:j+k]
           value = np.sum(region * kernel)
           output[i, j] = value
    return output


def calculate_gradient(img):
    ##Apply Sobel Kernels
    Sx = np.array([[-1, 0, 1],
                     [-2, 0, 2],
                     [-1, 0, 1]] , dtype=np.float32)
    
    Sy = np.array([[1, 2, 1],
                        [0, 0, 0],
                        [-1, -2, -1]] , dtype=np.float32)
    ##Convolve
    Gx = apply_convolution(img, Sx)

    Gy = apply_convolution(img, Sy)

   ## Gradient Magnitude
    grad_magnitude = np.sqrt(Gx**2 + Gy**2)
    grad_angle = np.arctan2(Gy, Gx) * (180.0 / np.pi)
   
    grad_magnitude = (grad_magnitude / grad_magnitude.max()) * 255
    grad_magnitude = grad_magnitude.astype(np.uint8)
    return grad_magnitude, grad_angle


img = cv2.imread("images/noise.png")  
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

grad_magnitude, grad_angle = calculate_gradient(img)



cv2.waitKey(0)
cv2.destroyAllWindows()

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Gradient Magnitude")
plt.imshow(grad_magnitude, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
