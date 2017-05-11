# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 19:03:25 2016

@author: Gunjan
"""
import sys
# input comes from STDIN (standard input)
for item in sys.stdin:
   
	# remove leading and trailing whitespace
    line = item.strip()
    
    # splitting on tab
    split_trans = line.split('\t',1) 
    
    # list of split a,b,c
    split_composite_key = split_trans[0].split(',') 
    
    #checking if length of splitted composite key =3
    if len(split_composite_key) == 3:
        print('%s,%s\t%s' %(split_composite_key[1], split_composite_key[2],split_composite_key[0]))
    
     #checking if length of splitted composite key =2
    elif len(split_composite_key) == 2:
        print('%s,%s\t0' %(split_composite_key[1],split_composite_key[0]))
    