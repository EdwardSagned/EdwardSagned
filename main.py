import random
score=0
for i in range(0,5):   
    r1=random.randint(1,9)
    r2=r1
    guess="a"
    while r1==r2:
        r2=random.randint(1,9)
    print(f"The first number is: {r1}")
    while guess!="h"and guess!="l":
        guess=input("Higher or Lower? (h/l)")
    print(f"The second number is {r2}, ",end="")
    if guess == "h" and r1 < r2:
        print("you\'re right!")
        score+=1
    elif guess == "l" and r1 > r2:
        print("you\'re right :D")
        score+=1
    else:
        print("you lost ;-;")
        score=score
    print("_____________________________________")
print("Game ended!")
cpu_score=5-score
print(f"The score is (YOU-CPU): {score}-{cpu_score}")
if score>3:
    print("You won the game!")
else:
    print("You lost the game")