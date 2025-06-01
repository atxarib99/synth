from abc import ABC, abstractmethod

class Waveform(ABC):
    """
    Waveform class thats abstract. This should be implemented by classes that generate a waveform.
    """
    #make these static for now
    sample_rate = 44100
    duration = 1.0

    @abstractmethod
    def build_waveform(self):
        """
        build_waveform() will be called by runner classes or anything else trying to build a waveform
        """
        pass

