#Purpose: get input from user
#input: the question displayed to the user
#Post condition: returns user input
#Assumption: no assumptions
def getinput(query):
    variable=input(query)
    return variable

#test GetInput:
    #input - "how are you?", user input - good    Expect: "good"
    #input - 45, user input - 900                 Expect: "900"
    #input - "eneter value", user input - ["4","g"] Expect: "["4","g"]"

#purpose: get user input for hours in between 1 and 10
#input: no input
#post condition: retuns hours entered that fits the range 1 to 10
#Assumptions: no assumptions
def hoursenter():
    hours=getinput("Enter hours: ")
    while hours not in ["1","2","3","4","5","6","7","8","9","10"]:
        print("Please Enter a number between 1 and 10")
        hours=getinput("Enter hours: ")
    hours=int(hours)
    return hours

#test hoursenter:
    #user input: 3         Expect: 3
    #user input: 0         Expect: "Please Enter a number between 1 and 10"
    #user input: 10        Expect: 10
    #user input: "hello"   Expect: "Please Enter a number between 1 and 10"
    #user input: -3        Expect: "Please Enter a number between 1 and 10"
    #user input: True      Expect: "Please Enter a number between 1 and 10"
    #user input: [4,5]     Expect: "Please Enter a number between 1 and 10"
    #user input: {"G":"5"} Expect: "Please Enter a number between 1 and 10"
    
#Purpose: get user input as yes or no
#input: no input
#post condition: return yes or no (Yes or No)
#assumptions: no assumptions
def moreshifts():
    answer=getinput("More Shifts? ")
    while answer!="no" and answer!="yes" and answer!="No" and answer!="Yes":
        print("Please enter Yes or No for the answer")
        answer=getinput("More Shifts? ")
    return answer

#test moreshifts:
    #user input: yes             Expect: "yes"
    #user input: Yes             Expect: "Yes"
    #user input: no              Expect: "no"
    #user input: No              Expect: "No"
    #user input: 4               Expect: "Please enter Yes or No for the answer"
    #user input: [4,5]           Expect: "Please enter Yes or No for the answer"
    #user input: True            Expect: "Please enter Yes or No for the answer"
    #user input: {"G":"5"}       Expect: "Please enter Yes or No for the answer"
    #user input: Hello           Expect: "Please enter Yes or No for the answer"

#Purpose: get input from user about the person shift
#input: no input
#post condition: return worker name, hours worked during the shift and yes/no
    #if there are more shifts to be entered
#assumptions: no assumptions
def shiftenter():
    name=getinput("Eneter name: ")
    hours=hoursenter()
    moreshift=moreshifts()
    print("")
    return name, hours, moreshift

#test shiftenter:
    #User input: Name - Ana                            Excpect: Ana, 4, yes
    #            hours - 4
    #            more shifts - yes
    #User input: Name - Ana                            
    #            hours - 67                            Excpect: Please Enter a number between 1 and 10
    #            hours-7
    #            more shifts - N                       Excpect: Please enter Yes or No for the answer
    #            more shifts - No                      Excpect: Ana, 7, No
    


#purpose: create a dictionary with hours worked assigned to the workers
#input: no input
#post condition: return a dictionary with total hours worked assign to specific worker
#assumption: no assumptions
def dictionary():
    moreshift="yes"
    shiftlog={}
    while moreshift=="yes" or moreshift=="Yes":
        shift=shiftenter()
        if shift[0] in shiftlog:
            shiftlog[shift[0]]=shiftlog[shift[0]]+shift[1]
        else:
            shiftlog[shift[0]]=shift[1]
        moreshift=shift[2]  
    return shiftlog

#test dictionary:
    #User input: Name - Ana                            
    #            hours - 4
    #            more shifts - yes
    #            
    #            Name - Kevin                            
    #            hours - 67                            Excpect: Please Enter a number between 1 and 10
    #            hours-7
    #            more shifts - N                       Excpect: Please enter Yes or No for the answer
    #            more shifts - Yes
    #
    #            Name - Ana
    #            Hours - 9
    #            more shifts - No                      Excpect: {"Ana":13, "Kevin":7}
    

#purpose: sort the dictionary keys in the alphabetical order 
#inputs: the dictionary
#post conditions: return a list of dictionary keys in alphabetical order
#assumptions: input is type dict 

def keylistsorted(dictionary):
    alist=[]
    for k in dictionary:
        alist.append(k)
    alist.sort()
    return alist

def keylistsortedTEST():
    if keylistsorted({"Ana":5,"Clover":9,"Simon":5,"Becca":34,"Balen":1,"Meg":5})!=["Ana","Balen","Becca","Clover","Meg","Simon"]:
        print("Failed test 1")
    if keylistsorted({"Ana":5,"Balen":1,"Becca":34,"Clover":9,"Meg":5,"Simon":5})!=["Ana","Balen","Becca","Clover","Meg","Simon"]:
        print("Failed test 2")
    if keylistsorted({"Ana":5})!=["Ana"]:
        print("Failed test 3")
    if keylistsorted({})!=[]:
        print("Failed test 4")
    print("Testing finished")

#purpose: display how many hours each worker worked total this week
#input: dictionary with names and hours
#post condition: prints workers names in alphabetical order with correxpoding total hours worked
#assumption: input is type dict

def totworked(dictionary):
    alist=keylistsorted(dictionary)
    for k in alist:
        print(k, dictionary[k])

#test totalworked:
    #input: {"Ana":5,"Clover":9,"Simon":5,"Becca":34,"Balen":1,"Meg":5}  Expect: Ana 5 Balen 1 Becca 34 Clover 9 Meg 5 Simon 5
    #input: {"Ana":5}                                                    Expect: Ana 5
    #input: {}                                                           Expect:


#purpose: find max number in dictionary values
#input: dictionary 
#post condition: retuns max number in dictionary values
#assumption: input is tyoe dict with values that are positive numbers
def maxnum(dictionary):
    maxnum=0
    for i in dictionary.values():
        if i>maxnum:
            maxnum=i
    return maxnum

def maxnumTEST():
    if maxnum({"Ana":5,"Clover":9,"Simon":5,"Becca":34,"Balen":1,"Meg":5})!=34:
        print("Failed test 1")
    if maxnum({"Ana":5,"Clover":9,"Simon":9,"Becca":3,"Balen":1,"Meg":5})!=9:
        print("Failed test 2")
    if maxnum({"Ana":5})!=5:
        print("Failed test 3")
    if maxnum({})!=0:
        print("Failed test 4")
    print("Testing finished")

#purpose: display the workres that morked the most hours with their total hours
#input: dictionary with worker names and hours 
#post condition: prints worker names(in alphabetical order) with max hours worked and with "**" in front of their names
#assumprions: input is type dict with values that are positive numbers
def maxnumdict(dictionary):
    maxn=maxnum(dictionary)
    alist=keylistsorted(dictionary)
    for i in alist:
        if dictionary[i]==maxn:
                print("**"+i, dictionary[i])

#test maxnumdict:
        #input:{"Ana":5,"Clover":9,"Simon":5,"Becca":34,"Balen":1,"Meg":5}       Expect: **Beccd 34
        #input:{"Ana":5,"Simon":9,"Clover":9,"Becca":3,"Balen":1,"Meg":5}        Expect: **Clover 9 **Simon 9
        #input:{"Ana":5}                                                         Expect: **Ana 5
        #input:{}                                                                Expect:

#purpose: compute the avarage number of the of all the dictionary values
#input: dictionary
#post condition: returns the avarage of the dictionary values
#assumptions: input is type dict with values that are numbers
def averagenum(dictionary):
    summ=0
    n=0
    for i in dictionary.values():
        summ=summ+i
        n=n+1
    if n!=0:
        av=summ/n
    else:
        av=0
    return av

def averagenumTEST():
    if averagenum({"Ana":5,"Clover":9,"Simon":5,"Becca":34,"Balen":2,"Meg":5})!=10:
        print("Failed test 1")
    if averagenum({"Ana":5,"Meg":5})!=5:
        print("Failed test 2")
    if averagenum({"Ana":5})!=5:
        print("Failed test 3")
    if averagenum({})!=0:
        print("Failed test 4")
    print("Testing finished")
        
#purpose: display workers that worked at least avarage hours this week with their hours
#input: dictionary with worker names and hours
#post condition: prints worker names (in alphabetical order) that worked at least avarage with their total hours and "*" before their names
#assumptions: input is type dict with values that are numbers
def workersaboveav(dictionary):
    average=averagenum(dictionary)
    alist=keylistsorted(dictionary)
    for i in alist:
        if dictionary[i]>=average:
            print("*"+i , dictionary[i])

#test workersaboveav:
        #input:{"Ana":5,"Clover":9,"Simon":5,"Becca":34,"Balen":2,"Meg":5}    Expect: *Becca 34
        #input:{"Meg":7,"Ana":5,"Clover":9,"Simon":5,"Becca":3,"Balen":2}     Expect: *Clover 9 *Meg 7
        #input:{"Ana":5,"Meg":5}                                              Expect: *Ana 5 *Meg 5
        #input:{Ana":5}                                                       Expect: *Ana 5
        #input:{}                                                             Expect: 

def main():
    shifts=dictionary()
    totworked(shifts)
    maxnumdict(shifts)
    workersaboveav(shifts)

#Test main:
    #User input: Name - Ana                            
    #            hours - 3
    #            more shifts - yes
    #            
    #            Name - Kevin                            
    #            hours - 67                            Excpect: Please Enter a number between 1 and 10
    #            hours-7
    #            more shifts - N                       Excpect: Please enter Yes or No for the answer
    #            more shifts - Yes
    #
    #            Name - Ana
    #            Hours - 9
    #            more shifts - yes
    #
    #            Name - Becca
    #            Hours - 1
    #            more shifts - no                     Excpect: Ana 12 Becca 1 Kevin 7 **Ana 12 *Ana 12 *Kevin 7 


    
    
    

    
    
