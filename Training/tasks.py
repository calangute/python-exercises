'''
Created on Jan 30, 2017
Program to add two numbers
find the sum
print the result

@author: empqtut
'''
import os

def addition():
    '''contains points related to sum example'''
    n1 = raw_input("Enter the First value: ")
    n2 = raw_input("Enter the second value: ")
#converting type to integer
#python takes all the values as strings when taken from keyboard.
    if n1.isdigit() and n2.isdigit():
        res = int(n1) + int(n2)
        print "Sum of %s and %s is %s"%(n1,n2,res)
    else:
        print "Invalid Input"
    
    
def numbers():
    '''contains points related to numbers'''
    print "all numbers are stored in decimal format"
    num =1452
    first_digit= str(num)[0]
    print "first digit is ",first_digit
   
def strings():
    '''Contains points related to strings'''
    print '''1.all strings are stored in ascii and are immutable
2.strings can be in single quotes or double quotes or even triple quotes'''
    a = r"10\n20\n30" #WYSIWYG
    b = "10\n20\n30"
    d = 'sample data'
    # Each letter in the string can be retrieved with index number, similar format as array
    print a,b,"\n",d[0],'\n',d[-1]
    #Slicing a[start:{len()-1}:step]
    print "Sample data to play:",d
    print "Length of the string",len(a)
    print "First Character:",a[0]
    print "Last Character:",a[-1]
    print "Slicing 4 chars of d :",d[:3]
    print "Reversed string :",d[::-1]
    print "Except First 4 chars:",d[4:]
    print "Except last 4 chars:",d[:-4]  
    #Strip
    print "Concatenating hello:","hello "+d
    print "a.strip(), a.lstrip(),a.rstrip()"
    print "by default strip strips space,newline and tabs from the either side of the string"
    #replace
    #print "replace ("existing word", "word to replace")"
    
    
def task1(name):
    '''Function to convert First and Last character of the entered string to upper case'''
    name_upper = name[0].upper() + name[1:-1] + name[-1].upper()
    print "Orignal Name : %s Changed Name: %s "%(name,name_upper)

def task2():
    '''convert abcdefghijkl --> DCBA-efgh-LKJI'''
    str1 = raw_input("Enter any String:")
    str_res= str1[3::-1].upper() +'-'+str1[4:-4]+'-'+str1[:-5:-1].upper()
    print str_res


def task3():
    '''break the input string in middle, reverse and convert to upper'''
    str1 = raw_input("Enter any String:").upper()
    mid_point= len(str1)//2
    str_res= str1[:mid_point][::-1] +'-'+str1[mid_point:][::-1]
    print str_res

def task3_2(): #Slept
    a = "14-may-2017"
    flst = [a.split('-')[1]]
    a = "192.168.1.10:8080"
    flst.append(a.split(':')[-1]) 
    a = "10 20 30 40 50 60"
    flst.append(a.split()[:4])
    flst.append(a.split()[-4:])
    a = "10-jan-2010 16:45:32"
    flst.append(a.split())
    print flst


def task4():  
    "simple-if, if-else, if-elif-else ladder, nested if"
    str1 = raw_input("Enter a sentence:").lower().split()
    print "EQUAL" if str1[0]==str1[-1] else "NOT EQUAL"
    
def task5():
    '''example of for loop'''
    name = raw_input("Enter any Name:").lower()
    print "VOWEL" if name[-1] in "aeiou" else "CONSONANT"
        
def task6():
    '''for loop example_2 with print formatting'''
    my_list = [1234,45678,87654,90736]
    for i in map(str,my_list):
        sum = int(i[0])+int(i[-1])
        print "%-6s %s"%(i,sum)

def task7():
    ''' for each loop- convert first and last char to uppercase'''
    namelst = ["arun","hari","yash","john","guru","mani"]
    for name in namelst:
        task1(name)

def task8():
    '''test result list with test_name, expected and actuals, task: print individual test results'''
    test_list = ["test1-34-34","test2-34-56","test3-42-42","test4-10-10","test5-10-10","test6-55-50"]       
    for test in test_list:
        test = test.split("-")
        if int(test[1]) == int(test[2]):
            print "%-10s - PASS"%(test[0])
        else:
            print "%-10s - FAIL"%(test[0])


def task9():
    '''printing individual student results'''
    stud_list = ["arun-cse-blr-10,20,30,40,50,60",
                 "hari-eee-chn-10,90,65,40,66,60",
                 "jagan-eie-hyd-89,20,65,40,67,60",
                 "kiran-mech-del-98,20,99,45,78,65"]
    def print_line():
        print "------------------------------"
    print "Name      |Dept  |Total Marks|"
    print_line()
    for stud in stud_list:
        name,dept,location,marks = stud.split("-")
        total_marks = sum(map(int,marks.split(",")))
        print "%-10s|%-6s|%-11s|"%(name,dept,total_marks)
        print_line()

        
def task10():
    '''searching an employee array'''
    emplst = ["amit-blr-sales-15000",
              "ravi-chn-purchase-5000",
              "jaya-blr-accounts-35000",
              "ragu-blr-marketing-75000",
              "mishra-blr-manufacturing-90000"]
    ip_name = raw_input("Enter the employee name :").lower()
    flag = False
    for elem in emplst:
        name,location,department,salary= elem.split("-")
        if ip_name == name:
            print "Name: %-10s\nLocation: %-5s\nDepartment: %-20s\nSalary: %-20s"%(name,location,department,salary)
            flag = True
            break;
    if not flag:
        print "Name '%s' NOT FOUND"%(ip_name)
        
def task11():
    '''sorting'''
    studlist = [
               "arun-40 89 99 85 55 64",
               "ravi-56 98 34 28 19 87",
               "john-67 50 40 85 88 67",
               "ahmed-88 29 60 85 55 53"]
    for elem in studlist:
        name = elem.split("-")[0]    
        marks = map(int,elem.split("-")[1].split())
        print 
 
def tassk12():#missed
    pass    
    
def task13():
    '''finding odd and even - mani's way - usual way use %2'''
    numlst = [1,32,54,76,77,89,33,23,78,65,93]
    oddlst = []
    evenlst = []
    for elem in numlst:
        if elem in xrange(0,max(numlst)+1,2):
            evenlst.append(elem)
        else:
            oddlst.append(elem)
    print "odd :",oddlst
    print "even :",evenlst
        
def task14():
    '''Dictionary demonstration'''
    menu = {"mdosa":"50","idli":"35","pongal":"29","vada":"9"}
    order_item = raw_input("What would you like to have today??").lower()
    if order_item in menu.keys():
        print "Price : Rs.%s"%menu[order_item]
    else:
        print "Sorry, The item you entered is not available."
        
def task15():
    '''some more dictionary exercises'''
    edict = {101:"arun-blr-501-10500",102:"hari-hyd-503-15000",103:"mani-chn-502-25000",104:"joshua-tvm-505-44000"}
    dept = {501:"sales",502:"purchase",503:"R&D",504:"support",505:"marketing"}
    emp_id = int(raw_input("Enter the employee id :"))
    if emp_id in edict.keys():
        name,loc,dept,sal=edict[emp_id].split("-")
        print "Emp_id: %s\nName: %s\nLocation: %s\nDepartment: %s\nSalary: %s"%(emp_id,name,loc,dept,sal)
    else:
        print "Employee id not found"

def task16():
    ''''''
    plst = ["dvd-blr-loc1-10",
         "usb-chn-loc4-30",
         "cpu-hyd-loc3-50",
         "mon-tvm-loc2-43",
         "prn-mum-loc5-35"]
    prods={}
    for elem in plst:
        name,loc,desc,qty= elem.split('-')
        prods[name]=int(qty)
    
    for i in prods:
        print i, prods[i]


def task17():
    '''file operations'''
    f1 = open("zones.txt","w+")
    f1.write("north-Q1,43,Q2,76,Q3,54,Q4,65\n")
    f1.write("south-Q1,33,Q2,64,Q3,88,Q4,11\n")
    f1.write("east-Q1,33,Q2,49,Q3,31,Q4,65\n")
    f1.write("west-Q1,99,Q2,18,Q3,26,Q4,65\n")
    f1.seek(0,0)
    for line in f1:
        zones,quat = line.rstrip().split('-')
        qw = quat.split(',')
        numlist = map(int,qw[1::2])
        mx_val = max(numlist)
        pos = qw.index(str(mx_val))
        print zones,qw[pos-1],mx_val
    f1.close()
        
def task18():
    '''file manipulation'''
    f1 = open("studs.txt","w+")
    f1.write("group1 - 10\n")
    f1.write("group2 - 34\n")
    f1.write("group3 - 54\n")
    f1.write("group4 - 67\n")
    f1.seek(0,0)
    sum = 0
    for l in f1:
        group,num=l.rstrip("\n").split("-")
        sum += int(num)
    print sum
    f1.close()
    
def task19():
    '''more file manipulations'''
    f1 = open("data.txt","w+")
    f1.write("sample data was added\n")
    f1.write("this was an extra info\n")
    f1.write("with this some sand also added\n")
    f1.write("small infor can be done and\n")
    f1.write("and also this is it\n")
    search = raw_input("Enter the word you want to search(case-insensitive) :").lower()
    f1.seek(0,0)
    flag = False
    for ele in f1:
        if search in ele:
            print ele,
            flag = True
    if not flag:
        print "Word not found"        
    f1.close()   

def task20():
    f1 = open("emp.txt","w+")
    f1.write("arun-15000\n")
    f1.write("hari-50000\n")
    f1.write("john-25000\n")
    f1.write("maan-46000\n")
    f2 = open("out.csv","w")
    f1.seek(0,0)
    f2.write("name,salary,net\n")
    for l in f1:
        name,sal = l.rstrip().split("-")
        net = (float(sal) + (0.4*float(sal))-(0.1*float(sal)))
        f2.write("%s,%s,%s\n"%(name,sal,net))
    f1.close()
    f2.close()
    
def task21():
    '''functions'''
    def greet(str1, str2):
        if str2.lower() == "male":
            print "Hello Mr."+str1
        elif str2.lower() == "female":
            print "Hello Ms."+str1
        else:
            print "Invalid Gender"    
    name = raw_input("Enter Your Name : ")
    gender = raw_input("Enter male/female :")       
    greet(name,gender)

def task22():
    '''function_example2:'''
    def convert(li):
        res = []
        for elem in li:
            res.append(elem.capitalize())
        return res
    namelst = ["mani","arun","hari","jaya"]
    reslst = convert(namelst)
    print namelst
    print reslst
    
def task23():
    '''more function examples'''
    def display(dict1, str1):
        flag = False
        for a,b in dict1.items():
            if b == str1.lower() :
                print a
                flag =True
        if not flag:       
            print "invalid department"
    empdict = {"arun":"sales",
               "ravi":"purchase",
               "leela":"marketing",
               "john":"sales",
               "mani":"purchase"}
    search = raw_input("Enter the dept Name :")
    display(empdict,search)
    
min_cost = 0
def reductionCost(num):    
    def sum (a,b):
        global min_cost
        s = int(a)+ int(b)
        min_cost +=s
        return s
    res = reduce(lambda x,y:sum(x,y),num)
    return min_cost       
    
a = [1,2,3,4]
print reductionCost(a)


task17()