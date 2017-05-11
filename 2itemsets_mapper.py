# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 20:14:27 2016

@author: Gunjan
"""
import sys
#importing combinations to make combinations 
from itertools import combinations

# input comes from STDIN (standard input)
for item in sys.stdin:
    #creating a list
    combination_list=[]
	# remove leading and trailing whitespace
    line = item.strip()
    #splitting by space
    split_trans=line.split(" ")
    
    #making combinations of length 2 i.e. two itemsets
    for subset in combinations(split_trans, 2):
        #appending all 2itemsets to list
        combination_list.append(subset)
        #printing list
        print('%s,%s\t%s' % (subset[0],subset[1], 1))
       