import numpy as np
import matplotlib.pyplot as plt

##global variables
signal_frequency = 5  # Frequency of the original signal in Hz
duration = 2 # Duration in seconds
sampling_freq = 8
num_bit = 3
min_signal = -1
max_signal = 1

num_levels = 2 ** num_bit

##Plot original signal
def orignal_signal(t):
    return np.sin(2 * np.pi * signal_frequency * t)

##Continuous signal plot
t_points = np.linspace(0, duration, 1000)
cont_signal = orignal_signal(t_points)

plt.figure(figsize=(12, 6))
plt.plot(t_points, cont_signal, label= 'Continuous Signal')

##Sampling
n = int(sampling_freq * duration)
t_sampled = np.linspace(0, duration, n, endpoint=False)
sampled_signal = orignal_signal(t_sampled)
plt.plot(t_sampled, sampled_signal, 'o', label=f'Sampled Signal: {sampling_freq} Hz', color='orange')

## Quantize
def quantize(signal, num_bits, min_val, max_val):
    n = 2 ** num_bits
    q_signal = np.round((signal - min_val) / (max_val - min_val) * (n - 1))
    q_signal = np.clip(q_signal, 0, n - 1)  # Ensure values are within valid range
    return min_val + q_signal * (max_val - min_val) / (n - 1)

quantized_signal = quantize(sampled_signal, num_bit, min_signal, max_signal)

##Plotting 
plt.step(t_sampled,quantized_signal, where='post',label = 'Quantized Signal: {{num_bit} bits, {sampling_freq} Hz', color='blue')



plt.title('Signal Sampling and Quantization')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()   
plt.legend
plt.tight_layout()
plt.show()
