import pandas
import sys
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

# load data and transpose so that country names are
# the columns and their gdp data becomes the rows

# read data into a pandas dataframe and transpose
filename= sys.argv[1] # "gapminder_gdp_oceania.csv"
data = pandas.read_csv(filename, index_col = 'country').T

# create a plot the transposed data
ax = data.plot(title=filename)

#Add axes
ax.set_xlabel("year")
ax.set_ylabel("GDP per capita")

#axes tick properties
ax.set_xticks(range((len(data.index))))
ax.set_xticklabels(data.index, rotation=45)

# display the plot
plt.show()
