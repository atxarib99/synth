from waveform import Waveform

class WaveformValidator:
    """
    Validates waveforms.
    This doesnt really work properly because it insinuated that the 
    duration of a waveform is a whole number (in seconds).
    TODO: actually validate sample size
    """

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
        if not (len(wave) / self.sample_rate == len(wave) // self.sample_rate):
            return False
        return True



