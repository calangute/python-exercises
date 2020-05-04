'''
Created on Feb 15, 2017

@author: empqtut
'''
from Algorithms.basic import Stack

def brackChecker(symbolstr):
    s = Stack()
    o = Stack()
    for index in xrange(len(symbolstr)):
        sym = symbolstr[index]
        if s.isEmpty():
            if sym == ")":                
                o.push(sym)
            else:
                s.push(sym)
        else:
            if sym == "(":
                s.push(sym)
            else:
                s.pop()
    if not o.isEmpty():
        for a in xrange(o.size()):
            symbolstr = "(" + symbolstr
    if not s.isEmpty():
        for a in xrange(s.size()):
            symbolstr = symbolstr + ")"   
    return symbolstr
                              

def parse_dict(ipjson):
    def _child_finder(key, value):
        if isinstance(value, dict):
            return [(key + '.' + k_child, v_child) for k_child, v_child in parse_dict(value).items()]
        else:
            return [(key, value)]

    result_list = [item for ky, val in ipjson.items() for item in _child_finder(ky, val)]
    return dict(result_list)


my_js={"TargetingDimensions": {
          "Days": [
            "FRIDAY"
          ],
          "Devices": [
            "iPad"
          ],
          "States": [
            "us|ar",
            "us|ak",
            "us|al"
          ]}}

print parse_dict(my_js)