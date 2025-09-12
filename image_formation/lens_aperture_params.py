import numpy as np
import matplotlib.pyplot as plt 
#A.)
def thin_lens(z0, f):
   return 1/(1/f -1/z0)
    



focal_length1= 3 # in mm
focal_length2= 9 # in mm
focal_length3=50
focal_length4 =200

z0_min =1.1
z0_max =104 # in mm
z0_point = 4

## Generate object distance values
z0_values = np.linspace(z0_min, z0_max, int((z0_max-z0_min)*z0_point))

## Plotting
plt.figure(figsize=(12, 8))
colors = ['r', 'g', 'b', 'm']
## Plot for each focal length
for f, color in zip([focal_length1, focal_length2, focal_length3, focal_length4], colors):
    z0 = z0_values[z0_values > f]
    zi = thin_lens(z0, f)
    plt.loglog(z0, zi, label=f'f={f}mm', color=color)
    plt.axvline(x=f, color=color, linestyle='--')


plt.xlabel('Object Distance z0 (mm)')
plt.ylabel('Image Distance zi (mm)')
plt.ylim([0,3000])
plt.title('Thin Lens Equation: Image Distance vs Object Distance')
plt.legend()
plt.tight_layout()
plt.show()

#B.)
# fnumbers 
f_numbers = [1.4,1.8,2.8,4.0]
#focal lengths 
f_values = np.linespace(20,650,500)


lens_examples = [(24,1.4, "24mm f/1.4"),(50,1.8,"50mm f/1.8"),(70,2.8,"85mm f/2.8"),(200,4.0,"200mm f/4.0") ,(400,2.8,"400mm f/2.8"),(600,4.0,"600mm f/4.0")]
for f_numbers,color in zip(f_numbers,colors):
    D = f_values/f_numbers
    plt.plot(f_values,D,label=f'f/{f_numbers}',color=color)


# Plot lens examples
for f,f_numbers,label in lens_examples:
     D = f/f_numbers
     plt.scatter(f,D,label=label,s=80,edgecolors='k')


plt.xlabel('Focal Length (mm)')
plt.ylabel('Aperture Diameter(mm)')
plt.title(': Aperture Diameter vs Focal Length')
plt.grid(True,linestyle='--',alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
