from transformation import Transformation
import numpy as np

class Noise(Transformation):

    def __init__(self, noise_level=0.1):
        self.noise_level = noise_level

    def transform(self, wave):
        noise = np.random.normal(loc=0, scale=self.noise_level, size=len(wave))
        noise = np.clip(noise, self.noise_level * -1, self.noise_level)  # force values into range if needed
        return wave+noise






