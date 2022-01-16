#1
#purpose: count number of letters appearing in the given strin query
#input: the string query
#post condition: prints out how many times each letter appeared in the string
#asumptions: input is a string 
def frequencies(query):
    import string
    letters=string.ascii_letters
    msg=""
    for i in letters:
        count=query.count(i)
        if count>0:
            count=str(count)
            msg=msg+i+":"+count+" "  
    print (msg)

#test cases
    #Input:   "hello there"   Expect: e:3 h:2 l:2 o:1 r:1 t:1
    #Input:   "HELLO there"   Expect: e:2 h:1 r:1 t:1 E:1 H:1 L:2 O:1
    #Input:   "aAaAaAaAaA"    Expect: a:5 A:5
    #Input:   "12H45tF%&5hj"  Expect: h:1 j:1 t:1 F:1 H:1
############################################################################
#2-get key
    
#Purpose: produce a sting of all lowercase letters
#input: no input
#post condition: returns a string of lowercase letters in alphabetical order
#asumptions: no assumptions
def letters():
    import string
    letters=string.ascii_lowercase
    return letters

#Purpose: choose a random character from the given string or list element from the  list
#Input: string or list
#post condition: returns randomly selected character or a list element
#assumption: input is a list or a string
def randomletter(letters):
    import random
    alen=len(letters)
    i=random.randint(0,alen-1)
    character=letters[i]
    return character

#purpose: mixes up an order of the characteres in the string (without repitition)
#input: a string
#post condition: returns a new string with same characters but different order
#assumption: input is a string
def concatination(letters):
    key=""
    l=len(key)
    while l<26:
        character=randomletter(letters)
        key=checkletterinkey(key, character)
        l=len(key)
    return key

#purpose: if the string does not have the character adds this character to the string
#input: a string and a character 
#post conditon: returns a string
#assumptions: string and a character are str type
def checkletterinkey(string, character):
    if character not in string:
        string=string+character
    return string

#purpose: makes a key from the alphabet of lowercase letters
#input: no input
#post condition: returns a key
#assumptions: variable a is a str type
def getkey():
    a=letters()
    key=concatination(a)
    return key
###################################################################################################################
#centered average
#purpose: delete the items of the list that are not numbers
#input: the list
#post condition: returns new list of numbers
#assumption: input is a list
def deletenotnum(lis):
        newlist=[]
        for i in lis:     
            if type(i)==int or type(i)==float:
                newlist.append(i)
        return newlist
                
#purpose: find the lowest number is the list
#input: the list
#post condition: returns the lowest number
#assumption: input is a list of numbers
def lowestnum(lis):
    import math
    k=math.inf      
    for i in lis:
        if i<k:
            minnum=i
            k=i
    return minnum

#purpose: find the highest number is the list
#input: the list
#post condition: returns the highest number
#assumption: input is a list of numbers
def highestnum(lis):
    import math
    k=-math.inf
    for i in lis:
        if i>k:
            maxnum=i
            k=i
    return maxnum

#purpose: delte the specific item from the list if it is in the list
#input: the item to delete and the list
#post condition: returns the new list without the item
#assumptions: input is a list 
def findnum(item, lis):
    if item in lis:
        numind=lis.index(item)
        del lis[numind]
    return lis

#Purpose: summ all the numbers in the list
#input: the list
#post condition: returns the sum of the numbers
#assumptions: input is a list of numbers
def sumnum(lis):
    summ=0
    for i in lis:
        summ=summ+i
    return summ

#purpose: deletes not numbers items, min and max numbers from the list
#input: the list
#post condition: returns a new list
#assumptions: input is a list
def newlist(lis):
    liss=deletenotnum(lis)
    minn=lowestnum(liss)
    maxn=highestnum(liss)
    liss=findnum(maxn, liss)
    liss=findnum(minn, liss)
    return liss

#purpose: calculates the centered avarage of the list
#input: the list
#post condition: returns the centered average
#assumption: input is a list
def checklen(lis):
    lis=deletenotnum(lis)
    l=len(lis)
    if l<=2:
        av=0
    else:
        lis=newlist(lis)
        summ=sumnum(lis)
        devis=len(lis)
        av=summ/devis
    return av

#purpose: runs the functions to get centered average of the list
#input: the list
#post condition: returns centered average
#assumptions: input is a list
def centered_avg(lis):
    av=checklen(lis)
    return av

#test function for centered average function
def testCentered_avg():
    if centered_avg([2,3,7,4,2,45,7])!=4.6:
        print("Failed test 1")
    if centered_avg([1,2,3])!=2:
        print("Failed test 2")
    if centered_avg([1,2])!=0:
        print("Failed test 3")
    if centered_avg([4])!=0:
        print("Failed test 4")
    if centered_avg([])!=0:
        print("Failed test 5")
    if centered_avg(["e","45","5"])!=0:
        print("Failed test 6")
    if centered_avg([2,"r","rt",7])!=0:
        print("Failed test 7")
    if centered_avg([2,"f","45",4,7])!=4:
        print("Failed test 8")
    if centered_avg([2,3,7,True,7])!=5:
        print("Failed test 9")
    if centered_avg([2,3,7,["v",5,5],7])!=5:
        print("Failed test 10")
    if centered_avg([4,5,True,"f",98,[4,4]])!=5:
        print("Failed test 11")   
    print("Testing completed!")


    

    
