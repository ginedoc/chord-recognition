import vamp
import librosa
import essentia.standard as es
import math
import numpy as np
import matplotlib.pyplot as plt


C0 = 440*pow(2, -4.75)

sft_s = 6*8

def get_melody_freq(f):
	audio, sr= librosa.load(f)
	data = vamp.collect(audio, sr, "mtg-melodia:melodia")

	hop, melody = data['vector']
	for i, m in enumerate(melody):
		if m > 0:
			h = round(12*math.log2(m/C0))
			n = h%12
		else:
			n = -1
		melody[i] = n

	# plt.plot(melody)
	# plt.show()

	return melody[1*sft_s:-1]

# if __name__ == "__main__":
# 	print(get_melody_freq('./score/wav/C.wav', 8192))