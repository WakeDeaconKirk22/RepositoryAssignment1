import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#Reod the original and transformed images

img = cv.imread("images/original_image.jpg")
img2 = cv.imread("images/transformed_image.jpg")


# Peform a rotation
rows,cols = img.shape[:2]

# Perform a translation
M = np.float32([[1,0,0],[0,1,0]]) # Translate by (50, 50)
dst = cv.warpAffine(img,M,(cols,rows))
# Rotate by 18 degrees around the center
M = cv.getRotationMatrix2D((cols/2,rows/2),16,.63) 
rotation = cv.warpAffine(img,M,(cols  ,rows ))
## Perform a skew in X direction
skew_X= np.float32([[1, .38, 0], [0, .95, 0]])
skew_img = cv.warpAffine(rotation,skew_X,(cols,rows))
## peform a skew in Y direction
skew_Y = np.float32([[1, 0, 0], [1.1, 1, 0]])
M_2 = cv.warpAffine(skew_img,skew_Y,(cols * 2,rows * 2))

shift = np.float32([[1, 0, 0], [0, 1, -555]])
translated_img = cv.warpAffine(M_2,shift,(cols * 1,rows * 1))

#Need to convert BGR to RGB for matplotlib

img_rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
img2_rgb = cv.cvtColor(img2,cv.COLOR_BGR2RGB)
transformed_img_rgb = cv.cvtColor(translated_img,cv.COLOR_BGR2RGB)

#Use matplotlib to display the images

plt.figure(figsize=(24,6))
plt.subplot(1,3,1)
plt.title("Original Image")
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(1,3,2)
plt.title("Transformed Image")
plt.imshow(transformed_img_rgb)
plt.axis('off')



plt.subplot(1,3,3)
plt.title("Reference Image")
plt.imshow(img2_rgb)
plt.axis('off')


plt.show()


print("\nTransformation Matrix for Rotation:")
print("Rotation Matrix:\n", M)
print("\nTransformation Matrix for Shear in X direction:",skew_X)
print("\nTransformation Matrix for Shear in Y direction:",skew_Y)
print("\nTransformation Matrix for Translation:",shift)