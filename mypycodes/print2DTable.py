
def printCol(n):
    i=1
    while i<=n:#this controls whether to print a right triangle or table.
        print n*i,'\t',
        i+=1
    print

def printRow(lenth):
    i=1
    while i<=lenth:
        printCol(i)
        i+=1


if __name__=='__main__':
    printRow(10)
