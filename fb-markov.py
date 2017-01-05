#!/usr/bin/python3
# -*- coding: utf8 -*-

import markovgen as mg
import urllib.request as req
import json
import sys
import ssl

def fetch():
	#apikey:n saa haettua osoitteesta: https://developers.facebook.com/tools/explorer

	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE

	f = req.urlopen('https://graph.facebook.com/me/posts?until=now&fields=message&limit=1000&access_token=API_KEY', context=ctx)
	d = json.loads(f.read().decode('utf-8'))

#	f = open('posts.js', 'r')
#	d = json.loads(f.read())

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
