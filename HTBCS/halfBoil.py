import math,copy

class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(str(self.x),str(self.y))

    def __add__(self,p2):
        return Point(self.x + p2.x, self.y + p2.y)

    def __sub__(self,p2):
        return Point(self.x - p2.x, self.y - p2.y)

    def __mul__(self,p2):
        return Point(self.x * p2.x, self.y * p2.y)

    def __rmul__(self,p2):
        return Point(self.x * p2, self.y * p2)

    def distance(self,p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        dSq = dx**2 + dy**2
        return math.sqrt(dSq)

    def reverse(self):
        self.x,self.y =self.y,self.x

    def frontback(self):
        back = copy.copy(self)
        back.reverse()
        print str(self),str(back)


class Rectangle(Point):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.corner = Point()

    def findCenter(self):
        p = Point()
        p.x = self.corner.x + (self.width/2.0)
        p.y = self.corner.y + (self.height/2.0)
        return p

    def growRect(self,nheight,nwidth):
        self.width += nwidth
        self.height += nheight

    def moveRect(self,dx,dy):
        self.corner.x += dx
        self.corner.y += dy

class Time():
    def __init__(self, hours=0,minutes=0,seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def printTime(t):
        print "{0:02d}:{1:02d}:{2:02d}".format(t.hours,t.minutes,t.seconds)

    def increment(self,seconds):
        self.seconds = self.convertToSeconds() + seconds
        return self.seconds

    def convertToSeconds(self):
         seconds =  (self.hours*3600) + (self.minutes*60) + self.seconds
         return seconds

    def after(self, time2):
        if self.hours > time2.hours:
            return 1
        else:
            return 0
        if self.minutes > time2.minutes:
            return 1
        else:
            return 0
        if self.seconds > time2.seconds:
            return 1
        return 0

    def addTime(self,t2):
        sumTime = self.convertToSeconds() + t2.convertToSeconds()
        return self.makeTime(sumTime)

    def makeTime(self,sec):
        nTime = Time()
        nTime.hours = sec//3600
        nTime.minutes = (sec%3600)//60
        nTime.seconds = sec%60
        return nTime

if __name__=='__main__':
    box = Rectangle(100.0,200.0)
    p1 = Point(10.0,20.0)
    p1.frontback()
    timy = Time(1,9,45)
    domy = Time(10,49,25)
    doneTime = Time()
    doneTime = timy.addTime(domy)
    doneTime.printTime()
    timy.printTime()
    if doneTime.after(timy):
        print "hurrah!!"
