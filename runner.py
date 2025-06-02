from sinewave import Sinewave
from audio import Audio
from noise import Noise
import matplotlib.pyplot as plt
import simpleaudio as sa

sample_rate = 44100


#audio builder
audio_builder = Audio(sample_rate)

audio_builder.add_waves([
    Sinewave(80,1).add_transformation(Noise(0.005)),
    Sinewave(80,.25),
    Sinewave(120,.25),
    Sinewave(160,.25),
    Sinewave(200,.25),
    Sinewave(80,.25),
    Sinewave(120,.25),
    Sinewave(160,.25),
    Sinewave(200,.25),
    Sinewave(80,.25),
    Sinewave(120,.25),
    Sinewave(160,.25),
    Sinewave(200,.25),
    Sinewave(80,.25),
    Sinewave(120,.25),
    Sinewave(160,.25),
    Sinewave(200,.25),
    Sinewave(80,1)
])

audio_builder.add_transformation(Noise(0.005))


final_audio = audio_builder.build_audio()

play_obj = sa.play_buffer(final_audio, 1, 2, sample_rate)
play_obj.wait_done()

