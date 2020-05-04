'''
Created on Mar 2, 2017

@author: empqtut
'''
class LogicGate:
    
    def __init__(self,n):
        self.label =  n
        self.output = None
    
    def getLabel(self):
        return self.label
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
    
class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self, n)        
        self.pinA = None
        self.pinB = None
        
    def getPinA(self):
        if self.pinA==None:
            return int(raw_input("Enter PinA input for " + self.getLabel()+ " gate -->"))
        else:
            return self.pinA.getFrom().getOutput()
    
    def getPinB(self):
        if self.pinB==None:
            return int(raw_input("Enter PinB input for " + self.getLabel()+ " gate -->"))
        else:
            return self.pinB.getFrom().getOutput()
    
    def setNextPin(self,source):
        print source
        if self.pinA==None:
            self.pinA = source
        else:
            if self.pinB==None:
                self.pinB = source
            else:
                raise RuntimeError('ERROR : NO EMPTY PINS')

class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self, n)
        self.pin = None
    
    def getPin(self):
        if self.pin==None:
            return int(raw_input("Enter Pin input for " + self.getLabel()+ " gate -->"))
        else:
            return self.pin.getFrom().getOutput()  
    
    def setNextPin(self,source):
        if self.pin==None:
            self.pin = source
        else:
            print "Cannot Connect: No empty Input PIN"
    
class AndGate(BinaryGate):   
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return 1 if a==1 and b==1 else 0

class OrGate(BinaryGate): 
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return 0 if a==0 and b==0 else 1

class NotGate(UnaryGate):    
    def performGateLogic(self):
        a = self.getPin()
        return 1 if a==0 else 0
    
class NandGate(AndGate):
    def performGateLogic(self):
        if super(NandGate,self).performGateLogic() ==1:
            return 0
        else:
            return 1
        
class NorGate(OrGate):
    def performGateLogic(self):
        if super(OrGate,self).performGateLogic()==1:
            return 0
        else:
            return 1    
                    
class Connector():
    def __init__(self,fgate,tgate):
        self.fromgate = fgate
        self.togate = tgate
        
        tgate.setNextPin(self)
    
    def getFrom(self):
        return self.fromgate
    
    def getTo(self):
        return self.togate   
            
        
def main():
    g1 = NorGate("NAND")
    print g1.getOutput()       
             
    
main()