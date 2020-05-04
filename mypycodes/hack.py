@lru_cache(maxsize = 1000)
def fibo(num):
    if num==1:
        return 1
    elif num==2:
        return 1
    elif num>2:
        return fibo(num-1)+fibo(num-2)
for num in range(1,1000):
    print(num,':',fibo(num))