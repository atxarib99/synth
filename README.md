# synth

synth is a little music project i've been working on that allows the user to work with music kinda in raw. user gets to create the waves, perform transformations to achieve their desired sound, and then play it their created track!

## class structure
### waveforms
waveforms are the baseplate of the sound. this is the unadulterated sound wave that should be played. this can be something like a sinewave or a squarewave depending on the sound desired.
#### sinewave
a nice, smooth, and wavy waveform!
#### squarewave
a fun, boxy, and aggressive waveform! warning its a bit loud!
#### saw wave (to come soon!)
#### write your own!

### transformations
transformations are effects to be added to the original waveform. these are changes that should be applied.
#### noise
a simple gaussion noise that applies white noise to the wave
#### adsr
attack, decay, sustain, release. the durations are changed with percentages as decimals (.25, .5) this modulates the volume to make a wubby sound. make it aggressive with an small attack duration value, or have it slowly increase with a large value. decay is where the sound should settle to. sustain is how long, as a percentage, to sustain that volume. lastly, release is the amount of time in which to bring the volume to 0
#### 8 bit! (to come soon!)
#### write your own!

### audio
the final holding cell of the track. this will normalize and tranform the audio into a playable track
#### audio level transformation
transformation can be added at the audio level which will apply to all waveforms, on top of transformation already added to independent waveforms. 
#### loop the track
how many times to loop the track

## installation 
simply run
```
pip install -r requirements.txt
python runner.py
```
## how-to
see runner.py as an example on how to build a playable sound as well as view it on a plot