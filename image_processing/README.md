

##RepiositoryAssignment2

1.) For Exercise 1 we peformed techniques to strech and redistribute pixels intensitities to enhance the image. The first function I was able to learn about how point wise operations apply here it transform each pixels intensity values independenlty of its neighbors. In the next function I also learned how to calculate for histogram and how linearity is applied to histogram equalization by distrubuting intensity values linearly similar to contrast streching. When applied I noticed the outputs were similar. 



2.) For Excercise 2 I implemneted median filter and the fundamental operator for edge detection. I learned here the difference between linear functions vs non linear functions. For example the median function sorts and selects a middle value from the pixel window while a linear function sums the pixel values. I also found that a median filter gets rid of salt and pepper noise really well compared to the gaussian filter. I also found that median filter performs better because it is more resistant to outliers than a linear filter because linear filters are easily skewed by outlier pixels. 
"What is the effect of median filtering on the calculation of gradient magnitude of an
image corrupted by salt-and-pepper noise? Use your code to answer this question" . To answer this the gradient magnitude measures changes in intensity so if the image is noisey it would cause false large gradients. When applying the median filter is applied as mentioned before it removes outliers which reduces the influence of gradient magnitude calculation.



3.) For exercise 3 I  explored how to extend the gradient direction. For sobel edge detector I found it produeces strong edges while directional edge detects edges in a specfic orientation.
