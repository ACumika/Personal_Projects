#Purpose: getting the input from the user for some question and covert it to int type
#Input: user enters the input for the specified question (prompt)
#Post consition: returns the int variable
#Assumptions: user enters an integer
def getInput(prompt):
    response=input(prompt)
    number=int(response)
    return number

#Test Cases:
     #Enters: 80 Expect return: 80
     #Enters: -5 Expect return: -5
     #Enters: 0 Expect return: 0
     #Enters: Hi Expect return: Value Error


#Purpose: calculating how many quaters, dimes, nickels and pennies one has to use
    #for the entered amount of coins
#Input: the amount to make change 
#Post Consition: returns the amount of quaters, dimes, nickels and pennies
#Assumptions: the amount of conins is a positive number
def calculateChange(amount):
    quaters=amount//25
    dimes=(amount%25)//10
    nickels=((amount%25)%10)//5
    pennies=(((amount%25)%10)%5)
    return (quaters, dimes, nickels, pennies)
#Test Cases: 
     #amount: 80 Expect return: 3,0,1,0
     #amount: -5 Expect return: -1,2,0,0
     #amount: 0 Expect return: 0,0,0,0
     #Enters: Hi Expect return: Name Error

#Purpose: evokes getInput and calculateChange functions and prints out the answer
#Input: no input
#Post Consition: Prints put the amount of quaters, dimes, nickels and pennies one
    #has to use for the entered amount of coins
#Assumption: the amount of coins is an integer positice number
def main():
    amount=getInput("Enter the amount in cents: \n")
    quaters, dimes, nickels, pennies=calculateChange(amount)
    print("For the", amount, "coins, you should use:")
    print(quaters, "quaters,",dimes,"dimes,", nickels, "nickels and", pennies, "pennies.")
            
             
#Test Cases:
    #Enters: coins=10 Expect: quaters=0, dimes=1, nickels=0, pennies=0
    #Enters: coins=90 Expect: quaters=3, dimes=1, nickels=1, pennies=0
    #Enters: coins=43 Expect: quaters=1, dimes=1, nickels=1, pennies=3
    #Enters: coins=aa Expect: Value Error
    #Enters: coins=0 Expect: quaters=0, dimes=0, nickels=0, pennies=0
    #Enters: coins=-43 Expect: quaters=-2, dimes=0, nickels=1, pennies=2

#Extra coment on negative inputs - what happens is when we devide the negative number
    #we get some negative answer, so phyton rounds it up the other way. When we devide
    #-5 by 25 answer is -1/5 - where if we go other way we have -1 quater and 2 simes.
    #so -1 quater=-25, 2 dimes=20 theredoe we get -5. And -43 is 2 quaters minus nickel
    #and 2 pennies. It like takes as many quaters it can get and then substracts others
    #This answer would not make sence for us, so we want user to input positive number.
