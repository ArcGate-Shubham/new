# import logging
# logging.basicConfig(level=logging.DEBUG,filename="app.log")
# def add(x,y):
#     return x+y
   
# def sub(x,y):
#     return x-y

# def pro(x,y):
#     return x*y

# def div(x,y):
#     return x/y

# a=13
# b=11
# add_result = add(a,b)
# logging.debug("Add:{}+{}={}".format(a,b,add_result))

# sub_result = sub(a,b)
# logging.debug("sub:{}-{}={}".format(a,b,sub_result))

# pro_result = pro(a,b)
# logging.debug("pro:{}*{}={}".format(a,b,pro_result))

# div_result = div(a,b)
# logging.debug("div:{}/{}={}".format(a,b,div_result))

import logging
logging.basicConfig(level=logging.DEBUG,filename="app.log")
def data():
    data_set = []
    data_value = []
    num = int(input("Enter a number :"))
    for x in range(num):
                    name = input("Enter name :")
                    v=0
                    if(name.isalpha()):
                        data_set.append(name)
                    elif(name.isnumeric()):
                        data_value.append(name)
                    else:
                        logging.debug("This is service is not available")
                
    logging.debug(data_set)
    logging.debug(data_value)
data()
    
        
            