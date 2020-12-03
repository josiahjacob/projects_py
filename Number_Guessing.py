import math
import random
l=int(input("Enter lower limit: "))
u=int(input("Enter upper limit: "))
g=round(math.log(u - l + 1, 2))
n=random.randint(l,u)
print("You have only",g,"chances to guess")
while g>0:
    gn=int(input("Guess a no: "))
    if gn==n:
        print("Congratulations you did it ! ")
        break
    elif n > gn:
       print("You guessed too small!")
    elif n < gn:
       print("You Guessed too high!")
    g-=1
if g==0:
     print("\nThe number is %d"%n)
     print("\tBetter Luck Next time!")