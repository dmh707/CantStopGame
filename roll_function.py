#proof of concept for the roll() function
import random
print("enter 'roll()' to roll four dice")
def roll():
    dice = random.sample(range(6),4)
    
    options = setOptions(dice)
    
    print("you have rolled: " )
    print(dice)
    
    print("Your options are")
    i=0
    for opt in options:
        print("Option %r is %r" % (i,opt))
        i=i+1
    checker=''
    while checker!='Y':
        optSelection = options[int(input("Which option number would you like? (only include the number,please) "))]
        checker=input("You have selected %r. Is this correct? (Y or N) " % (optSelection))
    
    
def setOptions(dice):
    a=dice[0]
    b=dice[1]
    c=dice[2]
    d=dice[3]
    
    ab=a+b
    ac=a+c
    ad=a+d
    
    cd=c+d
    bd=b+d
    bc=b+c
    
    opt1=[ab,cd]
    opt2=[ac,bd]
    opt3=[ad,bc]
    options=[opt1,opt2,opt3]
    return options
