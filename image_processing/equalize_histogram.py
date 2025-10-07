import cv2
import numpy as np
import matplotlib.pyplot as plt


def equalize_histogram(img):
    flat = img.ravel()
    
    hist, bins = np.histogram(flat, bins=256, range=[0, 256])
     ##Normalize
    probability = hist / hist.sum()
    ## Compute cdf 
    cumulative_distribution = np.cumsum(probability)

    cumlative_scaled = np.floor(255 * cumulative_distribution).astype(np.uint8)

    new_img = cumlative_scaled[flat].reshape(img.shape)

    return new_img

##Reead
img = cv2.imread("images/image.png")  # Update this path to your image location

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##apply histogram 
equalized_img = equalize_histogram(img)
##show images side by side



##Plot histograms
plt.figure(figsize=(24, 6))

plt.subplot(1, 4, 1)
plt.hist(img.ravel(), bins=256, range=[0, 256], color='black', alpha=0.5, label='Original Image')
plt.title('Histogram of Original Image')
plt.legend()


plt.subplot(1, 4, 2)
plt.hist(equalized_img.ravel(), bins=256, range=[0, 256], color='blue', alpha=0.5, label='Equalized Image')
plt.title('Histogram of Equalized Image')
plt.legend()


plt.subplot(1, 4, 3)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')


plt.subplot(1, 4, 4)
plt.imshow(equalized_img, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.tight_layout()
plt.show()


cv2.waitKey(0)



cv2.destroyAllWindows()


