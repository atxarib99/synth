import numpy as np
import matplotlib.pyplot as plt

sample_rate = 44100
tone = np.sin(80 * np.linspace(0, 1, sample_rate) * 2 * np.pi)
print(tone)
plt.plot(tone)

