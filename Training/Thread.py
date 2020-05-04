'''
Created on Feb 1, 2017

@author: empqtut
'''
import os
import time,threading

def job1():
    print "P1 - PID =", os.getpid()
    time.sleep(5)

def job2():
    print "P2 - PID =",os.getpid()
    time.sleep(6)
    
if __name__ == '__main__':
    p1 = threading.Thread(target=job1,args=())
    p2 = threading.Thread(target=job2,args=())
    p1.start()
    p2.start()
    start = time.time()
    p1.join()
    p2.join()
    end = time.time()
    print "Time Taken :",(end-start)
