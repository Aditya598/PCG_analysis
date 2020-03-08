import cleanup
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal
from scipy.signal import savgol_filter
from scipy.signal import hilbert


def wave_input():
    wave = []
    print('enter wave')
    while True:
        a = float(input())
        if a == 9999:
            break
        else:
            wave.append(float(a))
    return wave


def shannon_entropy_envelope(abs_signal):
    shannon_entropy = [-i * math.log(i) for i in abs_signal]
    return savgol_filter(shannon_entropy, 299, 4)


def transform():
    inp = np.array(wave_input(), dtype=float)
    t_gol = savgol_filter(inp, 299, 6)
    plt.plot(t_gol)
    plt.show()
    abs_t = [abs(i) for i in t_gol]
    se_t = abs(shannon_entropy_envelope(abs_t))
    plt.plot(abs_t)
    plt.show()
    analytic_wave = hilbert(se_t)
    amplitude_envelope = np.abs(analytic_wave)
    plt.plot(se_t)
    plt.plot(amplitude_envelope)
    plt.show()
    instantaneous_phase = np.unwrap(np.angle(analytic_wave))
    plt.plot(instantaneous_phase)
    plt.show()
    return amplitude_envelope, instantaneous_phase, t_gol


