import glob
import librosa
import numpy as np

window_time = 2 # sec
shift_time = 1 # sec


def chord_in_window(w, t):
	fft_w = np.fft.fft(w)
	fft_w = abs(fft_w)
	top_note = np.argsort(-fft_w)
	print(top_note[0:4]/t, fft_w[top_note[0:4]])
	return w

if __name__ == "__main__":
	fw = open('result.csv', 'w')
	chord = []
	note = []

	for f in glob.glob('./score/*'):
		data, fs = librosa.load(f)
		dur = librosa.get_duration(data)

		window_size = window_time*fs
		shift_size = shift_time*fs

		for win in range(0, shift_size, int(dur)):
			if win+window_size < dur*fs:
				chord.append(chord_in_window(data[win:win+window_size], dur))




