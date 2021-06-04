import random
from matplotlib import pyplot as plt
import numpy as np


print("r=Rock,p=Paper,s=Scissors")


options=["Rock","Paper","Scissors"]
choices=["r","p","s"]
Rock_Wins=[]
Paper_Wins=[]
Scissors_Wins=[]
Tie=[]

for i in range(100):
    if random.choice(options) == "Rock" and random.choice(choices)=="s":
        print("Rock WINS")
        Rock_Wins.append(1)
    elif random.choice(options) == "Paper" and random.choice(choices)=="s":
        print("Scissors WIns")
        Scissors_Wins.append(1)
    elif random.choice(options) == "Scissors" and random.choice(choices)=="r":
        print("rock wins")
        Rock_Wins.append(1)
    elif random.choice(options) == "Paper" and random.choice(choices)=="r":
        print("Paper WINS")
        Paper_Wins.append(1)
    elif random.choice(options) == "Rock" and random.choice(choices)=="p":
        print ("Paper WINS")
        Paper_Wins.append(1)
    elif random.choice(options) == "Scissors" and random.choice(choices)=="p":
        print("Scissors WINs")
        Scissors_Wins.append(1)
    else:
        print("TIE")
        Tie.append(1)




rocksum= sum(Rock_Wins)
print(rocksum)
papersum= sum(Paper_Wins)
print(papersum)
scissorsum=sum(Scissors_Wins)
print(scissorsum)
sumtie=sum(Tie)
print(sumtie)

results=["Rock WINs","Paper WINS","Scissors Wins","Ties"]
#xaxis=[1,2,3,4]
totalsum=[rocksum,papersum,scissorsum,sumtie]
print (totalsum)
 
plt.bar(results,totalsum,color=['red', 'blue', 'purple', 'green'])
plt.ylabel("Amount of wins for each option in rock paper scissors over 100 times")
plt.show()

