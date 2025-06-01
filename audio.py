from waveform_validator import WaveformValidator
import numpy as np

class Audio:

    def __init__(self, sample_rate):
        self.sample_rate = sample_rate
        self.wave = np.linspace(0, 1, 0)

    def add_wave(self, wave):
        self.wave = np.append(self.wave, wave)

    def build_audio(self):

        #validate waveform
        validator = WaveformValidator(self.sample_rate)
        if not validator.validate_wave(self.wave):
            print("Invalid wave!")
            exit(1)


        #convert audio to 16-bit audio
        #normalize wave
        audio = self.wave * (2**15 - 1) / np.max(np.abs(self.wave))
        #convert to int16
        audio = audio.astype(np.int16)

        return audio


