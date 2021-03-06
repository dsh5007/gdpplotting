import pandas
import sys
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt
import glob



# load data and transpose so that country names are
# the columns and their gdp data becomes the rows

def parse_arguments():
  """parses the user command argument and returns the appropriate list of files
  input: 
   nothing
  Returns: 
   filelist = list of files (strings)
  """


  if len(sys.argv) == 1:
   print('NO ARGUMENTS SUPPLIED!!!!')
   print("try using: python gdp_plots.py <filename> or python gdp_plots.py -a")
   print("try using: the -a option looks for all files")
   exit()
 
  if sys.argv[1] == '-a'   :
    filelist = glob.glob("*gdp*.csv")
    if len(filelist) == 0:
      print('No files in diectory')
      print('The filelist is empty - make sure there are files listed')
      print('Filelist print = ',filelist)
      exit()
  else:
    filelist = sys.argv[1:]
 

  return filelist 
# read data into a pandas dataframe and transpose
#no longer need as defined above ## filelist= sys.argv[1:] # "gapminder_gdp_oceania.csv"


def create_plots(filelist):

  """
  Takes in a list of filenames to plot and creates a plot for each file.
    Input:
        filenames: list of strings, list of files to plot
    Returns:
        nothing
  """

  for filename in filelist:
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


def main():
  #parse arguments
  filelist = parse_arguments()

  #generate plots
  create_plots(filelist)

main()
