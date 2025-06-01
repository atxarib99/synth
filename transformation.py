from abc import ABC, abstractmethod

class Transformation(ABC):
    """
    Transforms a wave in some manner
    """

    @abstractmethod
    def transform(self, wave):
        """
        Transforms a wave in some manner
        """
        pass

