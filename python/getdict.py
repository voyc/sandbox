''' getdict.py '''
import configparser
import psycopg2
import json
import numpy as np

def getdict():
	sql_list_dict = ''\
		'select d.id, m.id, d.lvl, d.t, m.e '\
		'from mai.dict d, mai.mean m '\
		'where d.id = m.did '\
		'order by d.lvl;'
	
	print(sql_list_dict)
	
	# open db
	config = configparser.ConfigParser()
	config.read('../../config.ini')
	conn = psycopg2.connect(f"dbname={config['db']['name']} user={config['db']['user']} password={config['db']['password']} port={config['db']['port']}") 
	
	cur = conn.cursor()
	cur.execute(sql_list_dict)
	
	print(f'rowcount: {cur.rowcount}')
	
	rows = cur.fetchall()
	for row in rows:
		print(row)
	
	cur.close()
	conn.close()

if __name__  == '__main__':
	getdict()

