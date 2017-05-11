# -*- coding: utf-8 -*-

import sys
#import re
split_line_list=[]
split_list=[]
# input comes from STDIN (standard input)
for item in sys.stdin:
   
	# remove leading and trailing whitespace
    line = item.strip()
    
    #splitting by space
    split_line=line.split(' ')
    
    #appending to a list the first line of original input file
    split_line_list.append(split_line)
    #print(split_line_list)

#opening the 3candidate_itemsets output file which is copied to candidates    
f=open('candidates')
for each_f in f:
    # remove leading and trailing whitespace
    each_strip=each_f.strip()
    
    #splitting by single tab
    split_e,e=each_strip.split('\t',1)
    
    #splitting by single comma
    e_split,b=e.split(',',1)
    #print(split_e,e_split,b)
    
    #appending a list to larger list
    split_list.append([split_e,e_split,b])
    #print(split_list)
  
    
for each in split_list:
    for each_t in split_line_list:
        #if first element e.g. A of 3itemset exist in transaction 1
        if each[0] in each_t:
            #if second element e.g.B of 3itemset exist in transaction 1
            if each[1] in each_t:
                #if third element e.g.C of 3itemset exist in transaction 1
                if each[2] in each_t:
                      #printing frequent three itemset
                      print('%s,%s,%s\t%s' % (each[0],each[1],each[2], 1))


                
