#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, json
from datetime import datetime
from flask import Flask, abort, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST']) 
def webhook():
	if not request.form:
		abort(400)

	data = json.loads(request.form['payload'])

	
	# Do what you need with the data here.
	# In this case, we're only acting on media.play or media.resume events.

	if data['event'] == 'media.play' or data['event'] == 'media.resume':
		user = data['Account']['title']
		artist = data['Metadata']['grandparentTitle']
		title = data['Metadata']['title']
		event = data['event'][6:]

		# print user
		print "%s %s by %s" % (event.capitalize(), title, artist)
		# print artist
		# print title

	# print data
	return "OK"

# Set the IP address you want to bind to here, and specify the port
if __name__ == '__main__':
	app.run(host='192.168.1.20', port=8091, debug=False,threaded=True)
