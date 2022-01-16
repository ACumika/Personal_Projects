#purpose: determines the temperature of the random bowl of porrige
#input: argumets low and high limits
#post condition: prints out the porrige temperature and determines if it's hot
    #cold or just right
#assumption: lo and hi limits are numbers 

def goldilocks(lo,hi):
    import random
    sum=0
    for i in range(10):
        roll=random.randint(1,6)
        sum=sum+roll
    print("The porridge is",sum,"degrees")
    if sum>hi and sum>lo:
        print("Ouch! Too hot!")
    elif sum<lo and sum<hi:
        print("Yuck! Too cold!")
    else:
        print("Yum! Just right!")

#Test cases
        #min temp we can get is 10 and max is 60.
        #Inputs: lo=10 hi=60           Expect: "The porrige is (range 10 to 60) degres", "Yum! Just right!"
        #Inputs: lo=0 hi=9             Expect: "The porrige is (range 10 to 60) degres", "Ouch! Too hot!"
        #Inputs: lo=61 hi=200          Expect: "The porrige is (range 10 to 60) degres", "Yuck! Too cold"
        #Inputs: lo=-10 hi=-4          Expect: "The porrige is (range 10 to 60) degres", "Ouch! Too hot!"
        #Inputs: lo=-10 hi=80          Expect: "The porrige is (range 10 to 60) degres", "Yum! Just right!"
        #Inputs: lo=0 hi=40            Expect: "The porrige is (range 10 to 60) degres", "Yum! Just right!" or "Ouch! Too hot!"
        #Inputs: lo=30 hi=80           Expect: "The porrige is (range 10 to 60) degres", "Yum! Just right!" or "Yuck! Too cold"
        #Inputs: lo=30 hi=40           Expect: "The porrige is (range 10 to 60) degres", "Yum! Just right!" or "Yuck! Too cold" or "Ouch! Too hot!"
        #Inputs: lo=30.5 hi=40.87      Expect: "The porrige is (range 10 to 60) degres", "Yum! Just right!" or "Yuck! Too cold" or "Ouch! Too hot!"
        #Inputs: lo="hi" hi=9          Expect: "The porrige is (range 10 to 60), Type error
        #Inputs: lo=hi hi=9            Expect: "The porrige is (range 10 to 60), Name error
        
#Purpose: count the amout of random flips that we have to do to get n number of heads
#input: argument for number of heads we want to have (n)
#Post condition: Prints out number of flips to get number of heads
#Assumption: n is a number

def headcount(n):
    if n<=0:
        print("number of heads should be above 0")
    else:
        import random
        flips=0
        heads=0
        while heads<=n-1:
            coin=random.randint(1,2)
            if coin==1:
                print("heads")
                heads=heads+1
                flips=flips+1
            else:
                print("tails")
                flips=flips+1
        print(flips, "flips to get", heads, "heads")

#Test Cases
        #input n=0         Expect: "number of heads should be above 0"
        #input n=-5        Expect: "number of heads should be above 0"
        #input n=-5.5      Expect: "number of heads should be above 0"
        #input n=5         Expect: "heads" or "tails" # times printed out, "# flips to get 5 heads"
        #input n=1.9       Expect: "heads" or "tails" # times printed out, "# flips to get 1 heads"
        #input n=1.1       Expect: "heads" or "tails" # times printed out, "# flips to get 1 heads"
        #input n=hi        Expect: Name error
        #input n="hi"      Expect: Type error

        
        
        
            
        
        
