from sinewave import Sinewave
from audio import Audio
from noise import Noise
import matplotlib.pyplot as plt
import simpleaudio as sa

sample_rate = 44100

#audio builder
audio_builder = Audio(sample_rate)

#build 80hz sine wave
sinewave_builder = Sinewave(80)
sinewave = sinewave_builder.build_waveform()
audio_builder.add_wave(sinewave)

#build 120hz sine wave
sinewave_builder.frequency = 120
sinewave = sinewave_builder.build_waveform()
#add noise
noise = Noise(0.005)
plt.plot(sinewave)
noisy_sinewave = noise.transform(sinewave)
plt.plot(noisy_sinewave)
plt.show()

audio_builder.add_wave(noisy_sinewave)

#build 160hz sine wave
sinewave_builder.frequency = 160
sinewave = sinewave_builder.build_waveform()
audio_builder.add_wave(sinewave)



final_audio = audio_builder.build_audio()
plt.plot(final_audio)
plt.title("Final Waveform")
plt.show()


play_obj = sa.play_buffer(final_audio, 1, 2, sample_rate)
play_obj.wait_done()

