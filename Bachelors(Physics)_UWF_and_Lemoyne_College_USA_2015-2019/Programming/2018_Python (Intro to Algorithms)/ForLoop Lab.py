#Purpose: create a triange of stars of specific size
#input:number N that determines size of a triangle
#post condition: prints out a triangle of stars of desired size
#assumptions:N is a positive integer
def stars_triangle(N):
        for j in range(N, 0, -1):
            print("*"*j)

#Purpose: create a specific size grid of stars and dots where each consequtive line subs one star with one dot
#input:number N that determines size of a grid
#post condition: prints out the grid of NxN size
#assumptions:N is a positive integer
def stars_and_dots(N):
        for j in range(N, 0, -1):
            dots=N-j
            print(dots*"." + j*"*")

#Purpose: takes n number of last characters of the string and repeats it n times
#input: a string that is used and number n
#post condition: returns last n characters of the string n times (no space)
#Assumptions: n is a positive integer
def repeatEnd(string, n):
        string=str(string)
        l=len(string)
        if n<0 or n>l:
                answ=""
        else:
                g=l-n
                for i in range(n+1):
                        answ=i*string[g:]
        return answ

#test case for repeatEnd:
def testRepeatEnd():
        if repeatEnd("Hello",3)!="llollollo":
                print("Failed test 1")
        if repeatEnd("Hello",1)!="o":
                print("Failed test 2")
        if repeatEnd("ght5sjbt3n4",4)!="t3n4t3n4t3n4t3n4":
                print("Failed test 3")
        if repeatEnd("Hello",0)!="":
                print("Failed test 4")
        if repeatEnd("Hello",-5)!="":
                print("Failed test 5")
        if repeatEnd("Hello",9)!="":
                print("Failed test 6")
        print("Testing complete")
        

#purpose: counts how many tripples there are in the string
#input: a string that is analyzed
#post condition: returns number of tripples in the string
#assumption: no assumptions
def countTripple(string):
    string=str(string)    
    l=len(string)-2
    count=0
    for i in range(l):
        character1=string[i]
        j=i+1
        character2=string[j]
        k=i+2
        character3=string[k]
        if character1==character2 and character2==character3:
            count=count+1
    return count

#test case fot countTripple
def testCountTripple():
        if countTripple("xxxtyrrr")!=2:
                print("Failed test 1")
        if countTripple("xxxtyrrrr")!=3:
                print("Failed test 2")
        if countTripple("xxxxtyrrrr")!=4:
                print("Failed test 3")
        if countTripple("qwertyu")!=0:
                print("Failed test 4")
        if countTripple("x")!=0:
                print("Failed test 5")
        if countTripple("RRRtrGf555gy&&&&")!=4:
                print("Failed test 6")
        if countTripple(234555765444)!=2:
                print("Failed test 7")
        print("Testing complete")

#purpose: output jotto game score (count repeated letters/characters in two strings)
#input: strings S and T
#post condition: returns number of repeated letters/characters in the strings S and T
#assumptions: no assumptions
def jscore(S,T):
        S=str(S)
        T=str(T)
        characters="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+[]'/{}?.,<>`~=-"
        ls=len(characters)
        count=0
        for i in range(ls):
                character=characters[i]
                cS=S.count(character)
                cT=T.count(character)
                if cS<=cT:
                        count=count+cS
                else:
                        count=count+cT
        return count

#test case for jscore
def testjscore():
        if jscore("gattaca","aggtccaggcgc")!=5:
                print("Failed test 1")
        if jscore("gattaca","")!=0:
                print("Failed test 2")
        if jscore(123456,287464)!=3:
                print("Failed test 3")
        if jscore("hello","matrass")!=0:
                print("Failed test 4")
        if jscore("fooooooof","fo")!=2:
                print("Failed test 5")
        if jscore("FoooooooF","fo")!=1:
                print("Failed test 5")
        if jscore("FOOOOF","fo")!=0:
                print("Failed test 5")
        print("Testing complete")
       
                
