# this section extracts input parameters, subdivides the phase signal into segments and classifies those segments as per the algorithm 
# detailed in chapter 5 of the thesis.


import matplotlib.pyplot as plt
import numpy as np


# divide the phase wave into segments of ranges from lowest to highest value, spread across the entire signal
def segment(phase_wave):
    segment_vector = []
    a = []
    _iter = 0
    _local_max = min(phase_wave)
    prev_elem = 0
    extrema_count = 0
    high_flag = False
    low_flag = False
    for i in range(len(phase_wave)):
        _local_max = max(_local_max, phase_wave[i])
        if phase_wave[i] <= -1.5 and not low_flag:
            a.append(i)
            extrema_count = 0
            high_flag = False
            low_flag = True
            _local_max = min(phase_wave)
        if _local_max > prev_elem:
            extrema_count += 1
            if extrema_count >= 150 and not high_flag:
                a.append(phase_wave.index(_local_max))
                segment_vector.append(a)
                a = []
                extrema_count = 0
                high_flag = True
                low_flag = False
                _local_max = min(phase_wave)
        prev_elem = phase_wave[i]
    return segment_vector


# initialize values of parameters: segment interval, segment duration, segment area of the envelope 
def initialize_parameters(segments, signal):
    interval = []
    dur = []
    area_env = []
    for i in range(len(segments)):
        a = 0
        if len(segments[i]) < 2:
            continue
        else:
            try:
                interval.append(segments[i + 1][0] - segments[i][0])
                dur.append(segments[i][1] - segments[i][0])
                for j in range(segments[i][0], segments[i][1]):
                    a += abs(signal[j])
                area_env.append(a)
            except IndexError:
                continue
    return interval, dur, area_env
                

# classify according to the detailed algorithm
def recog(n_i, seg_dur, area_env, intervals):
    hs_vector = [0] * n_i
    s1_flag = False
    s2_flag = False
    for i in range(n_i):
        try:
            if intervals[i] < intervals[i + 1]:
                s1_flag = True
                if (intervals[i + 1] - intervals[i] > 2205):    # 50ms = 2205 samples
                    hs_vector[i] = 1
                elif (seg_dur[i] > seg_dur[i + 1]) and (seg_dur[i] - seg_dur[i + 1]) > 220:   # 5ms = 220 samples
                    hs_vector[i] = 1
                elif area_env[i] > 1.5 * area_env[i + 1]:
                    hs_vector[i] = 1
            else:
                s2_flag = True
                hs_vector[i] = -1
            if intervals[i] > intervals[i + 1]:
                s2_flag = True
                if intervals[i] - intervals[i + 1] > 2205:
                    hs_vector[i] = -1
                elif seg_dur[i] < seg_dur[i + 1] and seg_dur[i + 1] - seg_dur[i] > 220.5:
                    hs_vector[i] = -1
                elif area_env[i] < 1.5 * area_env[i + 1]:
                    hs_vector[i] = -1
            else:
                s1_flag = True
                hs_vector[i] = 1
            if not s1_flag and not s2_flag:
                hs_vector[i] = 0
        except IndexError:
            continue
    return hs_vector

                    
    
