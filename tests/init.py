#!/usr/bin/env python

from subprocess import call
import os
import tempfile

filelist = {
    'test_mono_0sec.wav',
    'test_mono_3sec.wav',
    'test_mono_10sec.wav',
    'test_stereo_0sec.wav',
    'test_stereo_3sec.wav'
}

for filename in filelist:
    test_dir = os.path.dirname(os.path.realpath(__file__))
    root_dir = os.path.dirname(test_dir)
    bin = '%s/wav2image/__init__.py' % root_dir
    basename = os.path.splitext(filename)[0]
    inputfile = '%s/%s' % (test_dir, filename,)
    outputfile = '%s/%s.svg' % (tempfile.gettempdir(),  basename,)

    call(['python', bin, '-i', inputfile, '-o', outputfile])

    statinfo = os.stat(outputfile)
    if statinfo.st_size==0:
        raise Exception("Empty waveform: "+outpath)
    else:
        print 'Test passed on %s' % filename
