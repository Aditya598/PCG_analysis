import os
import wave
import tkinter as tk
import numpy as np
from tkinter import filedialog
import glob
from scipy.io.wavfile import read

folder_path = r'C:\Users\Aditya\EOG Project\Read papers\Atraining_normal'
folder_files = glob.glob(folder_path + '/*.wav')
frame_rate = []

def frame_rate():
    global frame_rate, folder_path
    for file_name in os.listdir(folder_path):
        with wave.open(file_name, 'rb') as wave_file:
            frame_rate.append(wave_file.getframerate())


def write_to_sheet():
    global folder_path, folder_files
    _iter = 0
    for file_name in folder_files:
        readWAV = read(file_name)
        c = np.array(readWAV[1], dtype=float)
        np.savetxt('pcg_wave__' + str(_iter) + '.csv', c, delimiter=",")
        _iter += 1
