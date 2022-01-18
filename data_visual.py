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
# Histogram of life_exp, 15 bins   TIP!!! If you wanna have both graphics at the same time, don't run plt.clf()
plt.hist(life_exp, bins = 15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins

plt.hist(life_exp1950, bins = 15)
# Show and clear plot again
plt.show()
plt.clf()

##### CREATE A PROFOUND SCATTERPLOT OF LIFE EXPECTATION VS GDP PER CAPITA
# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()
