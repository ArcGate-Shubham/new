# f = open("/home/stonex/Desktop/file.txt","a")
# f.write("he is very good communcator")
# f.close()

# f = open("/home/stonex/Desktop/file.txt","r")
# print(f.read())


# f = open("/home/stonex/Desktop/file.txt","a")
# f.write("he is good communicator in this company")
# f.close()
# f = open("/home/stonex/Desktop/file1.txt","r")
# print(f.read())

# f = open("/home/stonex/Desktop/file2.txt","x")
# f = open("/home/stonex/Desktop/file2.txt","w")
# f.write("This is Arcgate,Udaipur")
# f.close()
# f = open("/home/stonex/Desktop/file2.txt","r")
# print(f.read())

# import re
# txt = "The rain in india"
# x = re.search("^The rain",txt)

# if(x):
#     print("YES! We have a match!")
# else:
#     print("No match")

# import re
# txt = "The rain in india"
# x = re.findall("[a-m]",txt)
# print(x)

# import re
# txt = "my percentage is 77 in 12th class"
# x = re.findall("\d",txt)
# print(x)

# import re
# txt = "Hello all of you in this room"
# list1 = re.findall("He..o ..l ..",txt)
# print("list1 :",list1)

# import re
# txt = "It is mainly uses in this python. it show data in use amount various procedure"
# data = re.findall("^is",txt)
# if(data):
#     print("yes, this string startswith It")
# else:
#     print("No, this is not startswith It")

# import re
# username = "abc@gmail.com"
# password = "Abc5@gmail.com"
# list1 = []
# list2 = []
# username = input("enter username: ")
# password = input("enter password: ")
# validation = re.findall("^[a-z0-9.-_]+@[a-z]+\.([a-zA-Z*]{3})+$",password)
# valid = re.findall("^[a-zA-Z0-9.-_]+@[a-zA-Z]+\.([a-zA-Z]{3})+$",username)
# if(validation and valid):
#     list1.append(username)
#     list2.append(password)
#     print(list1)
#     print(list2)
#     print("Registered succesfully!!")
# else:
#     print("Please after some time")

# user = input("Enter userid :")
# passwords = input("Enter pass")
# if(user in list1 and passwords in list2):
#     print("login successfully")
# else:
#     print("Please userid and password is invalid")

# import re
# txt = input("Enter a txt :")
# data = re.search("there",txt)
# print(data)

# import re
# txt = input("Enter data")
# data = re.search("various",txt)
# print(data)

# import re
# txt = input("Enter data")
# data = re.split("\s",txt)
# print(data)

# import re
# txt = input("Enter data :")
# data = re.sub("\s","11",txt)
# print(data)

# import re
# txt = input("Enter valid data :")
# data = re.sub("\s"," ",txt,3)
# print(data)