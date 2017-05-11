# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 01:50:21 2016

@author: Gunjan
"""

#!/usr/bin/env python

import sys

current_d = None
current_t = 0
word = None

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	d, t = line.split('\t', 1)

	# convert count (currently a string) to int
	try:
		t = int(t)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue

	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	if current_d == d:
		current_t += t
	else:
         #comparing if count>=minsup i.e. 1000
		if current_d and current_t>=1000:
			# write result to STDOUT
			print('%s\t%s' % (current_d, current_t))
		current_t = t
		current_d = d

# do not forget to output the last word if needed!
#if current_word == word:
#	print('%s\t%s' % (current_word, current_count))