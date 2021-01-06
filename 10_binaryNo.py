#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    count=0
    max_ones=0
    while(n>0):
         if(n%2==0):
             count=0
         else:
             count+=1
         if(count>max_ones):
             max_ones=count
         n=n//2
    print(max_ones)

