#!/usr/bin/python3
# -*- coding: utf8 -*-

import markovgen as mg
import urllib.request as req
import json
import sys

def fetch():
	#apikey:n saa haettua osoitteesta: https://developers.facebook.com/tools/explorer

	f = req.urlopen('https://graph.facebook.com/me/posts?until=now&fields=message&limit=1000&access_token=CAACEdEose0cBAO58O0w92dBgQs7kbZBLGpwZCrZCP8znSHyFYuXch40PSP1BxJ7qRx8EqjQMNTZBRjqZACgAyTCfPYcdEcvpMfKNCSnUxOSXmhyxMjl7vN982SHSs3tFzZBpA3nhHJpZCcfgHqjqBJQO7nT2QklRqBiwyZAkwUFgQfsONcqOK3d7ZAQpyCZBNDrS0xDh75dfgCrRXormsINxJu')

	d = json.loads(f.readall().decode('utf-8'))

	wf = open('fswords.txt', 'w')

	for m in d['data']:
		if 'message' in m:
			wf.write(m['message'] + ' ')

	wf.close

if 'fetch' in sys.argv:
	fetch()

wf = open('fswords.txt', 'r')

m = mg.Markov(wf)
print(m.generate_markov_text(20))
