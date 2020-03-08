import matplotlib.pyplot as plt
import numpy as np

def get_colors(segments, signal, sol_vec):
    colors = ['black'] * len(signal)
    for i in range(len(segments)):
        if len(segments[i]) < 2:
            continue
        else:
            if sol_vec[i] == 1:
                colors[segments[i][0]:segments[i][1]] = ['red'] * abs(segments[i][0] - segments[i][1])
            elif sol_vec[i] == -1:
                colors[segments[i][0]:segments[i][1]] = ['blue'] * abs(segments[i][0] - segments[i][1])
    return colors


# credt for below code: Abhay Haraple
# http://abhay.harpale.net/blog/python/how-to-plot-multicolored-lines-in-matplotlib/

def find_contiguous_colors(colors):
    # finds the continuous segments of colors and returns those segments
    segs = []
    curr_seg = []
    prev_color = ''
    for c in colors:
        if c == prev_color or prev_color == '':
            curr_seg.append(c)
        else:
            segs.append(curr_seg)
            curr_seg = []
            curr_seg.append(c)
        prev_color = c
    segs.append(curr_seg)  # the final one
    return segs


def plot_multicolored_lines(x, y, colors):
    segments = find_contiguous_colors(colors)
    plt.figure()
    plt.xlabel('time (s * 10^-5)')
    plt.ylabel('absolute amplitude')
    start = 0
    for seg in segments:
        end = start + len(seg)
        l, = plt.gca().plot(x[start:end], y[start:end], lw=2, c=seg[0])
        start = end


