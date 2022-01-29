#This chapter will allow you to apply all the concepts you've learned in this course. You will use hacker statistics to calculate your chances of winning a bet. 
#Use random number generators, loops, and Matplotlib to gain a competitive edge!
import numpy as np
#set the seed for the random number
np.rand.seed(123)
print(np.random.rand())

# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <=5 :
    step = step + 1 
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)
#______________________________________________BUILDING THE LOOP FOR 100 ITERATIONS________
# NumPy is imported, seed is set
# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step-1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt 

#______________PLOT THE RANDON WALK_____________________#

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()
