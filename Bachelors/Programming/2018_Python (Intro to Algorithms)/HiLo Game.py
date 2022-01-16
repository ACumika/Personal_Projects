#purpose: get input from the user and return it
#Input: A question that the user will see
#Post condition: returns the user respond
#Assumptions: the question is a str, int or float. ???

def getFromUser(question):
    respond=input(question)
    return respond

#Purpose: let computer pick a random integer number between some high and low limits
#Input: high and low limits
#post condition: returns an integer between hi and lo
#Assumptions: hi and lo limits are integers
def pickRandom(hi,lo):
    import random
    number=random.randint(lo,hi)
    return number

def guesscheck(realnum, num):    
    if num<realnum:
        print("Too low!")
    else:
        print("Too hight!")

def checklimits(realnum, num, count, hi, lo):
    if num>hi or num<lo:
        num=int(getFromUser("Please enter a number between " + str(lo) + " and " + str(hi) + ":  "))
    else:
        count=count+1
        guesscheck(realnum,num)
        num=int(getFromUser("Enter a guess from " + str(lo) + " to " + str(hi)+": "))
    tuples=(num,count)
    return tuples

def repeatguess(realnum, hi, lo):
    count=1
    num=int(getFromUser("Enter a guess from " + str(lo)+" to "+str(hi)+": "))
    while num!=realnum:
        tuples=checklimits(realnum, num, count, hi, lo)
        num=tuples[0]
        count=tuples[1]
    print("Correct!")
    return count


#purpose: ask user a question that requers y or n answer and keeps asking
    #for a bew answer until its y or n.
#Input: the question we want to ask the user
#Post condition: returns y or n
#Assumptions: same as 1 def (question str int float ???)
def yesno(question):
    yn=getFromUser(question)
    while yn!="n" and yn!="y":
        yn=getFromUser("Please reenter the answer, it should be y or n: ")      
    return yn

def hiLoGame(lo,hi):
    yn="y"
    while yn=="y":
        print("Welcome to the Hi-Lo game!")
        print("I am thinking of a number from", lo, " to", hi, "Guess what it is")
        number=pickRandom(hi,lo)
        count=repeatguess(number, hi, lo)
        print("You used", count, "guesses")
        yn=yesno("Would you like to play again?(y/n)? ")
        print("      ")
    
                        
#purpose: evokes funcions to play hilo game until user does not want to play again
#input:no input
#post condition: runs the game over and over if user says y and exits if user says n
#assumption:???
def main():
    hiLoGame(1,20)


    
