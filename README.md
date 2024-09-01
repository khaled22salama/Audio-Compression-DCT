
# Audio Compression using Discrete Cosine Transform (DCT)

### Overview

This project demonstrates a simple audio compression and decompression technique using the Discrete Cosine Transform (DCT). The process involves applying DCT to an audio signal, compressing the coefficients based on a specified compression ratio, and then reconstructing the signal using the inverse DCT (IDCT).

### Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

### Introduction

Audio compression is a crucial aspect of digital audio processing, reducing file sizes while preserving sound quality. This project uses the Discrete Cosine Transform (DCT) to compress audio files by retaining only the most significant coefficients and reconstructing the signal with the inverse DCT. 

### Requirements

To run this project, you'll need the following:

- Python 3.x
- NumPy
- SciPy
- Matplotlib
- SoundFile

You can install the required packages using pip:

```bash
pip install numpy scipy matplotlib soundfile
```

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/khaled22salama/Audio-Compression-DCT.git
   cd audio-compression-dct
   ```
2. **Prepare Your Audio Files**:
   - Ensure you have an audio file named `original_audio.wav` in the project directory or update the file path in the script.

### Usage

1. **Run the Script**:
   ```bash
   python audio_compression_dct.py
   ```
   This will compress the `original_audio.wav` file using DCT, save the compressed version, and then decompress it.

2. **Adjust the Compression Ratio**:
   - The compression ratio can be adjusted by modifying the `compression_ratio` variable in the script (e.g., `compression_ratio = 0.50`).

### How It Works

1. **DCT (Discrete Cosine Transform)**:  
### Discrete Cosine Transform (DCT)

The **Discrete Cosine Transform (DCT)** is a mathematical technique used to transform a signal from the time domain to the frequency domain. It expresses a sequence of data points as a sum of cosine functions oscillating at different frequencies. The DCT is widely used in signal and image processing, particularly in compression algorithms, due to its energy compaction properties, meaning most of the signal's information tends to be concentrated in a few significant coefficients.

#### Why Use DCT for Audio Compression?

1. **Energy Compaction**: DCT has the ability to concentrate the most important information of the signal into a small number of coefficients. For audio signals, this property allows us to retain the most significant frequencies while discarding less important ones, thereby reducing the size of the data without greatly affecting the quality.
  
2. **Efficient Compression**: Unlike the Fourier Transform, the DCT produces only real coefficients (no imaginary parts), which simplifies storage and computation. Additionally, the DCT tends to produce fewer high-frequency components, making it more suitable for compressing audio signals where human perception is less sensitive to high frequencies.

3. **Minimizing Perceptual Loss**: Human hearing is less sensitive to higher frequency components. DCT takes advantage of this by allowing us to remove or reduce these components with minimal perceptual loss. This makes DCT an effective method for compressing audio without significantly impacting perceived sound quality.

#### How DCT Works

The DCT transforms an input signal into a sum of cosine functions at different frequencies. Mathematically, for an audio signal \( x[n] \) with \( N \) samples, the DCT of type-II is defined as:

\[
X[k] = \sum_{n=0}^{N-1} x[n] \cdot \cos \left( \frac{\pi}{N} \left( n + \frac{1}{2} \right) k \right) \quad \text{for } k = 0, 1, \ldots, N-1
\]

where:

- \( X[k] \) represents the DCT coefficient for frequency component \( k \).
- \( x[n] \) is the input audio signal at time \( n \).
- \( N \) is the total number of samples in the signal.

#### Inverse DCT (IDCT)

The Inverse DCT (IDCT) is used to convert the frequency domain representation back to the time domain, reconstructing the original signal from its DCT coefficients. The mathematical definition for the IDCT is:

\[
x[n] = \frac{1}{N} \left( X[0] + 2 \sum_{k=1}^{N-1} X[k] \cdot \cos \left( \frac{\pi}{N} \left( n + \frac{1}{2} \right) k \right) \right)
\]

where:

- \( x[n] \) is the reconstructed audio signal.
- \( X[k] \) are the DCT coefficients.

#### Application in the Project

In this project, the DCT is applied to the audio signal to transform it into the frequency domain. A compression ratio determines how many of the DCT coefficients are retained. By keeping only the most significant coefficients (those with the highest magnitude), we can compress the audio data effectively. The inverse DCT (IDCT) is then used to reconstruct the signal from the retained coefficients, yielding a compressed version of the original audio with reduced size but retained perceptual quality.

By leveraging the DCT, the project achieves a balance between compression efficiency and audio fidelity, making it a powerful tool for applications where storage or transmission bandwidth is limited.
   ```python
   def calculate_dct(signal):
       return scipy.fftpack.dct(signal, type=2, norm='ortho')
   ```

2. **Compression**:  
   The number of coefficients to retain is determined based on the compression ratio. Only the most significant coefficients are kept to achieve compression.

   ```python
   num_coefficients_to_retain = int(len(dct_coefficients) * compression_ratio)
   compressed_dct_coefficients = dct_coefficients[:num_coefficients_to_retain]
   ```

3. **IDCT (Inverse Discrete Cosine Transform)**:  
   The inverse DCT is applied to reconstruct the compressed audio signal back to the time domain.

   ```python
   def calculate_idct(coefficients):
       return scipy.fftpack.idct(coefficients, type=2, norm='ortho')
   ```

### Results

The script generates three plots:

1. **Original Audio Signal**:  
   Visualizes the original audio waveform.

2. **Compressed Audio Signal (DCT Coefficients)**:  
   Shows the compressed audio signal using retained DCT coefficients.

3. **Decompressed Audio Signal**:  
   Displays the reconstructed audio signal after applying IDCT.

### Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

