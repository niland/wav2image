#!/usr/bin/env python

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from numpy import empty
from numpy import  savetxt
from scipy.io import wavfile
from sys import  stdout
import argparse
import time

def parse_arguments():
    note = 'A command line tool to generate waveform image from wav file'
    parser = argparse.ArgumentParser(description=note)
    parser.add_argument('-v', '--version', action='version', version='1.0')
    parser.add_argument('-i', '--inputfile', required=True)
    parser.add_argument('-o', '--outputfile', help='The filename extension is used to generate the file within the good format')
    parser.add_argument('-c', '--color', default='575757',
                        help='Html color code for the waveform')
    return parser.parse_args()

def compute_waveform(inputfile, outputfile, color):
    image_length = 1000;

    try:
        fs, sig = wavfile.read(inputfile)
    except:
        print('Cannot open file: %s' % inputfile)
        raise

    if len(sig.shape) > 1:
        signal = sig.sum(1)
    else:
        signal = sig

    if len(signal) > 1000:
        frame_size=int(len(signal)/image_length)
    else:
        frame_size=1

    nframe = int(len(signal)/frame_size);

    if outputfile == 'stdout':
        signalF = signal.astype('float')/2**16
        waveform = empty(shape=(nframe,1))
        for k in range(0,nframe):
            waveform[k] = max(signalF[ k*frame_size : (k+1)*frame_size-1])
        savetxt(stdout, waveform, fmt='%.4f')
    else:
        waveform = empty(shape=(nframe*2,1))
        for k in range(0,nframe):
            waveform[2*k] = max(signal[ k*frame_size : (k+1)*frame_size-1])
            waveform[2*k+1] = min(signal[ k*frame_size : (k+1)*frame_size-1])

            plt.figure(1)
            plt.plot(waveform, color='#%s' % color)

            plt.axis('off')
            plt.gca().set_position([0, 0, 1, 1])
            plt.savefig(outputfile, transparent=True)

def main():
    args = parse_arguments()
    if args.outputfile is None:
        args.outputfile = 'stdout'
    compute_waveform(args.inputfile, args.outputfile, args.color)

if __name__ == '__main__':
    main()
