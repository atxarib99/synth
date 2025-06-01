from waveform import Waveform
import numpy as np

class Sinewave(Waveform):

    def __init__(self, frequency, duration):
        self.frequency = frequency
        self.duration = duration

    def build_waveform(self):
        t = np.linspace(0, self.duration, int(Waveform.sample_rate * self.duration), False)
        wave = np.sin(self.frequency * t * 2 * np.pi)
        return wave
