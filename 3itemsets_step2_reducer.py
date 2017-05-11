# -*- coding: utf-8 -*-
import sys
current_temp=None
cur_key1=None
cur_key2=None

# input comes from STDIN
for item in sys.stdin:
	# remove leading and trailing whitespace
     line = item.strip()

     #splitting the line
     temp = line.split()
     
     #splitting on the basis of comma
     p=temp[0].split(',')
     fg=p[0]
     yz=p[1]
     
     #checking if special character =0
     if temp[1] == '0':
         p=temp[0]
         a= p.split(',')
         
         cur_key1=a[0]
         cur_key2=a[1]
     else:
        b = temp[0].split(',')
        
        next_a=b[0]
        next_b=b[1]
        if cur_key1 == next_a and cur_key2 == next_b:
            print('%s\t%s' %(temp[1], temp[0]))
       
