import random 
a = ["1","2","3","4","5","6","7",]
b = ["1","2","3","4","5","6","7",]
c = ["1","2","3","4","5","6","7",]
d = ["1","2","3","4","5","6","7",]
e = ["1","2","3","4","5","6","7",]
f = ["1","2","3","4","5","6","7",]
g = ["1","2","3","4","5","6","7",]
dataset = ["a","b","c","d","e","f'","g"]
n = 0
while n < 7:
    output = random.choice(dataset)
    if output == "a":
        strioutput = a
        ans = "1"
    elif output == "b":
        strioutput = b
        ans = "2"
    elif output == "c":
        strioutput = c
        ans = "3"
    elif output == "d":
        strioutput = d
        ans = "4"
    elif output == "e":
        strioutput = e
        ans = "5"
    elif output == "f":
        strioutput = f
        ans = "6"
    elif output == "g":
        strioutput = g
        ans = "7"

    numoutput = random.choice(strioutput)
    if numoutput == ans:
        print(n)
        n+1

        
    elif not numoutput == ans:
        strioutput.remove(numoutput)
        print("0")
        n = 0

while n == 7:
    test = input('what letter do you want to test')
    answer = random.choice(test)
    print(answer)
    loop = input('do you want to go on')
    if loop == "yes":
        n = 7
    elif loop == "no":
        n = 8


    



    
        
    

