import random #random
import time #use for time.sleep()
from termcolor import colored # color text
from zalgo_text import zalgo # glitch text :))
lines = open('/Users/luka/OneDrive - ОАНО Школа ЛЕТОВО/Programming/Python/MyProjects/BullsAndCows/boy_users.txt').read().splitlines() #random nicknames

def DurakCheckFunction(guess): #check for invalid numbers
    DurakCheck=0
    key=[1,2,3,4,5,6,7,8,9,0]
    if len(guess)!=4:
        DurakCheck=1
    elif guess[0] not in key: #check for digits
        DurakCheck=2
    elif guess[1] not in key:
        DurakCheck=2
    elif guess[2] not in key:
        DurakCheck=2
    elif guess[3] not in key:
        DurakCheck=2
    else:
        q=guess.count(1) #check for wtimes or more digits
        w=guess.count(2)
        e=guess.count(3)
        r=guess.count(4)
        t=guess.count(5)
        y=guess.count(6)
        u=guess.count(7)
        i=guess.count(8)
        o=guess.count(9)
        p=guess.count(0)
        if q>1 or w>1 or e>1 or r>1 or t>1 or y>1 or u>1 or i>1 or o>1 or p>1:
            DurakCheck=3
    return(DurakCheck)
def GameOnlineOpponent(): #play with opponent (opponent (bot :)) make guess)
    number = random.sample(range(10), 4)
    #printAt(f'Solution: {*number,}'), for develop
    time.sleep(2)
    printAt('The opponent has thought of a number!')
    printAt("---------------------------------------------------- \n")
    tryes=0
    while True:
        tryes+=1
        printAt(f'Try number {tryes}')
        printAt("Try to guess his number:")
        try:
            guess = [int(i) for i in input()]
            if DurakCheckFunction(guess) == 0:
                if guess == number: #win check
                    printAt("You won!")
                    printAt(f"It took {tryes} guess(es).")
                    printAt("---------------------------------------------------- \n")
                    return(tryes)
                else: #how many bulls and cows
                    cow=0
                    bull=0
                    for i in range(4):
                        if guess[i]==number[i]:
                            bull += 1
                        elif guess[i] in number: 
                            cow += 1
                printAt(f"Bulls: {bull}. Cows: {cow}")
                printAt("---------------------------------------------------- \n")
            elif DurakCheckFunction(guess) == 1: #errors 
                printAt('The guess must be 4-digit')
                printAt("---------------------------------------------------- \n")
            elif DurakCheckFunction(guess) == 2:
                printAt('The guess must be only digits')
                printAt("---------------------------------------------------- \n")
            elif DurakCheckFunction(guess) == 3:
                printAt('The guess must be composed of different digits')
                printAt("---------------------------------------------------- \n")
        except:
            printAt('The guess must be only digits')
            printAt("---------------------------------------------------- \n")
def GameOnlineYou(): #play with opponent (you make guess)
    printAt('Ok, make a guess')
    while True:
        number=[int(i) for i in input()]
        if DurakCheckFunction(number) == 1: #errors
            printAt('The guess must be 4-digit')
            printAt("---------------------------------------------------- \n")
            printAt('Guess the number one more time')
        elif DurakCheckFunction(number) == 2:
            printAt('The guess must be only digits')
            printAt("---------------------------------------------------- \n")
            printAt('Guess the number one more time')
        elif DurakCheckFunction(number) == 3:
            printAt('The guess must be composed of different digits')
            printAt("---------------------------------------------------- \n")
            printAt('Guess the number one more time')
        else:
            break
    printAt("---------------------------------------------------- \n")
    number = random.sample(range(10), 4)
    printAt('The opponent starts to guess the number!')
    tryes=0
    for i in range (random.randint(7,30)):
        tryes+=1
        printAt(f"Try number {tryes}")
        printAt("The enemy is trying to guess the number ...")
        time.sleep(random.randint(1,3)) #random output to simulate online
        guess = random.sample(range(10), 4)
        ''.join(map(str, guess))
        printAt(f'{*guess,}')
        cow=0
        bull=0
        for i in range(4):
            if guess[i]==number[i]:
                bull += 1
            elif guess[i] in number:
                cow += 1
        printAt(f"Bulls: {bull}. Cows: {cow}")
        printAt("---------------------------------------------------- \n")
    tryes+=1
    time.sleep(random.randint(1,3)) #right number from computer
    printAt(f"Try number {tryes}")
    printAt("The enemy is trying to guess the number ...")
    printAt(f'{*number,}')
    printAt("The enemy has guessed right!")
    printAt(f"It took him {tryes} guess(es).")
    printAt("---------------------------------------------------- \n")
    return(tryes)
def GameOffline(): #play offline (bot make guess)
    printAt('Ok, let me play with you, now I will guess the number...')
    time.sleep(3)
    printAt("---------------------------------------------------- \n")
    number = random.sample(range(10), 4)
    printAt('I made a guess!')
    #printAt(f'Solution: {*number,}'), for develop
    tryes=0
    while True:
        tryes+=1
        printAt(f"Try number {tryes}")
        printAt("Try to guess my number:")
        try:
            guess = [int(i) for i in input()]
            if DurakCheckFunction(guess) == 0:
                if guess == number:
                    printAt("You won!") #win check
                    printAt(f"It took {tryes} guess(es).")
                    printAt("---------------------------------------------------- \n")
                    return(tryes)
                else: #how many bulls and cows
                    cow=0
                    bull=0
                    for i in range(4):
                        if guess[i]==number[i]:
                            bull += 1
                        elif guess[i] in number: 
                            cow += 1
                printAt(f"Bulls: {bull}. Cows: {cow}")
                printAt("---------------------------------------------------- \n")
            elif DurakCheckFunction(guess) == 1: #errors
                printAt('The guess must be 4-digit')
                printAt("---------------------------------------------------- \n")
            elif DurakCheckFunction(guess) == 2:
                printAt('The guess must be only digits')
                printAt("---------------------------------------------------- \n")
            elif DurakCheckFunction(guess) == 3:
                printAt('The guess must be composed of different digits')
                printAt("---------------------------------------------------- \n")
        except:
            printAt('The guess must be only digits')
            printAt("---------------------------------------------------- \n")

def printAt(text): #All text color func
    if SecretUnlock == 1: #secret check
        print(colored(zalgo.zalgo().zalgofy(text),ClAt))
    else:
        print(colored(text, ClAt))
def printNm(text): #Nickname color func
    print(colored(text, ClNm))
def printRm(text): #Random colors for opponents nicknames
    colors = ['blue', 'yellow', 'red', 'green', 'cyan']
    random.shuffle(colors)
    print(colored(text, colors[0]))

InvalidCheck=0 #sistem variables
logCheck=0
points=0
wins=0
loses=0
SecretUnlock=0
ClNm='white' #colors
ClAt='white'

#start:
printAt('\n\nHello! I am a bull and cow bot. Register so that other users can see you. So far, registration is one-time. If you lok at the code, then on top there will be a Part of the code for normal registration, but it does not work; (') #start message
while InvalidCheck!=1: #login
    printAt('Write your login:')
    logintry=input()
    printAt('Your password:')
    passwordtry=input()
    printAt('And your nickname:')
    nicknametry=input()
    printAt('Super! You just created an account!')
    printAt("---------------------------------------------------- \n")
    InvalidCheck=1

printAt('I\'m a cow and bull bot! I have a lot of functionality. If you suddenly do not know the rules write \'rules \', and if you are already trained and ready to fight write \'play\'. If you want to see your statistics write \'account\'. If you want to get to the store write \'shop\'.') #start message 2
while True: #main code
    request=input()
    if request=='rules': #rules, I think there is no need to explain anything here
        printAt('Great, now I\'m going to tell you the rules of this wonderful game!')
        time.sleep(1)
        printAt('Each player writes a secret 4-digit number. All numbers must be different. Then, in turn, the player tries to guess the opponent\'s number, which calls the number of matches. If the coinciding numbers are in their correct positions, they are bulls, if in different positions they are cows.')
        time.sleep(2)
        printAt('I told you all the rules.')
        printAt("---------------------------------------------------- \n")
        printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
    elif request=='play': #main game
        printAt('Do you want to play \'offline\' or \'online\'?')
        while True:
            requestgame=input()
            if requestgame=='offline': #offline game
                GameOffline()
                printAt('Game over!')
                break
            elif requestgame=='online':
                printAt('Ok, I\'m loking for a rival') #Simulation of online (loading, estimated waiting time, etc.)
                WaitingTime=random.randint(5,10)
                printAt(f'Approximate waiting time {WaitingTime} seconds.')
                for i in range (WaitingTime):
                    printAt(f'{WaitingTime-i} seconds left')
                    time.sleep(1)
                printAt("---------------------------------------------------- \n")
                printAt('I found a player!')
                time.sleep(1)
                printRm(f'{random.choice(lines)}')
                time.sleep(1)
                printAt('VS')
                time.sleep(1)
                printNm(f'{nicknametry}')
                time.sleep(1)
                printAt('And the first number thinks ...')
                time.sleep(2)
                FirstNumber=random.randint(0,1)
                if FirstNumber==1:
                    printAt('You!') 
                    Optryes=GameOnlineYou()
                    printAt('Round 1 is over!')
                    printAt('Timeout!')
                    for i in range(10):
                        printAt(f'{10-i} seconds left')
                        time.sleep(1)
                    printAt('The second round begins now!')
                    Youtryes=GameOnlineOpponent()
                    time.sleep(4)
                    printAt('Game over!')
                    points+=(Optryes-Youtryes)*500
                    if Optryes>Youtryes: #wins and loses
                        wins+=1
                        printAt('You win!')
                    elif Youtryes<Optryes:
                        loses+=1
                        printAt('You lose!')
                    printAt(f'You have earned {(Optryes-Youtryes)*500} points!') #points system
                    time.sleep(3)
                    break
                else:
                    printAt('Your opponent!')
                    Youtryes=GameOnlineOpponent()
                    printAt('Round 1 is over!')
                    printAt('Timeout!')
                    for i in range(10):
                        printAt(f'{10-i} seconds left')
                        time.sleep(1)
                    printAt('The second round begins now!')
                    Optryes=GameOnlineYou()
                    time.sleep(4)
                    printAt('Game over!')
                    points+=(Optryes-Youtryes)*500
                    if Optryes>Youtryes: #wins and loses
                        wins+=1
                        printAt('You win!')
                    elif Youtryes<Optryes:
                        loses+=1
                        printAt('You lose!')
                    printAt(f'You have earned {(Optryes-Youtryes)*500} points!') #points system
                    time.sleep(3)
                    break
            else:
                printAt('I don\'t understand you... Please write \'offline\' or \'online\'')
        printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
    elif request=='account': #statistics
        printAt(f'Login: {logintry}')
        printNm(f'Nickname: {nicknametry}')
        printAt(f'Points: {points}')
        printAt(f'Wins: {wins}')
        printAt(f'loses: {loses}')
        printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
    elif request=='shop': #shop
        printAt('Welcome to shop!')
        time.sleep(1)
        printAt('Here are our products:')
        printAt('1) Color nickname (500-20000 points)') #color text is my idea! Mark Gol. copy it ;(
        printAt('2) Color all text (1000-40000 points)')
        if SecretUnlock==0:
            printAt('3) Secret :) (80000 points)')
        elif SecretUnlock==1:
            printAt('3) Disable secret :) (20000 points)')
        printAt('Write the product number you want to buy (write 0 if you want to exit):')
        SomBuy=0
        while SomBuy==0:
            request=input()
            if request=='1': #nickname color
                printAt('Choose color:')
                print(colored('1) BLUE, 500', 'blue'))
                print(colored('2) CYAN, 1000', 'cyan'))
                print(colored('3) GREEN, 2000', 'green'))
                print(colored('4) MAGENTA, 5000', 'magenta'))
                print(colored('5) RED, 10000', 'red'))
                print(colored('6) YELLOW, 20000', 'yellow'))
                print('Write the product number you want to buy (write 0 if you want to exit):')
                while True:
                    request=input()
                    if request=='0':
                        printAt('Bye!')
                        time.sleep(0.5)
                        SomBuy=1
                        printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
                        break
                    if request=='1' and points>=500:
                        printAt('Sales!')
                        printAt('Thank you for your purchase!')
                        ClNm='blue'
                        points-=500
                        SomBuy=1
                        time.sleep(0.5)
                        printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
                        break
                    elif request=='2' and points>=1000:
                        printAt('Sales!')
                        printAt('Thank you for your purchase!')
                        ClNm='cyan'
                        points-=1000
                        SomBuy=1
                        time.sleep(0.5)
                        printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
                        break
                    elif request=='3' and points>=2000:
                        printAt('Sales!')
                        printAt('Thank you for your purchase!')
                        ClNm='green'
                        points-=2000
                        SomBuy=1
                        time.sleep(0.5)
                        printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
                        break
                    elif request=='4' and points>=5000:
                        printAt('Sales!')
                        printAt('Thank you for your purchase!')
                        ClNm='magenta'
                        points-=5000
                        SomBuy=1
                        time.sleep(0.5)
                        printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
                        break
                    elif request=='5' and points>=10000:
                        printAt('Sales!')
                        printAt('Thank you for your purchase!')
                        ClNm='red'
                        points-=10000
                        SomBuy=1
                        time.sleep(0.5)
                        printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
                        break
                    elif request=='6' and points>=20000:
                        printAt('Sales!')
                        printAt('Thank you for your purchase!')
                        ClNm='yellow'
                        points-=20000
                        SomBuy=1
                        time.sleep(0.5)
                        printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
                        break
                    else:
                        printAt('Either there is not enough money, or an invalid number! Try again (0 to exit):')
            elif request=='2': #all text color
                printAt('Choose color:')
                print(colored('1) BLUE, 1000', 'blue'))
                print(colored('2) CYAN, 2000', 'cyan'))
                print(colored('3) GREEN, 4000', 'green'))
                print(colored('4) MAGENTA, 10000', 'magenta'))
                print(colored('5) RED, 20000', 'red'))
                print(colored('6) YELLOW, 40000', 'yellow'))
                print('Write the product number you want to buy (write 0 if you want to exit):')
                while True:
                    request=input()
                    if request=='0':
                        printAt('Bye!')
                        time.sleep(0.5)
                        SomBuy=1
                        printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
                        break
                    if request=='1' and points>=1000:
                        printAt('Sales!')
                        printAt('Thank you for your purchase!')
                        ClAt='blue'
                        points-=1000
                        SomBuy=1
                        time.sleep(0.5)
                        printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
                        break
                    elif request=='2' and points>=2000:
                        printAt('Sales!')
                        printAt('Thank you for your purchase!')
                        ClAt='cyan'
                        points-=2000
                        SomBuy=1
                        time.sleep(0.5)
                        printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
                        break
                    elif request=='3' and points>=4000:
                        printAt('Sales!')
                        printAt('Thank you for your purchase!')
                        ClAt='green'
                        points-=4000
                        SomBuy=1
                        time.sleep(0.5)
                        printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
                        break
                    elif request=='4' and points>=10000:
                        printAt('Sales!')
                        printAt('Thank you for your purchase!')
                        ClAt='magenta'
                        points-=10000
                        SomBuy=1
                        time.sleep(0.5)
                        printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
                        break
                    elif request=='5' and points>=20000:
                        printAt('Sales!')
                        printAt('Thank you for your purchase!')
                        ClAt='red'
                        points-=20000
                        SomBuy=1
                        time.sleep(0.5)
                        printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
                        break
                    elif request=='6' and points>=40000:
                        printAt('Sales!')
                        printAt('Thank you for your purchase!')
                        ClAt='yellow'
                        points-=40000
                        SomBuy=1
                        time.sleep(0.5)
                        printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
                        break
                    else:
                        printAt('Either there is not enough money, or an invalid number! Try again (0 to exit):')
            elif request=='3' and points>=80000 and SecretUnlock==0: #secret XD
                printAt('Are you sure? [yes/no]')
                request=input()
                if request=='yes':
                    printAt('Really? [yes/no]')
                    request=input()
                    if request=='yes':
                        printAt('In fact, I myself do not know what is there... But is it your decision to continue? [yes/no]')
                        request=input()
                        if request=='yes':
                            printAt('OK good luck...')
                            time.sleep(1)
                            points-=80000
                            SecretUnlock=1 #Secret started its work
                            SomBuy=1
                            printAt('Sales!')
                            printAt('Thank you for your purchase!')
                            time.sleep(0.5)
                            printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
                elif SecretUnlock==0:
                    printAt('Okay, maybe this is the right choice, maybe not ...')
                    time.sleep(1)
                    printAt('Bye!')
                    SomBuy=1
            elif request=='3' and points>=20000 and SecretUnlock==1: #turn off secret ;(
                printAt('You do not like :(? Disable? [yes/no]')
                request=input()
                if request=='yes':
                    printAt('Ok :(')
                    points-=20000
                    SecretUnlock=0
                    SomBuy=1
                    time.sleep(0.5)
                    printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
            elif request=='0':
                printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
                break
            else:
                printAt('I do not understand you (or you have no money)... Write the item number:')
    elif request=='hack': #hack :)))
        wins=10000
        points=100000000000
        printAt('OMG HACKER!!!')
        printAt('I remind you that now you can write \'rules\', \'account\', \'shop\' or \'play\'')
    else:
        printAt('I don\'t understand you... Please write \'rules\', \'account\', \'shop\' or \'play\'') 