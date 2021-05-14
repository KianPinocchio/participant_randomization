

## Author: KianPinocchio
## Date: May, 2021

## *************************************************************************
## *************************************************************************

## ******** Code to generate randomcodes for Participant allocation ********
## ******** For the following Experimental Project *************************
## **** https://osf.io/bsvy2/?view_only=f03a795e0d25453591c710159edc6489****

## *************************************************************************
## *************************************************************************


## call the modules

import random
import pandas as pd

### There are four conditions
### with four different types of Stimuli: Fear, Shame, Prosocial inducing and Neutral '''

conditions = ['F','S','N','P']

## Condition for the loop

loop_cond = True

loop_count = 0

## Lists to append all the generated codes for each condition

F_lst = []
S_lst = []
N_lst = []
P_lst = []


## Loop to generate random participant codes

while loop_cond == True:


    loop_count = loop_count + 1    

    ## Randomly chooses a condition from the conditions list
    
    results = random.choices(conditions, k = 1)

    ## Assigns the randomly selected condition code with the current loop_count
    
    rand_code = results[0] + str(loop_count)

    ## Checks if there are enough randomly generated codes for each condition
    
    if len(F_lst) == 500 and len(S_lst) == 500 and len(N_lst)== 500 and len(P_lst) == 500:
        print('worked')
        loop_cond = False
        break


    ## Assigns generated codes to appropriate condition
    
    elif results[0] == 'F' and len(F_lst) < 500:
        F_lst.append(rand_code)
    elif results[0] == 'S'and len(S_lst) < 500:
        S_lst.append(rand_code)
    elif results[0] == 'N'and len(N_lst) < 500:
        N_lst.append(rand_code)
    elif results[0] == 'P'and len(P_lst) < 500:
        P_lst.append(rand_code)



## Creates a DataFrame for all the codes to be assigned to

df = pd.DataFrame (F_lst, index = None, columns = ['Fear'])

df['Shame'] = S_lst
df['Neutral'] = N_lst
df['Prosocial'] = P_lst

## Save the codes to a .CSV file
df.to_csv('randomcodes.csv')

print('ALL done')
