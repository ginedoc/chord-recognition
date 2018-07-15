from midi2audio import FluidSynth
import glob
import os


for f in glob.glob('./score/midi/*'):
    fs = FluidSynth()
    out = os.path.basename(f)
    fs.midi_to_audio(f, './score/wav/' + out + '.wav')
