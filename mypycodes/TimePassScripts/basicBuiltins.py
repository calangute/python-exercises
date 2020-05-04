def square(x):
    return x**2

def double(x):
    return 2*x

def x_calc(x):
    if x <= 0:
        return double(x)
    else:
        return square(x)
