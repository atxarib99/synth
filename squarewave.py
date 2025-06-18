from waveform import Waveform
import numpy as np

class Squarewave(Waveform):

    def __init__(self, frequency, duration=1.0, volume=0.05):
        self.frequency = frequency
        self.duration = duration
        self.volume = volume

    def build_waveform(self):
        t = np.linspace(0, self.duration, int(Waveform.sample_rate * self.duration), False)
        wave = np.sin(self.frequency * t * 2 * np.pi)

        with np.nditer(wave, op_flags=['readwrite']) as it:
            for cell in it:
                if cell[...] > 0:
                    cell[...] = self.volume
                else:
                    cell[...] = self.volume * -1

        return wave
