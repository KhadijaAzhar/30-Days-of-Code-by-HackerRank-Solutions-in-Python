#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
   
    a = list(map(int, input().rstrip().split()))
    n_swaps=0

    # Write your code here
    j = 1
    i = 0
    swap = []
    # Write your code here
    for i in range(n):
        n_swaps = 0
        for j in range(n-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swap.append(a[i])
                n_swaps += 1
        if n_swaps == 0:
            break
          
    print("Array is sorted in",len(swap),"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])


# In[ ]:




