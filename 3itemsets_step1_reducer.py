# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 01:50:21 2016

@author: Gunjan
"""

#!/usr/bin/env python

import sys

current_w = None
current_f = 0
word = None

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	w, f = line.split('\t', 1)

	# convert count (currently a string) to int
	try:
		f = int(f)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue

	# this IF-switch only works because Hadoop sorts map output
	# by key (here: w) before it is passed to the reducer
	if current_w == w:
		current_f += f
	else:
		if current_f:
			# write result to STDOUT
			print('%s\t%s' % (current_w, current_f))
		current_f = f
		current_w = w

# do not forget to output the last word if needed!
if current_w == w:
	print('%s\t%s' % (current_w, current_f))