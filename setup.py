from setuptools import setup

setup(
    name='wav2image',
    version='1.0',
    description='Waveform generator that can generate any image type',
    url='https://github.com/niland/wav2image',
    author='Niland',
    author_email='support@niland.io',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'License :: OSI Approved :: MIT License'
    ],
    keywords='waveform svg png wav',
    install_requires=['matplotlib', 'numpy', 'scipy'],
    scripts=['wav2image']
)
