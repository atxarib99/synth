from waveforms.waveform_validator import WaveformValidator
from waveforms.waveform import Waveform
import numpy as np

class Track:

    #TODO: Loop being ignored.
    def __init__(self, loop=1):
        self.wave = np.linspace(0, 1, 0)
        #hold array of waves we will put together later
        self.waves = []
        self.transformations = []
        self.loop = loop

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

