
# coding: utf-8

# In[7]:

import numpy as np

# setting the doors as 0,1,2
doors=np.array([0,1,2])

# simulating the selection the prize door
def simulate_prizedoor(nsim):
    answer=np.random.choice(doors,nsim)
    return answer

# simulating the user guess
def simulate_guess(nsim):
    answer=np.random.choice(doors,nsim)
    return answer

# simulating the goat door to be revealed once the prize is fixed and the user has made a guess
def goat_door(prizedoors,guesses):
    goat_door=[]
    for x in range(0,prizedoors.size):
        doors_na=np.array([prizedoors[x],guesses[x]])
        options=list(set(doors)^set(doors_na))
        goat_door.append(np.random.choice(options))
    goat_door=np.array(goat_door)
    return goat_door
    
# switches the guess     
def switch_guess(guesses,goatdoors):
    return goat_door(guesses,goatdoors)

# calculating win percentage
def win_percentage(guesses,prizedoors):
    win_per=sum(guesses==prizedoors)/prizedoors.size
    return win_per
    

# simulating the game 10,000 times
games =10000
prizedoors=simulate_prizedoor(games)
guesses=simulate_guess(games)
goatdoors=goat_door(prizedoors,guesses) 
switch=switch_guess(guesses,goatdoors)

# the win percentage for the case in which the switch is made is ~66% compared to ~33% in which the user sticks with the original choice. This is a direct application of Bayes theorem in which the prior probability is updated when the door different from the door which the user guessed and the one that has the prize is opened

print (win_percentage(guesses,prizedoors))
print (win_percentage(switch,prizedoors))

