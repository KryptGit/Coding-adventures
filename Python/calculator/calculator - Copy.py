import math 
value = input("what do you want to do(you can add subtract divide multiply sqaure cuberoot sqaureroot  )" )
if value == "divide":
    a =  int(input("what is a"))
    b =  int(input('what is b'))
    c=a/b
    print(c)
elif value == "add":
    a = int(input("what is a"))
    b = int(input("what is b"))
    c=a+b
    print(c)  
     
elif value == "subtract":
     a =  int(input("what is a"))
     b =  int(input('what is b'))
     c=a-b
     print(c)
     
elif value == "multiply":
     a =  int(input("what is a"))
     b =  int(input('what is b'))
     c=a*b 
     print(c)

elif value == "sqaure":
     a =  int(input("what is a"))
     b =  int(input('what is b'))
     c = a**b
     print(c)

elif value == "cuberoot":
     a = int(input("what is a"))
     b=a**(1./3.)
     print(b)

elif value == "sqaureroot":
     a = int(input("what is a"))
     b=a**(1./2.)
     print(b)


 



