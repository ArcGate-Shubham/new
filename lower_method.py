# data = input("Enter data")
# print(data.lower())

# import random
# x = random.randint(2,4)
# #rand = random.random(x
# print(x)

# import math
# a = "shubham"
# b = 25
# c = f"He is {a} and age is {b} and passed on {math.cos(0)}"
# print(c)


# list1 = ["Shubham","Vijay","Kartik","vikas"]
# for index,items in enumerate(list1):
#     if(index%2==0):
#         print(f"Bhidi buy from {items}")

# list2 = ["ajay","vikas","teena","vijay",12,13,23]
# print(len(list2))
# for index,items in enumerate(list2):
#     if(index%2==0 and list2.pop()):
#         print(f"value as show of list in {items}")

# def function1(a,b):
#     return a+b
# print(function1(2,4))

# def function2(*args):
#     c=0
#     for num in args:
#         c += num
#     return c

# print(function2(12,131,13,14,15))

# def function3(*args):
#     v=0
#     for num in args:
#         if(num%2==0):
#             v = v + num
#         v+=1
#         return num
# print(function3(12,13,14,154))

# def product(num,num1,*args):
#     product = 1
#     print(num)
#     print(num1)
#     print(args)
#     for x in args:
#         product+=x
#     return product

# print(product(2,3,3,4))

# def function4(*args):
#     product = 0
#     print(args)
#     for i in args:
#         product *=i
#     return product
# num =[23,4,56]
# print(function4(*num))

# def function4(num,*args):
#     if(args):
#         return [i**num for i in args]
#     else:
#         print("you didn't pass any value")

# nums = [4,5,6]
# print(function4(3,*nums))

# def function5(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# function5()

# def add(a,b):
#     return a+b

# def new_add(n,*args):
#     s=0
#     for num in args:
#         s = s + num
#         print(s,end=",")
#     return s

# print(new_add(2,3,4,5))

# event = lambda a: a%2==0
# print(event(5))

# eodd = lambda a,b : int(a/b)
# print(eodd(6,4))

# evenData = lambda a : a==5
# num= int(input("Enter number :"))
# print(evenData(num))

# oddData = lambda a,b : "Data is valid"  if(a*b>=100) else "Data is not valid"
# a = int(input("Enter number :"))
# b = int(input("Enter number :"))
# print(a*b)
# print(oddData(a,b))
# print(oddData)


# def add(a,b):
#     return a+b+5
# def minus(a,b):
#     return a-b

# print(minus(13,12))
# s=add(12,13)
# print(s)

# list1 = ["Akash","vikas","vaibhav","shubham","priya"]
# list2 = " ".join(list1)
# print(list2)

# set1 = {"vikas","vijay","teena","veena"}
# set2 = " ".join(set1)
# print(set2)


# numbers = ["2","34","65","78"]
# numbers = list(map(int,numbers))
# numbers[3]= numbers[3]+34
# print(numbers[3])

#string4 = input("Enter data :")
# list1 = []
# num = int(input("Enter number for append in list1 :"))
# for x in range(num):
#     name = input("Enter number for a list :")
#     if(name):
#         list1.append(name)
#     else:
#         print("value is not valid!!")
# print(list1)
# square = list(map(lambda x: x*x,list1))
# print(square)


# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a

# def fourth(a):
#     return a*a*a*a
# func = [square,cube,fourth]
# num = int(input("Enter nustring4 = input("Enter data :")mber :"))
# for i in range(num):
#     value = list(map(lambda x : x(i),func))
#     print(value)

# basic= [1,2,3,4,5,6,7,8,9]
# def greater(num):
#     return num>4

# list1 = list(filter(greater,basic))
# print(list1)

# from functools import reduce
# list1 = [11,12,13,14,15]
# num = reduce(lambda x,y : x+y, list1)
# print(num)

# from functools import reduce
# list1 = []
# num = int(input("Enter Number :"))
# for x in range(num):
#     name = int(input("Enter value :"))
#     if(name>=10):
#         list1.append(name)
#     else:
#         print("Data is not valid !!")
# print(list1)
# list2 = ["ajay","vikas","teena","vijay",12,13,23]
# print(len(list2))
# for index,items in enumerate(list2):
#     print(f"this value present on this {index} for this {items}")
# nums = reduce(lambda x,y : x+y,list1)
# print(nums)

# list1 = []
# for x in range(1,11):
#     list1.append(x**5)
# print(list1)

# list1 = [x**2 for x in range(1,4)]
# print(list1)

# list1 =[12,11,34,67,78,90]
# list2 = iter(list1)
# print(next(list2))
# print(next(list2))
# print(next(list2))
# print(next(list2))
# print(next(list2))
# print(next(list2))

# list1 = []
# list2 = []
# num =int(input("Enter number :"))
# for x in range(num):
#     name = input("Enter value :")
#     if(name.isalpha()):
#         list1.append(name)
#     elif(name.isnumeric()):
#         list2.append(name)
#         list2 = list(map(int,list2))
#     else:
#         print("Please Enter valid information")
# print(list1)
# print(list2)
# x=list(zip(list1,list2))
# print(x)
# print(dict(x))

# squares = { num : num%2==0 for num in range(1,11)}
# print(squares)

# list2 = ["ajay","vikas","teena","vijay",12,13,23]
# print(len(list2))
# for index,items in enumerate(list2):
#     print(f"this value present on this {index} for this {items}")

# def funct(num, *args):
#     if(args):
#         return [i**num for i in args]
#     else:
#         print("This data is not valid!!")

# nums = [1,2,3]
# print(funct(3,*nums))


# def functionvalue(*args):
#     product = 1
#     print(args)
#     for i in args:
#         product*=i

#     return product

# num = [11,12,13]
# print(functionvalue(*num))

# def functiondata(*args):
#     s=0
#     for i in args:
#         if(i%2==0):
#             s+=i
#     return s

# num = [11,12,15,14]
# print(functiondata(*num))

# def functionpass(*args):
#     s=0
#     r=1
#     for i in args:
#         if(i>10):
#             s+=i
#         else:
#             r*=i
#     return s,r

# num = [23,56,8,13,2,3,89]
# print(functionpass(*num))

# list1=[]
# def fun():
#     num = int(input("Enter number :"))
#     for x in range(num):
#         data = input("Enter number in append on a list :")
#         if(data.isnumeric()):
#             list1.append(data)
#         else:
#             print("Data is not valid")
#     print(list1)
# print(list1)
# fun()
# list1 = list(map(int,list1))
# print(list1)
# s=0
# r=1
# for x in list1:
#     if(x%2==0):
#         s+=x
#     else:
#         r*=x
# print(s,r)

# squares = {f"square of {num} is": num**2 for num in range(1,11)}
# print(squares)
# for i,j in squares.items():
#     print(f"{i} : {j}")

# data = {f"cube of {num} is":num**3 for num in range(1,6)}
# print(data)
# for x,y in data.items():
#     print(f"{x} : {y}")

# data =  {f"squares of {num} is":num**4 for num in range(1,11)}
# print(data)
# for x,y in data.items():
#     print(f"{x} : {y}")

# string1 = 'Shubham'
# add = {char : string1.count(char) for char in string1}
# print(add)

# string2 = input("Enter number :")
# dataset = { char : string2.count(char) for char in string2}
# print(dataset)

# string3 = input("Enter various data :")
# datavalue = { data : string3.find(data) for data in string3}
# print(datavalue)

# list2 = ["shubham","vijay","vikas"]
# print(len(list2))
# for index,data in enumerate(list2):
#     print(f"this {index} is various {data} process")

# import re
# class College:
#     list1 = []
#     list2 = []
#     def college(self):
#         self.username= input("Enter username :")
#         self.password = input("Enter password :")
#         self.valid_username = re.findall("^[a-zA-Z0-9]+@[a-zA-Z]+\.([a-z]{3})+$",self.username)
#         self.valid_password = re.findall("^([a-z]{5})+([A-Z]{1})+([@!#$%]{1})+([0-9])+$",self.password)
#         if(self.valid_username and self.valid_password):
#             self.list1.append(self.username)
#             self.list2.append(self.password)
#         else:
#             print("This username and password is not valid for this requirement")
#         print(self.list1)
#         print(self.list2)
        
#     def login(self):
#         v=1
#         while(v):
#             try:
#                 self.usernames = input("Enter student username :")
#                 v=0
#                 self.passwords = input("Enter student password :")
#                 v=0
#                 if(self.usernames in self.list1 and self.passwords in self.list2):
#                         print("login successfully")
                        
#                 else:
#                         print("Data is not valid for given information")
#             except:
#                 print("given data is not callable")
# c=College()
# c.college()
# c.login()

# import re
# txt = "this is various process in there path"
# x = re.split("\s",txt)
# print(x)

# import re
# txt = "this is various process in there path"
# x = re.sub("\s","9",txt,3)
# print(x)

# import re
# txt = "this is various path of variount protocol. it will show data set."
# x = re.sub("\s","9",txt,3)
# print(x)

import re
txt = "This is various path of various process."
x = re.sub("\s","11",txt,2)
print(x)
