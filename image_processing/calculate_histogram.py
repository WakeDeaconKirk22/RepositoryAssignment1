import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2

def calulate_histogram(img, bins):

    flat = img.flatten()

    counts, bin_edges = np.histogram(flat, bins=bins, range=(0, 256))
    dist = counts / counts.sum() ##normalized distrubution
    return counts, dist


#Read in grayscale
img = cv2.imread("images/image.png")  # Update this path to your image location

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

counts, dist = calulate_histogram(img, bins=256)




plt.figure(figsize=(10, 5))

##Histogram
plt.subplot(1, 2, 1)
plt.bar(range(256), counts, width=1.0, color='black')
plt.title('Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

##Normalized Histogram
plt.subplot(1, 2, 2)
plt.bar(range(256), dist, width=1.0, color='blue')
plt.title('Normalized Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Probability')
plt.ylim(0,dist.max()*1.1)

plt.tight_layout()
plt.show()
