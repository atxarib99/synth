import simpleaudio as sa
import numpy as np
import matplotlib.pyplot as plt

sample_rate = 44100
duration = 1.0  # Seconds
frequency = 80  # Hertz

t = np.linspace(0, duration, int(sample_rate * duration), False)
print("linspace")
print(t)
plt.plot(t)
plt.title("wave")
plt.show()
tone = np.sin(frequency * t * 2 * np.pi)
print("tone")
print(tone)
plt.plot(tone)
plt.title("tone")
plt.show()
audio = tone * (2**15 - 1) / np.max(np.abs(tone))
audio = audio.astype(np.int16)
print("audio")
print(audio)
plt.plot(audio)
plt.title("audio")
plt.show()

play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
play_obj.wait_done()
