import numpy as np
from scipy.io.wavfile import write
from scipy import signal
import matplotlib.pyplot as plt

#------------------------------ 1 ---------------------------------
# Parameters
fs = 44100         # Sampling frequency
duration = 5       # seconds
f1 = 440           # Frequency of left channel (square)
f2 = 480           # Frequency of right channel (sawtooth)
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Generate waveforms
left = signal.square(2 * np.pi * f1 * t)
right = signal.sawtooth(2 * np.pi * f2 * t)

# Normalize to range [-1, 1]
stereo = np.stack((left, right), axis=-1)

# Save as int16
write("stereo_int16.wav", fs, (stereo * 32767).astype(np.int16))

# Save as uint8 (range [0, 255])
stereo_uint8 = ((stereo + 1) / 2 * 255).astype(np.uint8)
write("stereo_uint8.wav", fs, stereo_uint8)

#------------------------------ 1b ---------------------------------

def calculate_audio_info(fs, duration, channels, bit_depth):
    bytes_per_sample = bit_depth // 8
    total_samples = int(fs * duration)
    total_bytes = total_samples * channels * bytes_per_sample
    bitrate = fs * channels * bit_depth
    return total_bytes, bitrate

size_int16, bitrate_int16 = calculate_audio_info(44100, 5, 2, 16)
size_uint8, bitrate_uint8 = calculate_audio_info(44100, 5, 2, 8)

print(f"\nINT16: File size = {size_int16/1024:.2f} KB, Bitrate = {bitrate_int16} bps")
print(f"UINT8: File size = {size_uint8/1024:.2f} KB, Bitrate = {bitrate_uint8} bps")


#------------------------------ 2 ---------------------------------
def generate_melody(waveform_type, freqs, durations, fs=44100):
    melody = np.array([], dtype=np.float32)
    for f, d in zip(freqs, durations):
        t = np.linspace(0, d, int(fs * d), endpoint=False)
        if waveform_type == 'sine':
            wave = np.sin(2 * np.pi * f * t)
        elif waveform_type == 'square':
            wave = signal.square(2 * np.pi * f * t)
        elif waveform_type == 'sawtooth':
            wave = signal.sawtooth(2 * np.pi * f * t)
        elif waveform_type == 'triangular':
            wave = signal.sawtooth(2 * np.pi * f * t, width=0.5)
        melody = np.concatenate((melody, wave))
    return melody

# User-defined melody
frequencies = [440, 500, 830]
durations = [3, 5, 6]
melody = generate_melody('triangular', frequencies, durations)

# Save as WAV
write("melody.wav", 44100, (melody * 32767).astype(np.int16))


#------------------------------ 3 ---------------------------------
# Generate waveforms
duration = 1
t = np.linspace(0, duration, fs, endpoint=False)

waveforms = {
    "Square": signal.square(2 * np.pi * 440 * t),
    "Sawtooth": signal.sawtooth(2 * np.pi * 440 * t),
    "Triangular": signal.sawtooth(2 * np.pi * 440 * t, width=0.5)
}

# Plot FFTs
plt.figure(figsize=(12, 8))
for i, (name, wave) in enumerate(waveforms.items()):
    fft_vals = np.fft.fft(wave)
    fft_freq = np.fft.fftfreq(len(fft_vals), 1/fs)
    magnitude = np.abs(fft_vals[:fs//2])

    plt.subplot(3, 1, i+1)
    plt.plot(fft_freq[:fs//2], magnitude)
    plt.title(f"{name} Wave FFT")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.grid(True)

plt.tight_layout()
plt.show()