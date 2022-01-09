#----------------Build a histogram (2): Build histogram with 5 bins, life_exp is a list
import matplotlib.pyplot as plt
plt.hist(life_exp, bins = 5)
# Show and clean up plot
plt.show()
plt.clf() #plt.clf() cleans it up again so you can start afresh.

# Build histogram with 20 bins
plt.hist(life_exp, bins = 20)

# Show and clean up again
plt.show()
plt.clf()

#----------------Build a histogram (3): compare
# Histogram of life_exp, 15 bins   TIP!!! If you wanna to have both graphics at the same time, don't run plt.clf()
plt.hist(life_exp, bins = 15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins

plt.hist(life_exp1950, bins = 15)
# Show and clear plot again
plt.show()
plt.clf()
