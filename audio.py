from waveform_validator import WaveformValidator
from waveform import Waveform
import numpy as np

class Audio:
    def __init__(self, sample_rate, loop=0) -> None:
        self.wave = None
        self.tracks = []
        self.transformations = []
        self.sample_rate = sample_rate
        self.loop = loop

    def add_track(self, track) -> None:
        self.tracks.append(track)

    def add_tracks(self, tracks):
        for track in tracks:
            self.tracks.append(track)

    def add_transformation(self, transformation):
        self.transformations.append(transformation)

    def add_transformations(self, transformations: list):
        for transformation in transformations:
            self.transformations.append(transformation)

    def build_audio(self):

        # holds final waves for each track
        final_waves = []

        # for each track, build waves into a single object
        for track in self.tracks:
            count = 0
            final_wave = np.linspace(0,0,0)
            # loop the track as specified.
            for i in range(0, track.loop):
                for wave in track.waves:
                    count += 1
                    #if its of type Waveform, build it
                    if isinstance(wave, Waveform):
                        #TODO: validate each part independently
                        final_wave = np.append(final_wave, wave.build())
                    elif isinstance(wave, np.ndarray):
                        #TODO: validate each part independently
                        final_wave = np.append(final_wave, wave)
                    else:
                        print("Invalid wave type found during building at position:" + str(count))

            # save this final_wave
            final_waves.append(final_wave)

        # all final_waves need to be same length
        # find longest wave
        longest_wave_len = len(max(final_waves, key=lambda x: len(x)))

        # for each wave, if wave not long enough, add length to end.
        index = 0
        while index < len(final_waves):
            if len(final_waves[index]) < longest_wave_len:
                final_waves[index] = np.append(final_waves[index], np.linspace(0,0,longest_wave_len - len(final_waves[index])))
            index += 1

        # waveform addition all tracks together
        for wave in final_waves:
            if self.wave is None:
                self.wave = wave
            else:
                self.wave = self.wave + wave


        #apply audio level transforms
        for transformation in self.transformations:
            self.wave = transformation.transform(self.wave)

        #validate waveform
        validator = WaveformValidator(self.sample_rate)
        if not validator.validate_wave(self.wave):
            print("Invalid wave!")
            exit(1)


        #convert audio to 16-bit audio
        #normalize wave again. Waves are normalized, but audio scope transformation may invalidate
        audio = self.wave * (2**15 - 1)
        audio = audio / np.max(np.abs(self.wave))
        #convert to int16
        audio = audio.astype(np.int16)
        one_audio = audio
        for i in range(0, self.loop):
            audio = np.concatenate((audio, one_audio))

        return audio


