# RepositoryAssignment1

Transparency : Portions of the code was generated with Copilot then modified by me and commented to show understanding 

In this assignment we implement geometric translations in order to reverse enigneer an image that was given, we also manipulate lens apperture,sampling and quantization,and error/noise anaylsiy. It uses python scripts,libraries and images to help visualize each problem instance.


1.) Sample output
reverse engineered a series of 2d transformations to approximate a given transformed image from a original image. I used open cv for image manipultation and matplotlib to plot. Through this exercise I was able to understand and remember Translations matrices that was given in the book. I also found that the Skew Matrix in the x or y direction creates an almost 3d perspective that the transformed image gave. I also tried to apply the Affine matrix and found the same result of almost all my transformations but couldnt get it to center.

2.)
Exercise 1 plot the image distance as a function of object for various focal lengths using the thin lens equation.
Exercise 2 calculates aperture diameters required to achieve specific f number various real-world lenses.In this exercise i could visually see how image distance behaves near the focal length and this helped me better understand how my Canon Rebel XS hlens handles focusing. Additionally this gave me a clear sense of how f number affects exposure and depth of field. 

b.)
    24/1.4 = 17.14
    50/1.8 = 27.7
    70/2.8 = 25
    200/2.8 = 71.4
    400/2.8 = 142.85
    600/4.0 = 150


3. This exercise helped visualize the impact of undersampling and low bit quantization on signal accuracy. Undersampling show how inssuficient sampling rates can cause loss of detail aliasing, where the reconstructed signal no longer represents the original accurately. Low bit introduces noice and lowers signal expecially in areas with subtle changes.

What do you think a reasonable sampling frequency should be to capture the true shape of the
signal?:To find the true shape of a signal without distortion the Nyquist Shannon sampling theorem should be used. 
What should be done to minimize error?:
To minimize error increasng the sampling frequency and increasing the number of bits could help minimize error

4. Simulated real world sensor noise by adding Gaussian not to sinusodial signal. This helped understand how small amounts of noise can impact digital signals. I think the addition of Gaussian noise gives me more idea how thermal flucations, electronic interferene and cause randomness into the sensor data. Also this helped understand how noise distorts the signal shape which also make features harder to interpret.