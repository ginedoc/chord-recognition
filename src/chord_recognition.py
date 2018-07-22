import glob
import librosa
import numpy as np
import heapq
import chromagram
import hmm
import melody

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
	fw = open('../data/result.csv', 'w')
	chord = []
	note = []

	win_s = 12*8
	sft_s = 6*8
	for f in glob.glob('../score/wav/*.wav'):
		print(f)

		chord = hmm.get_chord_progress(f, 0.0232*win_s/8, 0.0232*sft_s/8)
		note = melody.get_melody_freq(f)
		

		for i in range(len(chord)):
			fw.write('%s,'%chord[i])
			# print('%s,'%chord[i])
			if i*sft_s+win_s>len(note):
				note = np.append(note, np.zeros(i*sft_s+win_s-len(note))-1)
			for n in note[i*sft_s:i*sft_s+win_s]:
				fw.write('%s,'%n)
				# print('%s,'%n, end='')
			fw.write('\n')
			# print('\n')

	fw.close()