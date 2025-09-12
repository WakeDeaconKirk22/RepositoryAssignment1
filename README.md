# RepositoryAssignment1

In this assignment we implement geometric translations in order to reverse enigneer an image that was given, we also manipulate lens apperture,sampling and quantization,and error/noise anaylsiy. It uses python scripts,libraries and images to help visualize each problem instance.


1.) Sample output
reverse engineered a series of 2d transformation to approximate a given transformed image from a original image. I used open cv for image manipultation and matplotlib to plot.

2.)
Exercise 1 plot the image distance as a function of object for various focal lengths using the thin lens equation.
Exercise 2 calculates aperture diameters required to achieve specific f number various real-world lenses.

b.)
 24/1.4 =
    50/1.8
    70/2.8
    200/2.8
    400/2.8
    600/4.0


3. This exercise help visualize the impact of undersampling and low bit quantization on signal accuracy. U


To find the true shape of a signal without distortion the Nyquist Shannon sampling theorem should be used. To minimize error increasng the sampling frequency and increasing the number of bits could help minimize error

4. Simulated real world sensor noise by adding Gaussian not to sinusodial signal. This helped understand how small amounts of noise can impact digital signal