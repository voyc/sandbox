''' level.py '''

import configparser
import psycopg2
import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def level(prnt=True,plot=False,save=False,update=False):
	output = ''
	freqtbl = {}

	def sortFreq(key):
		return freqtbl[key]['freq']
	
	def sortLvl(key):
		return freqtbl[key]['lvl']

	# open db
	config = configparser.ConfigParser()
	config.read('../../config.ini')
	connect_string = f""\
		f"dbname={config['db']['name']} "\
		f"user={config['db']['user']} "\
		f"password={config['db']['password']} "\
		f"port={config['db']['port']}"
	conn = psycopg2.connect(connect_string)

	# build freq table
	cur = conn.cursor()
	id = 1
	#cur.execute("SELECT words from mai.story where id = %s", (id,))
	cur.execute("SELECT words from mai.story")
	rows = cur.fetchall()
	for row in rows:
		words = json.loads(row[0])
		for word in words:
			t = word['t']
			if len(t) > 0 and t != ' ':
				for loc in word['loc']:
					n = loc['n']
					if t in freqtbl:
						freqtbl[t]['freq'] += 1
					else:
						#freqtbl[t] = 1
						freqtbl[t] = {'freq':1, 'lvl':0}
	cur.close()
	conn.close()
	
	# sort by frequency
	sorted_keys = sorted(freqtbl, key=sortFreq, reverse=True)
	
	# set level of each word
	cnt = 0
	words_per_level = 20
	level = 1
	for key in sorted_keys:
		cnt += 1
		if cnt > words_per_level:
			cnt = 0
			level += 1
		freqtbl[key]['lvl'] = level

	# print freq table
	if prnt:
		output += f"word\tfreq\tlevel\n"
		for key in sorted_keys:
			output += f"{key}\t{freqtbl[key]['freq']}\t{freqtbl[key]['lvl']}\n"
			if freqtbl[key]['lvl'] > 5:
				break;
		output += f'total words: {len(freqtbl)}\n'
	
	# plot results
	if plot:
		x = np.array([])
		y = np.array([])
		for key in freqtbl:
			x = np.append(x, freqtbl[key]['freq'])
			y = np.append(y, freqtbl[key]['lvl'])
		plt.plot(x)
		if save:
			plt.savefig('plot.png')
		plt.show()
	return output

if __name__ == '__main__':
	s = level(prnt=True, plot=False, save=False, update=False)
	print(s)

'''
levels
freq 1 or 2
freq 3 to 20
freq > 20
'''
