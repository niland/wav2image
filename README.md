# Wav2image

A waveform generator that can generate any image type (png, svg, etc.).

## Dependency

* python modules
    + matplotlib
    + numpy
    + scipy

On ubuntu you can install those dependencies using `apt-get install python-numpy python-scipy python-matplotlib`

## Installation

On ubuntu 12.04 you have to install 
### Using pip (Recommended)

    pip install wav2image

This command will install wav2image and its python dependencies (not the system dependencies).

### Using git

    git clone https://github.com/niland/wav2image

Use `python wav2image/__init__.py`.

## Usage

    wav2image [options]

## Options
Please read

    wav2image -h

## Example

    wav2image -i myTrack.wav -o myWaveform.svg -c 000000

## License

This software is distributed under the MIT licence
