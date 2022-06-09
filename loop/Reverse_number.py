import logging
logging.basicConfig(filename = 'Reverse.log',level=logging.INFO)
num = int(input("Enter number :"))
rev=0
while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num=int(num/10)
logging.info("Reverse Number :",rev)
