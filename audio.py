from waveform_validator import WaveformValidator
from waveform import Waveform
import numpy as np

class Audio:

    def __init__(self, sample_rate, loop=1):
        self.sample_rate = sample_rate
        self.wave = np.linspace(0, 1, 0)
        #hold array of waves we will put together later
        self.waves = []
        self.transformations = []
        self.loop = loop -1

    def add_wave(self, wave):
        self.waves.append(wave)

    def add_waves(self, waves_to_add):
        for wave in waves_to_add:
            self.waves.append(wave)

    def add_transformation(self, transformation):
        self.transformations.append(transformation)

    def add_transformations(self, transformations: list):
        for transformation in transformations:
            self.transformations.append(transformation)

    def build_audio(self):

        #compile list of waves into single object
        count = 0
        for wave in self.waves:
            count += 1
            #if its of type Waveform, build it
            if isinstance(wave, Waveform):
                #TODO: validate each part independently
                self.wave = np.append(self.wave, wave.build())
            elif isinstance(wave, np.ndarray):
                #TODO: validate each part independently
                self.wave = np.append(self.wave, wave)
            else:
                print("Invalid wave type found during building at position:" + str(count))


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


