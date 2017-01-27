
# coding: utf-8

# In[7]:

import numpy as np

doors=np.array([0,1,2])

def simulate_prizedoor(nsim):
    answer=np.random.choice(doors,nsim)
    return answer

def simulate_guess(nsim):
    answer=np.random.choice(doors,nsim)
    return answer

def goat_door(prizedoors,guesses):
    goat_door=[]
    for x in range(0,prizedoors.size):
        doors_na=np.array([prizedoors[x],guesses[x]])
        options=list(set(doors)^set(doors_na))
        goat_door.append(np.random.choice(options))
    goat_door=np.array(goat_door)
    return goat_door
    
def switch_guess(guesses,goatdoors):
    return goat_door(guesses,goatdoors)

def win_percentage(guesses,prizedoors):
    win_per=sum(guesses==prizedoors)/prizedoors.size
    return win_per
    
games =10000

prizedoors=simulate_prizedoor(games)
guesses=simulate_guess(games)
goatdoors=goat_door(prizedoors,guesses) 
switch=switch_guess(guesses,goatdoors)

#hello

print (win_percentage(guesses,prizedoors))
print (win_percentage(switch,prizedoors))

