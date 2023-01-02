a1 = "a1"
a2 = "a2"
a3 = "a3"
b1 = "b1"
b2 = "b2"
b3 = "b3"
c1 = "c1"
c2 = "c2"
c3 = "c3"
moves = [a1,a2,a3,b1,b2,b3,c1,c2,c3]


loop = True
loop2 = False

def display():
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
    print(a1,"|",a2,"|",a3)
    print("------------")
    print(b1,"|",b2,"|",b3)
    print("------------")
    print(c1,"|",c2,"|",c3)

def edit(pos, player):
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
    if pos == "a1":
        a1 = player
    elif pos == "a2":
        a2 = player
    elif pos == "a3":
        a3 = player
    elif pos == "b1":
        b1 = player
    elif pos == "b2":
        b2 = player
    elif pos == "b3":
        b3 = player
    elif pos == "c1":
        c1 = player
    elif pos == "c2":
        c2 = player
    elif pos == "c3":
        c3 = player
def remove(pos):
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
    if pos == "a1":
        a1 = ""
    elif pos == "a2":
        a2 = ""
    elif pos == "a3":
        a3 = ""
    elif pos == "b1":
        b1 = ""
    elif pos == "b2":
        b2 = ""
    elif pos == "b3":
        b3 = ""
    elif pos == "c1":
        c1 = ""
    elif pos == "c2":
        c2 = ""
    elif pos == "c3":
        c3 = ""
def play(pos,moves,player):
    if pos in moves:
        edit(pos,player)
        return 1
    else:
        print("please pick a valid move")
        return 0
        


        


def check_win(name):
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
    global loop
    global turn
    if a1 == a2 and a2 == a3:
        display()
        print(name + " is the winner!!")
        loop = False
    elif b1 == b2 and b2 == b3:
        display()
        print(name + " is the winner!!")
        loop = False
    elif c1 == c2 and c2 == c3:
        display()
        print(name + " is the winner!!")
        loop = False
    elif a1 == b1 and b1 == c1:
        display()
        print(name + " is the winner!!")
        loop = False
    elif a2 == b2 and b2 == c2:
        display()
        print(name + " is the winner!!")
        loop = False
    elif a3 == b3 and b3 == c3:
        display()
        print(name + " is the winner!!")
        loop = False
    elif a1 == b2 and b2 == c3:
        display()
        print(name + " is the winner!!")
        loop = False
    elif c1 == b2 and b2 == a3:
        display()
        print(name + " is the winner!!")
        loop = False    
    elif turn == 9:
        display()
        print("THE GAME IS A DRAW")
        loop = False
    else:
        return


#setup

class Player:
    def __init__(self, name, symbol, id):
        self.name = name
        self.symbol = symbol
        self.id = id

p1 = Player(input("what is your name player 1 "), input("what is your symbol player 1 "), 'p1')
p2 = Player(input("what is your name player 2 "), input("what is your symbol player 2 "), "p2")
cp = Player(p2.name, p2.symbol, p2.id)
print("player one you are " + p1.symbol)
print("player two you are " + p2.symbol)
switch = True
turn = 0
#loop
while loop == True:
    if switch == True:
        if cp.id == p2.id:
            cp = Player(p1.name, p1.symbol, p1.id)
        elif cp.id == p1.id:
            cp = Player(p2.name, p2.symbol, p2.id)
    if switch == False:
        switch = True


    display()
    pos = input('what is your move ' + cp.name + " ")
    n = play(pos,moves,cp.symbol)
    if n == 1:
        pass
    if n == 0:
        switch = False
        continue
    turn += 1
    check_win(cp.name)  

