from sinewave import Sinewave
from audio import Audio
from noise import Noise
import matplotlib.pyplot as plt
import simpleaudio as sa

sample_rate = 44100

sinewave_builder = Sinewave(80, 1.0)
sinewave_one_long = sinewave_builder.build_waveform()
sinewave_builder = Sinewave(80, 0.25)
sinewave_one_short = sinewave_builder.build_waveform()

sinewave_builder = Sinewave(120, 0.25)
sinewave_two = sinewave_builder.build_waveform()
sinewave_builder = Sinewave(160, 0.25)
sinewave_three = sinewave_builder.build_waveform()
noise = Noise(0.01)
sinewave_three = noise.transform(sinewave_three)

sinewave_builder = Sinewave(200, 0.25)
sinewave_four = sinewave_builder.build_waveform()

plt.plot(sinewave_four)
plt.plot(sinewave_two)
plt.show()

#audio builder
audio_builder = Audio(sample_rate)

audio_builder.add_wave(sinewave_one_long)

audio_builder.add_wave(sinewave_one_short)
audio_builder.add_wave(sinewave_two)
audio_builder.add_wave(sinewave_three)
audio_builder.add_wave(sinewave_four)
audio_builder.add_wave(sinewave_one_short)
audio_builder.add_wave(sinewave_two)
audio_builder.add_wave(sinewave_four)
audio_builder.add_wave(sinewave_three)
audio_builder.add_wave(sinewave_one_short)
audio_builder.add_wave(sinewave_two)
audio_builder.add_wave(sinewave_four)
audio_builder.add_wave(sinewave_three)
audio_builder.add_wave(sinewave_one_short)
audio_builder.add_wave(sinewave_two)
audio_builder.add_wave(sinewave_four)
audio_builder.add_wave(sinewave_three)

audio_builder.add_wave(sinewave_one_long)


final_audio = audio_builder.build_audio()
plt.plot(final_audio)
plt.title("Final Waveform")
plt.show()


play_obj = sa.play_buffer(final_audio, 1, 2, sample_rate)
play_obj.wait_done()

