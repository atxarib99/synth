import simpleaudio as sa
import numpy as np
import matplotlib.pyplot as plt

sample_rate = 44100
duration = 4.0  # Seconds
frequency = 80  # Hertz

t = np.linspace(0, duration, int(sample_rate * duration), False)
print("linspace")
print(t)
#tone = np.sin(frequency * t * 2 * np.pi)
t1 = np.linspace(0, duration/frequency, int(sample_rate * duration/frequency), False)
print(t1)
tone = t1
for i in range(0,frequency):
    tn = np.linspace(0, duration/frequency, int(sample_rate * duration/frequency), False)
    tone = np.append(tone,tn)

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
