#Purpose: converting amount of years to the amount of month and printing the answer
#Input: the amount of years
#Post conditions: prints out amount of month in years if years>0 and tells that invalid
    #inout if years<0
#Assumptions: argument is a number (not a str)
def months (years):
    if years<=0:
        print("invalid number of years")
    else:
        month=years*12
        print(month, "months in", years, "years")

#Test cases:
        #Input: years=2      Expect: month=24
        #Input: years=5      Expect: month=60
        #Input: years=0      Expect: "invalid number of years"
        #Input: years=2.5    Expect: month=30
        #input: years=2.4987 Expect: month=29.9844
        #Input: years=-2     Expect: "invalid number of years"
        #Input: years=-2.5   Expect: "invalid number of years"
        #Input: years="two"  Expect: TypeError


#Purpose: find the max number of the three integers
#Input: a, b and c integers
#Post conditions: returns the max number out of three integers
#Assumptions: argument is a number (not a str)
def getMax(a,b,c):
    if a>=b and a>=c:
        Max=a
        return a
    elif b>a and b>=c:
        Max=b
        return b
    else:
        Max=c
        return c

#Test Cases:
    #Input: a=5, b=3, c=1              Expect: 5
    #Input: a=5, b=1, c=3              Expect: 5
    #Input: a=3, b=6, c=0              Expect: 6
    #Input: a=5, b=7, c=6              Expect: 7
    #Input: a=1, b=3, c=4              Expect: 4
    #Input: a=4, b=3, c=5              Expect: 5
    #Input: a=2, b=2, c=2              Expect: 2
    #Input: a=0, b=0, c=0              Expect: 0
    #Input: a=5, b=-5, c=-8            Expect: 5
    #Input: a=-8, b=-9, c=-10          Expect: -8
    #Input: a=8.65, b=1.25, c=1.8      Expect: 8.65
    #Input: a=-8.58, b=-9.14, c=-1.49  Expect: -1.49
    #Input: a="five", b=3, c=1         Expect: TypeError
    #Input: a="hi", b="five", c="bla"  Expect: TyprError
    
    
#Purpose: describe the weather depending on the temperature
#Input: the temperature 
#Post conditions: returns the describtion of the weather
#Assumptions: argument is a number (not a str)
def weather(temp):
    if temp>=90:
        return "Going to be a scorcher"
    elif temp>=80:
        return "Its hot out there!"
    elif temp>=50:
        return "Beautiful day!"
    elif temp>=35:
        return "Relatively mild"
    else:
        return "Brrr... its cold!"

#Test Cases:
    #Input: temp=115    Expect: Going to be a scorcher
    #Input: temp=90     Expect: Going to be a scorcher
    #Input: temp=85     Expect: Its hot out there!
    #Input: temp=80     Expect: Its hot out there!
    #Input: temp=64     Expect: Beautiful day!
    #Input: temp=50     Expect: Beautiful day!
    #Input: temp=41     Expect: Relatively mild
    #Input: temp=35     Expect: Relatively mild
    #Input: temp=20     Expect: Brrr... its cold!
    #Input: temp=0      Expect: Brrr... its cold!
    #Input: temp=-15    Expect: Brrr... its cold!
    #Input: temp=50.89  Expect: Beautiful day!
    #Input: temp=40.95  Expect: Relatively mild
    #Input: temp=-21.21 Expect: Brrr... its cold!
    #Input: temp="cold" Expect: TypeError
    
        
    
    


    
