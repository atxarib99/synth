#pull in the waveforms, tranformations, and audio track
from sinewave import Sinewave
from squarewave import Squarewave
from audio import Audio
from noise import Noise
from adsr import ADSR

#plotting library
import matplotlib.pyplot as plt

#library to actually play the sound
import simpleaudio as sa

#fixed sample rate for now, dont change this, i didnt implement that yet,
sample_rate = 44100


#audio builder
audio_builder = Audio(sample_rate, loop=2)

#some tranformations created beforehand so that we can reuse them
aggressive_attack = ADSR(attack_duration=.1, decay_duration=.25, decay_min=.1, sustain_duration=.5, release_duration=.15)
slow_attack = ADSR(attack_duration=.9, decay_duration=.025, decay_min=.1, sustain_duration=0, release_duration=.075)
long_delay = ADSR(attack_duration=.1, decay_duration=.85, decay_min=.01, sustain_duration=0, release_duration=.05)

#add waves to the track!
audio_builder.add_waves([
    Sinewave(80,1).add_transformation(Noise(0.005)), # an 80hz sinewave that plays for 1 second, with some noise added. 
    Sinewave(80,.25, 1), #a shorter 80hz sinewave, that only plays for a quarter second, at full volume
    Sinewave(120,.25, 0.5), #a shorter 80hz sinewave, that only plays for a quarter second, at half volume
    Sinewave(160,.25, 0.25),
    Sinewave(200,.25, 0.1),
    Sinewave(80,.25),
    Squarewave(120,.5, .1).add_transformation(aggressive_attack), # a 120hz squarewave that plays for 1/2 second, at 1/10th volume (squarewave are loud!), with an aggressive attack ADSR
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
    Squarewave(120,.25, .1), #a 120hz square wave, 1/4 second duration, 1/10th volume, no transformations
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

# add noise to the whole track
audio_builder.add_transformation(Noise(0.002))

#build the final audio
final_audio = audio_builder.build_audio()

#plot the final audio so you can see your creation!
plt.plot(final_audio)
plt.show()

#play the fuckin track!
play_obj = sa.play_buffer(final_audio, 1, 2, sample_rate)
play_obj.wait_done()

