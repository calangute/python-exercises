'''a sample calculator class author : C.Manikandan'''
class Calculator():
    def __init__(self):
        pass
    def addition(self,*values):
        sum = 0
        for i in values:
            sum +=i
        return sum
    def subtraction(self,*values):
        val = values[1:]
        sub = values[0]
        for i in val:
            sub -= i
        return sub
    def multiply(self, *values):
        product = 1
        for i in values:
            product*=i
        return product


if __name__ == "__main__":
    myCal = Calculator()
    print myCal.multiply(10,20,30)
