# RepositoryAssignment1

Transparency : Portions of the code was generated with Copilot then modified by me and commented to show understanding 

In this assignment we implement geometric translations in order to reverse enigneer an image that was given, we also manipulate lens apperture,sampling and quantization,and error/noise anaylsiy. It uses python scripts,libraries and images to help visualize each problem instance.


<<<<<<< HEAD
1.) 
Output Image:
<img width="1440" height="600" alt="Transformations Output" src="https://github.com/user-attachments/assets/71d65bfa-c618-4c66-8f1c-85fddf0b84a8" />

=======
1.) Sample output
>>>>>>> ac2e3d5 (Edited lens_aperture_params.py to fix bug)
reverse engineered a series of 2d transformations to approximate a given transformed image from a original image. I used open cv for image manipultation and matplotlib to plot. Through this exercise I was able to understand and remember Translations matrices that was given in the book. I also found that the Skew Matrix in the x or y direction creates an almost 3d perspective that the transformed image gave. I also tried to apply the Affine matrix and found the same result of almost all my transformations but couldnt get it to center.

2.)
Output Image:
<img width="1000" height="600" alt="Thin_Lens_Equation" src="https://github.com/user-attachments/assets/15982930-ed01-4863-8aaa-752ffcca397d" />


Exercise 1 plot the image distance as a function of object for various focal lengths using the thin lens equation.
Exercise 2 calculates aperture diameters required to achieve specific f number various real-world lenses.In this exercise i could visually see how image distance behaves near the focal length and this helped me better understand how my Canon Rebel XS hlens handles focusing. Additionally this gave me a clear sense of how f number affects exposure and depth of field. 

b.)
    24/1.4 = 17.14
    50/1.8 = 27.7
    70/2.8 = 25
    200/2.8 = 71.4
    400/2.8 = 142.85
    600/4.0 = 150


<<<<<<< HEAD
3.
Output Image:

<img width="1200" height="600" alt="Sampling and Quantization" src="https://github.com/user-attachments/assets/dd3df508-585f-4d9a-bdde-2560f4d7de71" />

 This exercise helped visualize the impact of undersampling and low bit quantization on signal accuracy. Undersampling show how inssuficient sampling rates can cause loss of detail aliasing, where the reconstructed signal no longer represents the original accurately. Low bit introduces noice and lowers signal expecially in areas with subtle changes.

What do you think a reasonable sampling frequency should be to capture the true shape of the
signal?:To find the true shape of a signal without distortion the Nyquist Shannon sampling theorem should be used. 
What should be done to minimize error?:
To minimize error increasng the sampling frequency and increasing the number of bits could help minimize error

<<<<<<< HEAD:README.md
4.
Output Image:
<img width="1200" height="600" alt="Noisy Signal and Quantization" src="https://github.com/user-attachments/assets/75379b74-fb78-469f-99d4-c21c2d00d06a" />
=======
3. This exercise helped visualize the impact of undersampling and low bit quantization on signal accuracy. Undersampling show how inssuficient sampling rates can cause loss of detail aliasing, where the reconstructed signal no longer represents the original accurately. Low bit introduces noice and lowers signal expecially in areas with subtle changes.
>>>>>>> ac2e3d5 (Edited lens_aperture_params.py to fix bug)

What do you think a reasonable sampling frequency should be to capture the true shape of the
signal?:To find the true shape of a signal without distortion the Nyquist Shannon sampling theorem should be used. 
What should be done to minimize error?:
To minimize error increasng the sampling frequency and increasing the number of bits could help minimize error

<<<<<<< HEAD
  Simulated real world sensor noise by adding Gaussian not to sinusodial signal. This helped understand how small amounts of noise can impact digital signals. I think the addition of Gaussian noise gives me more idea how thermal flucations, electronic interferene and cause randomness into the sensor data. Also this helped understand how noise distorts the signal shape which also make features harder to interpret.
=======
4. Simulated real world sensor noise by adding Gaussian not to sinusodial signal. This helped understand how small amounts of noise can impact digital signals. I think the addition of Gaussian noise gives me more idea how thermal flucations, electronic interferene and cause randomness into the sensor data. Also this helped understand how noise distorts the signal shape which also make features harder to interpret.
>>>>>>> ac2e3d5 (Edited lens_aperture_params.py to fix bug)
=======
4. Simulated real world sensor noise by adding Gaussian not to sinusodial signal. This helped understand how small amounts of noise can impact digital signals. I think the addition of Gaussian noise gives me more idea how thermal flucations, electronic interferene and cause randomness into the sensor data. Also this helped understand how noise distorts the signal shape which also make features harder to interpret.



##RepiositoryAssignment2

1.) For Exercise 1 we peformed techniques to strech and redistribute pixels intensitities to enhance the image. The first function I was able to learn about how point wise operations apply here it transform each pixels intensity values independenlty of its neighbors. In the next function I also learned how to calculate for histogram and how linearity is applied to histogram equalization by distrubuting intensity values linearly similar to contrast streching. When applied I noticed the outputs were similar. 



2.) For Excercise 2 I implemneted median filter and the fundamental operator for edge detection. I learned here the difference between linear functions vs non linear functions. For example the median function sorts and selects a middle value from the pixel window while a linear function sums the pixel values. I also found that a median filter gets rid of salt and pepper noise really well compared to the gaussian filter. I also found that median filter performs better because it is more resistant to outliers than a linear filter because linear filters are easily skewed by outlier pixels. 
"What is the effect of median filtering on the calculation of gradient magnitude of an
image corrupted by salt-and-pepper noise? Use your code to answer this question" . To answer this the gradient magnitude measures changes in intensity so if the image is noisey it would cause false large gradients. When applying the median filter is applied as mentioned before it removes outliers which reduces the influence of gradient magnitude calculation.



3.) For exercise three we explored how to extend the gradient direction. For sobel edge detector I found it produeces strong edges while directional edge detects edges in a specfic orientation. 



>>>>>>> ffa19bf (Added image processing scripts and sample images):image_processing/README.md
