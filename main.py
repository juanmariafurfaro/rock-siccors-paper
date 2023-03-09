def menu():
    print("1-Rock")
    print("2-Paper")
    print("3-Siccors")
def validacion():
    while True:
        try:
            answer=int(input("Pick a number: "))
        except ValueError:
            print("Write a answer.")
            continue
        if(answer != 1 and answer != 2 and answer != 3):
            print("ANSWER INVALID")
        else:
            break
    return answer
def value(Ai):
    if (Ai == 1):
        IAs = 'Rock'
        print("Rock")
    elif (Ai == 2):
        IAs = 'Paper'
        print("Paper")
    else:
        IAs = 'Siccors'
        print("Siccors")
    return IAs
def valid():
    while True:
        try:
            playing=input("Do you wanna play? ")
        except ValueError:
            print("Write a yes or no.")
            continue
        if(playing != 'Yes' and playing != 'yes' and playing != 'no' and playing != 'No'):
            print("ANSWER INVALID")
        else:
            break
    return playing
#main

import random

print("Welcome player 1")
contw=0
contl=0
contg=0
play=valid()
while play!='No' and play !='NO' and play !='no':
    menu()
    resp=validacion()
    rspc=value(resp)
    IA=random.randrange(1,4)
    IAs=value(IA)
    if(resp==IA):
        print("It's a tie")
    elif(resp==1 and IA==3):
        print("Player 1 win")
        contw+=1
    elif(resp==2 and IA==1):
        print("Player 1 win")
        contw+=1
    elif(resp==3 and IA==2):
        print("Player 1 win")
        contw+=1
    else:
        print("You loose")
        contl+=1
    contg+=1
    play=valid()

print("END")
print("Yo play ",contg,"games win:",contw," loose:",contl," and tie",contg-(contw+contl))