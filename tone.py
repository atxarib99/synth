from waveform_validator import WaveformValidator

class Audio:

    def __init__(self):
        pass

    def build_audio(self, wave):

        #validate waveform
        validator = WaveformValidator(44100)
        if not validator.validate_wave(wave):
            print("Invalid wave!")
            raise Exception("Invalid Wave!")


        #convert audio to 16-bit audio
        #normalize wave
        audio = tone * (2**15 - 1) / np.max(np.abs(tone))
        #convert to int16
        audio = audio.astype(np.int16)

        return audio


