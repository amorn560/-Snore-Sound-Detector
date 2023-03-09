import pyaudio
import wave
import os
import numpy as np
import matplotlib.pyplot as plt

# Set parameters for audio recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 30
save_path = os.path.join(os.path.expanduser('/home/amorn560/Desktop/pro'), 'MyPlots')
if not os.path.exists(save_path):
    os.makedirs(save_path)

exists = True
i = 1
while exists:
    if os.path.exists(f"recording_200Hz_{i}.wav"):
        i += 1
    else:
        exists = False
save_A = os.path.join(save_path, f"recording_200Hz_{i}.wav")
WAVE_OUTPUT_FILENAME = save_A

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open audio stream for recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording audio...")

# Create a buffer to store audio data
frames = []

# Record audio for the specified duration
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording audio.")

# Stop and close the audio stream
stream.stop_stream()
stream.close()
audio.terminate()

# Write the recorded audio to a WAV file
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

wav_obj = wave.open(WAVE_OUTPUT_FILENAME,'rb')

sample_freq = wav_obj.getframerate()


n_samples = wav_obj.getnframes()

t_audio = n_samples/sample_freq

n_channels = wav_obj.getnchannels()

signal_wave = wav_obj.readframes(n_samples)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)

l_channel = signal_array[0::1]
r_channel = signal_array[1::2]

times = np.linspace(0, n_samples/sample_freq, num=n_samples)



exists = True
x = 1
while exists:
    if os.path.exists(f"Waveform_200Hz_{x}.png"):
        x += 1
    else:
        exists = False


plt.figure(figsize=(15, 5))
plt.plot(times, l_channel)
plt.title('Waveform')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
save_fileA = os.path.join(save_path, f"Waveform_200Hz_{x}.png")
plt.savefig(save_fileA)
#plt.show()






plt.figure(figsize=(15, 5))
plt.specgram(l_channel, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('Spectogram')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.ylim(0, 2000)
plt.xlim(0, t_audio)
plt.colorbar()
save_fileB = os.path.join(save_path, f"Spectogram_200Hz_{x}.png")
plt.savefig(save_fileB)
#plt.show()


print("Audio saved to", WAVE_OUTPUT_FILENAME)

