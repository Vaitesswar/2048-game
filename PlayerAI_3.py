
# coding: utf-8

# In[ ]:



# coding: utf-8

# In[ ]:



# coding: utf-8

# In[ ]:



# coding: utf-8

# In[1]:


from random import randint
from BaseAI_3 import BaseAI
import math
import sys
import random
import numpy as np

class PlayerAI(BaseAI):

    def getMove(self, grid): # grid refers the the current grid state
                 
        alpha = math.inf*-1
        beta = math.inf
        depth = 0
        state = Maximize(grid,alpha,beta,depth)
        
        return state[0]
    
def Maximize(grd,alpha,beta,depth):
    moves = grd.getAvailableMoves() # moves is [Up, down, left, right] given as [0,1,2,3]
    depth += 1
    
    if depth >= 4: # Change this value if program stops prematurely
        return(heuristic(grd))
    
    elif len(moves) == 0:
        return(heuristic(grd))
    
    else:
        Max_state = [None, math.inf*-1]

        for i in range(len(moves)):

            child = grd.clone()
            child.move(moves[i])
            state = Minimize(child,alpha,beta,depth)

            if state[1] > Max_state[1]:
                Max_state[0] = moves[i]
                Max_state[1] = state[1]

            if Max_state[1] >= beta:
                break

            if Max_state[1] > alpha:
                alpha = Max_state[1]

        return(Max_state)

def Minimize(grd,alpha,beta,depth):
    cells = grd.getAvailableCells() # Available positions of cells
    depth += 1
    
    if depth >= 4: # Change this value if program stops prematurely
        return(heuristic(grd))
        
    elif len(cells) == 0:
        return(heuristic(grd)) # Update this based on a proper heuristic
    
    else:
        Min_state = [None, math.inf]
        values = [2,2,2,2,2,2,2,2,4,4] # 80:20 % chance of values 2 and 4

        for i in range(len(cells)):
            
            child = grd.clone()
            child.insertTile(cells[i],random.choice(values))
            state = Maximize(child,alpha,beta,depth)

            if state[1] < Min_state[1]:
                # Min_state[0] = cells[i]
                Min_state[1] = state[1]

            if Min_state[1] <= alpha:
                break

            if Min_state[1] < beta:
                beta = Min_state[1]

        return(Min_state)
    
def heuristic(grd):
    
    array = np.array(grd.map)
    weights = [[10000,500,250,150],[50,80,100,140],[7,6,5,4],[0,1,2,3]]
    weights = np.array(weights)
    total_sum_1 = np.sum(array*weights)
    
    hor_same = array[:,1:4] - array[:,0:3]
    ver_same = array[1:4,:] - array[0:3,:]
    total_sum_2 = np.count_nonzero(hor_same == 0) + np.count_nonzero(ver_same == 0)
    
    total_sum = total_sum_1 + total_sum_2*10
    state = [None,total_sum]
    return(state) # Update this based on a proper heuristic

