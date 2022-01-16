#Purpose: takes number and returns next even number that is bigger than that number.
#input: argument a.
#post condition: returns next even number after argument a that is bigger than a.
#assumption: argument is a number (float or int)

def getNextEven(a):
    if a%2==0:
        return a+2
    elif a%2==1:
        return a+1
    elif a%2!=0:
        a=int(a)
        if a%2==0 and a>0:
            return a+2
        elif a%2==0 and a<=0:
            return a
        else:
            return a+1
    
#Test
def testGetNextEven():
    if getNextEven(2)!=4:
        print("Fail test 1")
    if getNextEven(5)!=6:
        print("Fail test 2")
    if getNextEven(6.9)!=8:
        print("Fail test 3")
    if getNextEven(5.9)!=6:
        print("Fail test 4")
    if getNextEven(-3.5)!=-2:
        print("Fail test 5")
    if getNextEven(-6.89)!=-6:
        print("Fail test 6")
    if getNextEven(0)!=2:
        print("Fail test 7")
    if getNextEven(-2)!=0:
        print("Fail test 8")
    if getNextEven(-1.2)!=0:
        print("Fail test 9")
    if getNextEven(-0.5)!=0:
        print("Fail test 10")

#Purpose: program tells you if your date is appropriate age
#Input: your age and date age argumets
#Post condition: returns one of the phrases: Your date is too youg for you,
    #You are too youg for your date or Ok, have a good time.
#assumption: arguments are numbers (int or float) and number >0 and number <=100

def datingadvice(your_age, date_age):
    if your_age<=0 or your_age>100:
        print ("The input for your age is not valid")
    elif date_age<=0 or date_age>100:
        print ("The input for date age is not valid")
    else:
        your_limit=(your_age/2)+7
        date_limit=(date_age/2)+7
        if date_age < your_limit:
            return "Your date is too young"
        elif your_age < date_limit:
            return "You are too young for your date"
        else:
            return "Ok, have a good time" 
#do I have to mention in assumprions that imput is positive and etc, if we check it in the program            


def testDatingAdvice():
    if datingadvice(22,16)!="Your date is too young":
        print("Fail test 1")
    if datingadvice(22,19)!="Ok, have a good time":
        print("Fail test 2")
    if datingadvice(17,21)!="You are too young for your date":
        print("Fail test 3")
    if datingadvice(18,21)!="Ok, have a good time":
        print("Fail test 4")
    if datingadvice(20,17)!="Ok, have a good time":
        print("Fail test 5")
    if datingadvice(20,16.9)!="Your date is too young":
        print("Fail test 6")
    if datingadvice(17.3,20.8)!="You are too young for your date":
        print("Fail test 7")
    if datingadvice(25.7,19.9)!="Ok, have a good time":
        print("Fail test 8")
    if datingadvice(20,20)!="Ok, have a good time":
        print("Fail test 10")
    if datingadvice(-10,20)!=None:
        print("Fail test 11")
    if datingadvice(20,-5)!=None:
        print("Fail test 12")
    if datingadvice(20,0)!=None:
        print("Fail test 13")

#Purpose: determine which muber wins the blackjack
#Input: two arguments a and b
#post condition: returns the biggest number that is less or equal to 21. If both numers over 21
        #returns 0
#assumption: input is a number. Number is biger then 0. 

def blackjack(a,b):
    if a<=0 and b<=0:
        print("Both values are not valid")
    elif a<=0:
        print("First value is not valid")
    elif b<=0:
        print("Second value is not valid")
    else:
        a=int(a)
        b=int(b)
        if a>21 and b>21:
            return 0
        if b>21 or (a<=21 and a-b>=0):
            return a
        elif a>21 or (b<=21 and b-a>=0):
            return b
   

#test
def testBlackjack():
    if blackjack(20,19)!=20:
        print("Fail test 1")
    if blackjack(15,17)!=17:
        print("Fail test 2")
    if blackjack(21,19)!=21:
        print("Fail test 3")
    if blackjack(5,6)!=6:
        print("Fail test 4")
    if blackjack(19,19)!=19:
        print("Fail test 5")
    if blackjack(25,7)!=7:
        print("Fail test 6")
    if blackjack(5,22)!=5:
        print("Fail test 7")
    if blackjack(26,23)!=0:
        print("Fail test 8")
    if blackjack(0,19)!=None:
        print("Fail test 9")
    if blackjack(0,0)!=None:
        print("Fail test 10")
    if blackjack(-5,19)!=None:
        print("Fail test 11")
    if blackjack(15,-9)!=None:
        print("Fail test 12")
        
