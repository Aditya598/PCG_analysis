# this code is used to convert the raw pcg data into instantaneous phase of its enveloped hilbert transform as specified in the
# 5th chapter of the thesis by V. NIVITHA VARGHEES titled "PHONOCARDIOGRAM SIGNAL DELINEATION METHODS FOR AUTOMATED ANALYSIS OF
# HEART SOUNDS AND MURMURS" for AMRITA SCHOOL OF ENGINEERING (July 2017)
# *Note: the wave transform according to the Empirical Wavelet Transform mentioned in the thesis hasn't been replicated completely or
#  exactly by the methods outlined in it. The acquired signal, hence, is noisier and less accurate



import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal
from scipy.signal import savgol_filter
from scipy.signal import hilbert


# accept arbitrarily long pcg wave
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


# returns the shannon entropy envelope of the absolute pcg signal
def shannon_entropy_envelope(abs_signal):
    shannon_entropy = [-i * math.log(i) for i in abs_signal]
    return savgol_filter(shannon_entropy, 299, 4)


# accepts signal input and transforms obtained signal to the phase domain 
def transform():
    inp = np.array(wave_input(), dtype=float)
    t_gol = savgol_filter(inp, 299, 6)
    abs_t = [abs(i) for i in t_gol]
    se_t = abs(shannon_entropy_envelope(abs_t))
    analytic_wave = hilbert(se_t)
    amplitude_envelope = np.abs(analytic_wave)
    instantaneous_phase = np.unwrap(np.angle(analytic_wave))
    return amplitude_envelope, instantaneous_phase, t_gol


