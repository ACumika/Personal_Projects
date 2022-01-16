def encrypt(plain, key):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    cipher=""
    #key="badcfehgjilknmporqtsvuxwzy"
    l=len(plain)
    for i in plain:
        print (i)
        if i==" ":
            cipher=cipher+" "
        else:
            pos=alphabet.index(i)
            cipher=cipher+key[pos]
    return cipher

def encrypt1(msg, key):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    cipher=""
    #key="badcfehgjilknmporqtsvuxwzy"
    l=len(plain)
    for i in plain:
        print (i)
        if i==" ":
            cipher=cipher+" "
        else:
            pos=alphabet.index(i)
            cipher=cipher+key[pos]
    return cipher
        
        
