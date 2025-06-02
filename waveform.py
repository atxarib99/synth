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

    def build(self):
        wave = self.build_waveform()
        if hasattr(self, "transformations"):
            for transformation in self.transformations:
                wave = transformation.transform(wave)
                print(len(wave))
        return wave


    def add_transformation(self, transformation):
        if not hasattr(self, "transformations"):
            self.transformations = []
        self.transformations.append(transformation)
        return self

    def add_transformations(self, transformations: list):
        if not hasattr(self, "transformations"):
            self.transformations = []
        for transformation in transformations:
            self.transformations.append(transformation)
        return self

