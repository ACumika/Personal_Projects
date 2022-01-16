#Purpose: get input from user
#input: the question displayed to the user
#post condition: return the user input
#assumptions: no assumptions
def getInput(question):
    name=input(question)
    return name

#test GetInput:
    #input - "how are you?", user input - good    Expect: "good"
    #input - 45, user input - 900                 Expect: "900"
    #input - "eneter value", user input - ["4","g"] Expect: "["4","g"]"

#purpose: open the file 
#input: no input
#post condition: returns the text from the file or print an error of file can't be opened
#assumptions: no assumptions
def tryopen():
    filename=getInput("Enter the file name, please ")
    try:
        file=open(filename, 'r')
        try:
            linelist=file.readlines()
        finally:
            file.close()
    except IOError:
        print("Error: ", filename, "doesn not exist or it can't be opened")
        linelist=[]
    return linelist

#test tryopen:
        #user input: A8.txt         Expect: ['hello, my name is and I like to meet you today in the store,but. Polite 5 greetins are boring, so 6. gogogo 45 times and sleep good.']
        #user input: A8.ttc         Expect: "Error: A8.ttc doesn not exist or it can't be opened"
                                         #  []

#purpose: convert the list to the string
#input: the list
#post condition: returns the string
#assumption: input is a list 
def listtostring(alist):
    stringtext=" ".join(alist)
    return stringtext

def listtostringTEST():
    if listtostring(["hi 5","go"])!="hi 5 go":
        print("Failed test 1")
    if listtostring(["hi 5","go", "6,7,7."])!="hi 5 go 6,7,7.":
        print("Failed test 2")
    if listtostring(["hi 5"])!="hi 5":
        print("Failed test 3")
    if listtostring([])!="":
        print("Failed test 4")
    print("Testing finished")

#purpose: count characters, words and sentences in the text.
#input: the text
#post condition: retursn the number if characters, words and sentences
#assumption: input is a string
def count(text):
    words=text.split()
    numword=len(words)
    sent=text.split(".")
    numsent=len(sent)-1
    characters=list(text)
    numchar=len(characters)     
    return numchar, numword, numsent

def countTEST():
    if count("hello, my name is ana. I am 21 years old. Happy Thanksgiving.")!=(61, 12, 3):
        print("Failed test 1")
    if count("hello, my name is ana")!=(21, 5, 0):
        print("Failed test 2")
    if count("")!=(0,0,0):
        print("Failed test 3")
    print("Testing finished")

#purpose: create a list of words from the text given 
#input: the text
#post condition: return the list of words 
#assumption: input is a string
def listallwords(text):
    words=text.split()
    return words

def listallwordsTEST():
    if listallwords("hello, my name is Ana.")!=["hello,","my","name","is","Ana."]:
        print("Failed test 1")
    if listallwords("hello")!=["hello"]:
        print("Failed test 2")
    if listallwords("")!=[]:
        print("Failed test 3")
    print("Testing finished")
    
#purpose: delte the periods and comas at the end of the words in the list
#input: the lsit of words
#post condition: return the list of words without periods and comas
#assumptions: input is a list
def deleteperiods(words):
    newwords=[]
    for j in words:
        if "." in j or "," in j:
            jn=j[:len(j)-1]
            newwords.append(jn)
        else:
            newwords.append(j)
    return newwords

def deleteperiodsTEST():
    if deleteperiods(["hello,","my","name","is","Ana."])!=["hello","my","name","is","Ana"]:
        print("Failed test 1")
    if deleteperiods(["hello","my","name","is","Ana"])!=["hello","my","name","is","Ana"]:
        print("Failed test 2")
    if deleteperiods(["hello"])!=["hello"]:
        print("Failed test 3")
    if deleteperiods(["."])!=[""]:
        print("Failed test 4")
    print("Testing finihsed")

#purpose: check if the parameter can be converted to the float type
#input: the parameter 
#post condition: return Ture if the parameter can be converted and False if the valueError occures.
#assumptions: no assumptions
def errorValue(parameter):
    try:
        float (parameter)
        return True
    except ValueError:
        return False
    except TypeError:
        return False

def errorValueTEST():
    if errorValue("go")!=False:
        print("Failed test 1")
    if errorValue("4")!=True:
        print("Failed test 2")
    if errorValue("4.5")!=True:
        print("Failed test 3")
    if errorValue("0")!=True:
        print("Failed test 4")
    if errorValue(True)!=True:
        print("Failed test 5")
    if errorValue(["5"])!=False:
        print("Failed test 6")
    if errorValue(("df",5,6))!=False:
        print("Failed test 6")
    print("Testing finihsed")
    
#purpose: sum all the numbers from the text
#input: the text
#post condition: return the sum fo the numbers
#assumption: input is a string
def summ(text):
    wordlist=listallwords(text)
    listnodots=deleteperiods(wordlist)
    summ=0
    for i in listnodots: 
        if errorValue(i):
            num=float(i)
            summ=summ+num
    return summ

def summTEST():
    if summ("hello 5 guys and 4 boys. total 9.")!=18:
        print("Failed test 1")
    if summ("hello.")!=0:
        print("Failed test 2")
    if summ("hello 5, 6, 7.")!=18:
        print("Failed test 3")
    if summ("hello 54. 9.")!=63:
        print("Failed test 4")
    if summ("hello 5, 5.6, 4.")!=14.6:
        print("Failed test 5")
    if summ("")!=0:
        print("Failed test 6")
    print("Testing finished")
           
#purpose: count how many vowels there are in the text
#input: the text
#post condition: return number of vowels in the text
#assumptions: input is a text
def vowelsnum(text):
    count=0
    for i in text:
        character=list(i)
        vowels="aeiouAEIOU"
        for k in character:
            if k in vowels:
                count=count+1
    return count

def vowelsnumTEST():
    if vowelsnum("hello, how are you")!=7:
        print("Failed test 1")
    if vowelsnum("Ego")!=2:
        print("Failed test 2")
    if vowelsnum("ghtr")!=0:
        print("Failed test 3")
    if vowelsnum("")!=0:
        print("Failed test 4")
    print("Testing finished")
#purpose: open the file with the text and display number of characters, words, sentences, vowels and the total sum of the numbers in the text
#input: no input
#post condition: display number of characters, words, sentences, vowels and the total sum of the numbers in the text
#assumptions: no assuptions
def main():
    filetext=tryopen()
    strtext=listtostring(filetext)
    coun=count(strtext)
    numsum=summ(strtext)
    numvav=vowelsnum(strtext)
    print("There are", coun[0], "characters,", coun[1], "words, and", coun[2], "sentences.")
    print("Total sum of the numbers in the text is: ", summ(strtext))
    print("Total number of vowels in the text is: ", vowelsnum(strtext))

#TEST main funciton:
    #user input: A8.txt   Expect: "There are 132 characters,27 words, and 3 sentences."
                                # "Total sum of the numbers in the text is: 56"
                                # "Total number of vowels in the text is: 42"
    #user input: A8.ttx   Expect: Error:  j doesn not exist or it can't be opened
                                # There are 0 characters, 0 words, and 0 sentences.
                                # Total sum of the numbers in the text is:  0
                                # Total number of vowels in the text is:  0
    

