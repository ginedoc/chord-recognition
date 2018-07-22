import numpy as np
chords = ['G','G#','A','A#','B','C','C#','D','D#','E','F','F#','Gm','G#m','Am','A#m','Bm','Cm','C#m','Dm','D#m','Em','Fm','F#m']
notes = [i for i in range(-1, 13)]
win_s = 96

def train_data(fname):
	f = open(fname, 'r')
	data = f.read()
	chord = []
	note = []

	lines = data.split('\n')
	cr = [[] for _ in range(len(lines))]
	nr = [[] for _ in range(len(lines))]

	for line in lines:
		line = line.split(',')
		chord.append(line[0])
		for n in line[1:-1]:
			note.append(n)


	for i, cc in enumerate(chord):
		t = [0 for _ in range(24)]
		for j, cs in enumerate(chords):
			if cc==cs:
				t[j] = 1
				cr[i] = t
				break
			else:
				cr[i] = t

	note = np.array(note)
	note = np.append(note, np.zeros(int(win_s-len(note)%win_s)))
	note = np.reshape(note, (len(chord), win_s))
	for i, nn in enumerate(note):
		t = [0 for _ in range(13)]
		for n in nn:
			n = np.float32(n)
			for k, ns in enumerate(notes):
				if n==ns:
					t[k] = 1
					break
			nr[i] += t
		nr[i] = np.array(nr[i])

	cr = np.array(cr)
	nr = np.array(nr)
	
	return (nr, cr)