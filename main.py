import audio_pcg
import ewt
import sound_recog
import grapher
import numpy as np
import matplotlib.pyplot as plt

# audio_pcg.write_to_sheet()
env, phase, signal = ewt.transform()
phase_list = phase.tolist()
segmented_vector = sound_recog.segment(phase_list)
print('pcg segments')
print(*segmented_vector, sep='\n')
intl, dur, area_env = sound_recog.initialize_parameters(segmented_vector, phase_list)
heart_sounds = sound_recog.recog(len(segmented_vector), dur, area_env, intl)
print()
print('heart sounds extracted from input signal')
print(*heart_sounds, sep='\n')

col = grapher.get_colors(segmented_vector, env, heart_sounds)
x = np.arange(len(signal))
grapher.plot_multicolored_lines(x, signal, col)
plt.show()
# plt.plot(x)
# plt.show()
