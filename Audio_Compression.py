# Audio Compression DCT

import numpy as np
import scipy.fftpack
import soundfile as sf
import matplotlib.pyplot as plt

# Author: Khaled Salama
# Project: Audio Compression using Discrete Cosine Transform (DCT)
""" Description: This project demonstrates a simple audio compression and decompression technique using the DCT.
 The process involves applying DCT to the audio signal,
 compressing the coefficients based on a compression ratio, and 
 then reconstructing the signal using the inverse DCT.
 """

def calculate_dct(signal):
    
    return scipy.fftpack.dct(signal, type=2, norm='ortho')

def calculate_idct(coefficients):
  
    return scipy.fftpack.idct(coefficients, type=2, norm='ortho')

# File paths
input_file_path = 'original_audio.wav'
compressed_output_path = 'compressed/compressed_audio.wav'
decompressed_output_path = 'uncompressed/decompressed_audio.wav'

# Compression ratio (adjust this value to control compression level)
compression_ratio = 0.50

# Load audio file using soundfile
audio_signal, sample_rate = sf.read(input_file_path, dtype='float32')

# Plot original signal
plt.figure(figsize=(10, 8))
plt.subplot(3, 1, 1)
plt.plot(audio_signal)
plt.title('Original Audio Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Apply DCT to the audio signal
dct_coefficients = calculate_dct(audio_signal)

# Determine the number of coefficients to retain based on the compression ratio
num_coefficients_to_retain = int(len(dct_coefficients) * compression_ratio)

# Retain the highest-energy coefficients
compressed_dct_coefficients = dct_coefficients[:num_coefficients_to_retain]
sf.write(compressed_output_path, compressed_dct_coefficients, sample_rate)

# Plot compressed signal
plt.figure(figsize=(10, 8))
plt.subplot(3, 1, 2)
plt.plot(compressed_dct_coefficients)
plt.title('COMPRESSED Audio Signal from DCT Coefficients')
plt.xlabel('Frequency (1/s=Hz)')
plt.ylabel('Amplitude')

# Restore the compressed DCT coefficients to the original DCT coefficients
restored_dct_coefficients = np.zeros_like(dct_coefficients)
restored_dct_coefficients[:len(compressed_dct_coefficients)] = compressed_dct_coefficients

# Perform IDCT on the restored coefficients
restored_signal = calculate_idct(restored_dct_coefficients)
sf.write(decompressed_output_path, restored_signal, sample_rate)

# Plot decompressed signal
plt.figure(figsize=(10, 8))
plt.subplot(3, 1, 3)
plt.plot(restored_signal)
plt.title('Decompressed Audio Signal from IDCT Coefficients')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
