

##RepiositoryAssignment2

1.) For Exercise 1 we peformed techniques to strech and redistribute pixels intensitities to enhance 
the image. The first function I was able to learn about how point wise operations apply here it transform each pixels intensity values independenlty of its neighbors. In the next function I also learned how to calculate for histogram and how linearity is applied to histogram equalization by distrubuting intensity values linearly similar to contrast streching. When applied I noticed the outputs were similar. 

Outputs: 
<img width="1440" height="600" alt="Contrast_Stretech" src="https://github.com/user-attachments/assets/fdc1f709-4cb4-4fc8-ba83-00e17bf04c33" />

<img width="1440" height="600" alt="HistogramofEqualization" src="https://github.com/user-attachments/assets/ad230380-a613-4cd0-9235-2ea69c82e3a2" />


2.) For Excercise 2 I implemneted median filter and the fundamental operator for edge detection. I learned here the difference between linear functions vs non linear functions. For example the median function sorts and selects a middle value from the pixel window while a linear function sums the pixel values. I also found that a median filter gets rid of salt and pepper noise really well compared to the gaussian filter. I also found that median filter performs better because it is more resistant to outliers than a linear filter because linear filters are easily skewed by outlier pixels. 
"What is the effect of median filtering on the calculation of gradient magnitude of an
image corrupted by salt-and-pepper noise? Use your code to answer this question" . To answer this the gradient magnitude measures changes in intensity so if the image is noisey it would cause false large gradients. When applying the median filter is applied as mentioned before it removes outliers which reduces the influence of gradient magnitude calculation.

Outputs: 
<img width="1200" height="600" alt="MedianFilter" src="https://github.com/user-attachments/assets/cdccc87d-a167-4fca-91f5-43e67e7880e5" />

<img width="1200" height="600" alt="CalculateGradient" src="https://github.com/user-attachments/assets/d4df5619-7e0b-40df-807e-f8d5825afd74" />




3.) For exercise 3 I  explored how to extend the gradient direction. For sobel edge detector I found it produeces strong edges while directional edge detects edges in a specfic orientation. although for the directional edge detetector i found there is more noise picked up rhan the sobel edge detector.

Outputs: 
<img width="1440" height="600" alt="SobelEdge" src="https://github.com/user-attachments/assets/21ccc932-61a6-4330-881a-8d2516a653a5" />

<img width="1440" height="600" alt="DirectionalEdgeMap" src="https://github.com/user-attachments/assets/b4b4c36f-7b14-46c0-bfd9-5fc6eb26a153" />


