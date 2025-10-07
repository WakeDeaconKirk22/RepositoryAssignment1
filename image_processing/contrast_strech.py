import cv2
import numpy as np
import matplotlib.pyplot as plt


def contrast_strech(img , r_min, r_max):

    img = img.astype(np.float32)
   #apply contrast strech formula
    streched_img = (img - r_min) * (255 / (r_max - r_min))

    streched_img = np.clip(streched_img, 0, 255)

    return streched_img.astype(np.uint8)



##load image
img = cv2.imread("images/image.png")  # Update this path to your image location

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#get min and max pixel values
r_min , r_max = np.min(img) , np.max(img)
##apply contrast strech
new_img = contrast_strech(img , r_min, r_max)

##show images side by side


#plot histograms
plt.figure(figsize=(24, 6))

plt.subplot(1, 4, 1)
plt.hist(img.ravel(), bins=256, range=[0, 256], color='black', alpha=0.5, label='Original Image')
plt.title('Histogram of Original Image')



plt.subplot(1, 4, 2)
plt.hist(new_img.ravel(), bins=256, range=[0, 256], color='blue', alpha=0.5, label='Contrast Stretched Image')
plt.title('Histogram of Contrast Stretched Image')

plt.subplot(1, 4, 3)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 4, 4)
plt.imshow(new_img, cmap='gray')
plt.title('Contrast Stretched Image')

plt.show()






cv2.waitKey(0)

cv2.destroyAllWindows()
