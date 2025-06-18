from sinewave import Sinewave
from squarewave import Squarewave
from audio import Audio
from noise import Noise
from adsr import ADSR
import matplotlib.pyplot as plt
import simpleaudio as sa

sample_rate = 44100


#audio builder
audio_builder = Audio(sample_rate, loop=2)

aggressive_attack = ADSR(attack_duration=.1, decay_duration=.25, decay_min=.1, sustain_duration=.5, release_duration=.15)
slow_attack = ADSR(attack_duration=.9, decay_duration=.025, decay_min=.1, sustain_duration=0, release_duration=.075)
long_delay = ADSR(attack_duration=.1, decay_duration=.85, decay_min=.01, sustain_duration=0, release_duration=.05)

audio_builder.add_waves([
    Sinewave(80,1).add_transformation(Noise(0.005)),
    Sinewave(80,.25, 1),
    Sinewave(120,.25, 0.5),
    Sinewave(160,.25, 0.25),
    Sinewave(200,.25, 0.1),
    Sinewave(80,.25),
    Squarewave(120,.5, .1).add_transformation(aggressive_attack),
    Squarewave(160,.5, .1).add_transformation(aggressive_attack),
    Squarewave(200,.5, .1).add_transformation(aggressive_attack),
    Squarewave(80,.5, .1).add_transformation(aggressive_attack),
    Squarewave(120,.5, .1).add_transformation(slow_attack),
    Squarewave(160,.5, .1).add_transformation(slow_attack),
    Squarewave(200,.5, .1).add_transformation(slow_attack),
    Squarewave(80,.5, .1).add_transformation(slow_attack),
    Squarewave(120,.5, .1).add_transformation(long_delay),
    Squarewave(160,.5, .1).add_transformation(long_delay),
    Squarewave(200,.5, .1).add_transformation(long_delay),
    Squarewave(80,.5, .1).add_transformation(long_delay),
    Squarewave(120,.25, .1),
    Squarewave(160,.25, .1),
    Squarewave(200,.25, .1),
    Squarewave(80,.25, .1),
    Sinewave(120,.25).add_transformation(ADSR()),
    Sinewave(160,.25).add_transformation(ADSR()),
    Sinewave(200,.25).add_transformation(ADSR()),
    Sinewave(80,.25).add_transformation(ADSR()),
    Sinewave(120,.25),
    Sinewave(160,.25),
    Sinewave(200,.25),
    Sinewave(80,1)
])

audio_builder.add_transformation(Noise(0.002))


final_audio = audio_builder.build_audio()

plt.plot(final_audio)
plt.show()

play_obj = sa.play_buffer(final_audio, 1, 2, sample_rate)
play_obj.wait_done()

