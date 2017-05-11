# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 17:25:35 2016

@author: Gunjan
"""
import sys
from itertools import combinations

previous_split=None
previous_b=0
split_t=0

# input comes from STDIN (standard input)
for item in sys.stdin:                            
	# remove leading and trailing whitespace
    line = item.strip()
    split_trans,c=line.split('\t',1)

    
    split_t,b=split_trans.split(',',1)
    #checking for first element if prefix is same
    if previous_split==split_t :
        #appending to list the second element of itemset
        b_list.append(previous_b)
        previous_b=b
        
    elif previous_split==None:
        previous_split=split_t
        previous_b=b
        b_list=[]

    else:
        b_list.append(previous_b)
        #making combinations of 2itemset elements B AND C if prefix A matches
        for subsets in combinations(b_list,2):
                 #printing prefix ,combination formed from above step
                 print('%s,%s,%s\t%s' % (previous_split,subsets[0],subsets[1], 1))
            
        previous_split=split_t
        previous_b=b
        b_list=[]

if previous_split==split_t:
     b_list.append(previous_b)
     #making combinations of 2itemset elements B AND C if prefix A matches
     for subsets in combinations(b_list,2):
         print('%s,%s,%s\t%s' % (previous_split,subsets[0],subsets[1], 1))

       