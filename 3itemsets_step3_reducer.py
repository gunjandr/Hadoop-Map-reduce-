# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:45:08 2016

@author: Gunjan
"""

#!/usr/bin/env python

import sys

current_k = None
current_c = 0
k = None

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	k, c = line.split('\t', 1)

	# convert count (currently a string) to int
	try:
		c = int(c)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue

	# this IF-switch only works because Hadoop sorts map output
	# by key (here: k) before it is passed to the reducer
	if current_k == k :
		current_c += c
	else:
     #comparing if count>=minsup i.e. 1000
		if current_k and current_c>=1000:
			# write result to STDOUT
			print('%s' % (current_k))
		current_c = c
		current_k = k

# do not forget to output the last itemset if needed!
if current_k == k:
	print('%s' % (current_k))