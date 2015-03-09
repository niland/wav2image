#!/usr/bin/python

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from numpy import empty
from scipy.io import wavfile
import argparse
import time

def computeWaveform(filename, outfilename):
    image_length = 1000;
    try:
        fs, sig = wavfile.read(filename)
    except:
        print('Cannot open file: '+filename)

    if len(sig.shape) > 1:
        signal = sig.sum(1)
    else:
        signal = sig

    if len(signal) > 1000:
        frame_size=int(len(signal)/image_length)
    else:
        frame_size=1

    nframe = int(len(signal)/frame_size);

    waveform = empty(shape=(nframe*2,1))
    for k in range(0,nframe):
        waveform[2*k] = max(signal[ k*frame_size : (k+1)*frame_size-1])
        waveform[2*k+1] = min(signal[ k*frame_size : (k+1)*frame_size-1])

    plt.figure(1)
    plt.plot(waveform, color='#575757')

    plt.axis('off')
    plt.gca().set_position([0, 0, 1, 1])
    plt.savefig(outfilename, transparent=True)

## MAIN ##
parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("outfilename")
args = parser.parse_args()
computeWaveform(args.filename, args.outfilename)
