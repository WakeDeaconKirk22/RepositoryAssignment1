import numpy as np 
import matplotlib.pyplot as plt

signal_frequency = 5  # Frequency of the original signal in Hz  
duration = 2 # Duration in seconds  
sampling_freqs = 8 # Different sampling frequencies in Hz 
num_bits = 3 # 
min_signal = -1
max_signal = 1

mean = 0
std_dev = 0.1

num_levels = 2 ** num_bits
n_samples = int(sampling_freqs * duration)

## Original Signal
def original_signal(t):
    return np.sin(2 * np.pi * signal_frequency * t)

## Quantize
def quantize(signal, num_bits, min_val, max_val):
    q_signal = np.round((signal - min_val) / (max_val - min_val) * (2**num_bits - 1))
    q_signal = np.clip(q_signal, 0, 2**num_bits - 1)  # Ensure values are within valid range
    q_values = min_val + q_signal * (max_val - min_val) / (2**num_bits - 1)

    return q_values

## Add Gaussian noise
def add_Gaussian_noise(signal, mean, std_dev):
    noise = np.random.normal(mean, std_dev, signal.shape)
    return signal + noise
## Compute Error Metrics
def computed_error(original, quantized):
    mean_squared_error = np.mean((original - quantized) ** 2)
    mean_squared_error = np.sqrt(mean_squared_error)
    max_val = np.max(np.abs(original - quantized))
    peak_signal_to_noise_ratio = 10 * np.log10(np.max(np.abs(original)) / max_val)
    return mean_squared_error, peak_signal_to_noise_ratio

#Continuous signal
t_count = np.linspace(0, duration, 1000)
t_sampled = np.linspace(0, duration, n_samples, endpoint=False)

signal_continuous = original_signal(t_count)
signal_sampled = original_signal(t_sampled)


#Noise to sampled signal
signal_noisy = add_Gaussian_noise(signal_sampled, mean, std_dev)
#Quantize the noisy signal
signal_quantized = quantize(signal_noisy, num_bits, min_signal, max_signal)


#Plot
plt.figure(figsize=(12, 6))
plt.plot(t_sampled,signal_sampled,'k-o',label='Original Sampled Signal')
plt.plot(t_sampled,signal_noisy,'g.-',label='Noisy Signal')
plt.step(t_sampled,signal_quantized,where='post',label='Quantized Signal ({num_bits} bits)',color='blue',linestyle = '--')


plt.title('Noisy Signal and Quantization')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()