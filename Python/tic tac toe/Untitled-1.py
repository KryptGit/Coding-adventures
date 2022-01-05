diction = {1:"1"}
def generateboard(w,h):
    global diction
    for i in h:
        for j in w:
            diction.update({str(j): j})
    
    print(diction)