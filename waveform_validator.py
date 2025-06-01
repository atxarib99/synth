from waveform import Waveform

class WaveformValidator:

    def __init__(self, sample_rate):
        self.sample_rate = sample_rate

    def validate_builder(self, waveform: Waveform) -> bool:
        #ensure waveform class has appropriate sample rate
        wave = waveform.build_waveform()
        #checks that it is appropriate sample_rate of any duration
        if not (len(wave) / self.sample_rate == len(wave) // self.sample_rate):
            return False
        return True

    def validate_wave(self, wave) -> bool:
        print(len(wave))
        if not (len(wave) / self.sample_rate == len(wave) // self.sample_rate):
            return False
        return True



