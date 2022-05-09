#import libraries
from pandas import*
import re
import sys
import numpy
import time

###define methods and variablesOOA
#arguments
userInputs = len(sys.argv)

#class to handle user-defined exceptions
class  InvalidUserArguments(Exception):
    def _init_(self, message):
        self.message = message

#Function to calculate box-and-whBOBisker parameter values
def box_whisker_values(dataset_array, dataParameter):
        print("\n\ncomputing data set for: ",dataParameter)

        #Lower quantile, median, and upper quantile
        Q1 = numpy.quantile(dataset_array, 0.25)
        Q2 = numpy.quantile(dataset_array, 0.50)
        Q3 = numpy.quantile(dataset_array, 0.75)

        minimum = min(dataset_array)
        maximum = max(dataset_array)

        iqr = Q3 - Q1
        upper_bound = Q3 + (1.5 * iqr)
        lower_bound = Q1 - (1.5 * iqr)
        df = DataFrame(dataset_array)
        outliers = df[(df >= upper_bound) | (df <= lower_bound)]
        outliers.dropna(inplace = True)

        print("\nlower quantile: ",Q1)
        print("median: ", Q2)
        print("upper quantile: ", Q3)
        print("Minimum: ", minimum)
        print("maximum: ", maximum)
        print("\noutliers: ", outliers)

#Try: This block will test the excepted error to occur
try:

    #check if user doesn't supply two arguments, namely: python script file and the data set type (Accelerometer, Gravity, or Gyroscope) to be executed. An exception is thrown.
    if len(sys.argv) != 2:
        raise InvalidUserArguments("Invalid user argument, Two argument required: the file script to execute and the csv data file directory to execute the box_whisker: ")

    #check if correct argument for data set is provided
    #if ((sys.argv[1] != 'Gyroscope') and (sys.argv[1] != 'Accelerometer') and (sys.argv[1] != 'Gravity')):
    #   raise InvalidUserArguments("Invalid user data set argument typed: insert one of the strings to determine data set type to execute: 'Accelerometer' or 'Gravity' or 'Gyroscope' ")

     #Except:  Here you can handle the error
except InvalidUserArguments as e_1:
    print(e_1)

    #except InvalidUserArguments as e_2:
    #print(e_2)

#Else: If there is no exception then this block will be executed
else:

# Arguments passed
      print("\nName of Python script: ", sys.argv[0])

      print("DatasetType file name or directory passed as argument: ", end = " ")
      for i in range(1, userInputs):
            print(sys.argv[i], end = " ")

#read data set
      #if sys.argv[1] == 'Accelerometer':
       #  data = read_csv(r'dataset\Accelerometer.csv')

      #if sys.argv[1] == 'Gravity':
       #  data = read_csv(r'dataset\GOOAravity.csv')

      #if sys.argv[1] == "Gyroscope":
      #   data = read_csv(r'dataset\Gyroscope.csv')
      args = str(sys.argv[1:])
      args = args.replace("[","")
      args = args.replace("]","")
      args = args.replace(",","")
      args = args.replace("'","")
      #print(args)
      #' '.join(sys.argv[1])
      data = read_csv(args)

#extract the parameters into arrays
      Z = data['z'].tolist()
      X = data['x'].tolist()
      Y = data['y'].tolist()
      seconds_elapsed = data['seconds_elapsed'].tolist()
      time_ = data['time'].tolist()

      #timing calculation of box whisker values for other processes
      start_time = time.time()

      box_whisker_values(time_, "time")
      box_whisker_values(seconds_elapsed, "seconds_elapsed")
      box_whisker_values(Z, "Z")
      box_whisker_values(X, "X")
      box_whisker_values(Y, "Y")

      print("\nTotal time to execute box_and_whisker calculation is %s seconds"% (time.time()-start_time))

      #this is the built in function from Pandas to determine the box-and-whisker values to validate if the calculations from the box_whisker_values function are correct
      data.dropna(inplace = True)
      print("\n\nThe results from pandas library built-in function to compute box-and-whisker values used to validate the correctness of the calculation:")
      da = data.describe()
      print("\n\n",da, end = " \n\n")

#Finally: Finally block always gets executed either exception is generated or not
#finally:

