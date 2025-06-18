from transformation import Transformation
import numpy as np

class ADSR(Transformation):
    """
        Attack, Decay, Sustain, Release

        Only linear for now
    """

    def __init__(self,
                 attack_duration=.25,
                 decay_duration=.25,
                 decay_min=.75,
                 sustain_duration=.25,
                 release_duration=.25):
        if attack_duration + decay_duration + sustain_duration + release_duration != 1:
            raise Exception("Sum of durations must == 1")

        self.attack_duration = attack_duration
        self.decay_duration = decay_duration
        self.decay_min = decay_min
        self.sustain_duration = sustain_duration
        self.release_duration = release_duration

    def transform(self, wave):
        #builds attack multiplier
        att_mults = np.linspace(0, 1, int(len(wave) * self.attack_duration), False)
        decay_mults = np.linspace(1, self.decay_min, int(len(wave) * self.decay_duration), False)
        sustain_mults = np.linspace(self.decay_min, self.decay_min, int(len(wave) * self.sustain_duration), False)
        release_mults = np.linspace(self.decay_min, 0, int(len(wave) * self.release_duration), False)

        mults = np.concatenate((att_mults, decay_mults, sustain_mults, release_mults))

        #sometimes due to int() casting to build ADSR durations, we can end up with transformation multiplication array not matching size of input wave. 
        #so we either trim the end, or add to it so that we can do array multipication. Usually just off by 1
        size_diff = len(wave) - len(mults)
        #if transform array too long
        if size_diff < 0:
            mults = mults[:size_diff]
        #elif transform array too short
        elif size_diff > 0:
            to_add = np.array([0] * (size_diff))
            mults = np.concatenate((mults, to_add))


        return mults * wave



