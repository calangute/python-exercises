'''
Created on Mar 16, 2017

@author: empqtut
'''

def copyFile(sourceFile,TargetFile):
    f1 = open(sourceFile,"r")
    f2 = open(TargetFile,"w")
    while True:
            text = f1.read(50)
            if text == "":
                break
            f2.write(text)
    f1.close()
    f2.close()   


f1 = open("test.txt","rw")
f2 = open("test2.txt","w")

f1.write("ballelakka ballelakka ! Salathukka Maduraikka !!")

print f1.read()

f1.close()

