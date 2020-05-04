'''
Created on Feb 13, 2017

@author: manikandan
'''

def seq_search(alist, item1):
    pos = 0
    found= False    
    while pos < len(alist) and not found:
        if alist[pos]==item1:
            found = True
        else:
            pos += 1
    return found  

def bin_search(somelist, item):
    

print seq_search(a, 4)