'''
Created on Feb 1, 2017

@author: empqtut
'''
# User Defined Exception
class ZeroError(Exception):
    def __init__(self,mesg):
        Exception.__init__(self,mesg)
    
try:
    print "Program Starts"
    n1 = int(raw_input("Enter V1:"))
    n2 = int(raw_input("Enter V2 :"))
    
    if n1==0 or n2 ==0:
        raise ZeroError("Zero not accepted buddy")
    res = n1 + n2 
    
    print "Result = %d "%res
except ZeroError as e1:
    print "TAKE_ACTION-1"
except ValueError as e2:
    print "TAKE Action2"
except:
    print "default action"

finally:
    print "Program Ends"