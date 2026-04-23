#pull in the waveforms, tranformations, and audio track
from sinewave import Sinewave
from squarewave import Squarewave
from track import Track
from audio import Audio
from noise import Noise
from adsr import ADSR

#plotting library
import matplotlib.pyplot as plt

#library to actually play the sound
import simpleaudio as sa

#fixed sample rate for now, dont change this, i didnt implement that yet,
sample_rate = 44100


#track one
track_one = Track()

#some tranformations created beforehand so that we can reuse them
aggressive_attack = ADSR(attack_duration=.1, decay_duration=.25, decay_min=.1, sustain_duration=.5, release_duration=.15)
slow_attack = ADSR(attack_duration=.9, decay_duration=.025, decay_min=.1, sustain_duration=0, release_duration=.075)
long_delay = ADSR(attack_duration=.1, decay_duration=.85, decay_min=.01, sustain_duration=0, release_duration=.05)

#add waves to the track!
track_one.add_waves([
    Sinewave(80, .5, 0.0001).add_transformation(Noise(0.1)).add_transformation(aggressive_attack),
    Sinewave(80, .5, 0.0001).add_transformation(Noise(0.1)).add_transformation(aggressive_attack),
    Sinewave(80, .5, 0.0001).add_transformation(Noise(0.1)).add_transformation(aggressive_attack),
    Sinewave(80, .5, 0.0001).add_transformation(Noise(0.1)).add_transformation(aggressive_attack),
    Sinewave(80, 1, 0), # this super quite section just offsets the rest of the track
])

track_two = Track(loop=2)
track_two.add_waves([
    Sinewave(80, .25, 0), # this super quite section just offsets the rest of the track
    Sinewave(80, .5, 0.0001).add_transformation(Noise(0.1)).add_transformation(aggressive_attack),
    Sinewave(80, .5, 0.0001).add_transformation(Noise(0.1)).add_transformation(aggressive_attack),
    Sinewave(80, .5, 0.0001).add_transformation(Noise(0.1)).add_transformation(aggressive_attack),
    Sinewave(80, .5, 0.0001).add_transformation(Noise(0.1)).add_transformation(aggressive_attack),
    Sinewave(80, .75, 0), # this super quite section just offsets the rest of the track
])

#build the final audio
final_audio = Audio(sample_rate)
final_audio.add_tracks([track_one, track_two])
final_audio = final_audio.build_audio()

#plot the final audio so you can see your creation!
plt.plot(final_audio)
plt.show()

#play the fuckin track!
play_obj = sa.play_buffer(final_audio, 1, 2, sample_rate)
play_obj.wait_done()

