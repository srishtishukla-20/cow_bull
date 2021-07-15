import random
digit=5
name=input("enter name")
print("Hello",name,"Welcome to Cow & Bull Game!","\U0001F920")
print("+++++++++++++++++++++++++++++++++++++++++++++++")
def getSecretNum():
    number=list(range(10))
    random.shuffle(number)
    return number
def getclues():
    numbers=getSecretNum()
    secret_num=[]
    for i in range(digit):
        secret_num.append(numbers[i])
    return secret_num
def check_guess():
    Bull=[]
    Cow=[]
    num=getclues()
    i=0
    print(num)
    maxguess=10
    while maxguess>0:
        guess=int(input("enter your guess:"))
        position=int(input("enter the position of your number"))
        print("+++++++++++++++++++++++++++")
        if guess in num:
            index=1
            while index<guess:
            # index=num.index(guess)
                if index==position:
                    if guess not in Bull:
                        Bull.insert(index,guess)
                        print("BULL",Bull)
                    else:
                        print("You already used this digit,use another digit")
                        
                else:
                    Cow.append(guess)
                    print("COW,The number is in list you can reuse it",Cow)
                index+=1
            if Bull==num:
                print("Congratulations!",name,"You won the game")
                break
            maxguess-=1
            print(maxguess,"turns are left")
        else:
            print("You ran out of tries,Oops! you loose the game")
    return Bull
check_guess()
def play_again():
    while True:
        again=input("If you want to play again press 1 for yes and 2 for no")
        if again=="1":
            check_guess()
        else:
            break
play_again()


    
        
       
    