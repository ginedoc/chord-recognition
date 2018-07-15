import glob
import librosa
import numpy as np
import heapq
import chromagram
import hmm

window_time = 2 # sec
shift_time = 1 # sec

chord_root = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'false']

##
def note_predict(note_arr):
	p = heapq.nlargest(4, enumerate(note_arr), key=lambda x: x[1])

	ret = []
	for i in range(4):
		ret.append(chord_root[p[i][0]])

	return(ret)



#####################
if __name__ == "__main__":
	fw = open('result.csv', 'w')
	chord = []
	note = []

	for f in glob.glob('./score/wav/*'):
		# data, fs = librosa.load(f)
		# dur = librosa.get_duration(data)

		# print(fs)
		hmm.get_chord_progress(f, 1.25, 0.625)
		# window_size = window_time*fs
		# shift_size = shift_time*fs

		# for win in range(0, shift_size, int(dur)):
		# 	if win+window_size < dur*fs:
		# 		# chord.append(chord_in_window(data[win:win+window_size], dur))
		# 		n = note_predict( chromagram.compute_chroma(data[win:win+window_size], fs) )
		# 		print(n)
		# # chord_in_window(data[0:0+window_size], dur)

