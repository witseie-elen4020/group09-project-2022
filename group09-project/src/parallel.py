#import libraries
from pandas import*
from mpi4py import MPI
import re
import sys
import numpy
import time
from numpy.lib.utils import source

###define methods and variablesOOA
#arguments
userInputs = len(sys.argv)

class  InvalidUserArguments(Exception):
    def _init_(self, message):
        self.message = message

#initialize the communication world
comm = MPI.COMM_WORLD

#get this particular processes' 'rank' ID
rank = comm.Get_rank()

#get the size of the communication world
num_processes = comm.Get_size()
processor_name = MPI.Get_processor_name()

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

#function to read data
def read_data_set():
      args = str(sys.argv[1])
      args = args.replace("[","")
      args = args.replace("]","")
      args = args.replace(",","")
      args = args.replace("'","")

      #read data in chunks of 1 million rows at a time
      chunk = read_csv(args, chunksize=1000000)
      ReadData = concat(chunk)
      return ReadData

#Try: This block will test the excepted error to occur
try:

    #check if user doesn't supply two arguments, namely: python script file and the data set type (Accelerometer, Gravity, or Gyroscope) to be executed. An exception is thrown.
    if ((len(sys.argv) != 2) and (len(sys.argv) != 4)):
        raise InvalidUserArguments("Invalid user argument, Two or Four arguments required: \n\n For Two arguments: the time range is automatically set to {min - max), hence, insert file script to execute and the csv file directory path \n\n  For Four arguments: insert the file script to execute and the csv data file directory path")

#Except:  Here you can handle the error
except InvalidUserArguments as e_1:
    if rank == 0:
       print(e_1)

#Else: If there is no exception then this block will be executed
else:
    # Arguments passed
    print("\nName of Python script: ", sys.argv[0])

    #if two arguments passed, withou time range specified. automatic time range is from the minimum to maximum time
    if len(sys.argv) == 2:
        print("DatasetType file name or directory passed as argument: ", end = " ")
        for i in range(1, userInputs):
            print(sys.argv[i], end = " ")

        print("\n\nreading data ", end = " ")
        data = read_data_set()

        if rank == 0:
            #extract the parameters into arrays
            Z = data['z'].tolist()
            X = data['x'].tolist()
            Y = data['y'].tolist()
            seconds_elapsed = data['seconds_elapsed'].tolist()
            time_ = data['time'].tolist()

            #generate array of lists and array of process IDs
            comm.send(X, dest=1)
            comm.send(Y, dest=2)
            comm.send(seconds_elapsed, dest=3)

            #process for rank 0, execute box_whisker for seconds_elapsed array

            #start timing computation of box whisker for process 0
            start_time = MPI.Wtime()
            box_whisker_values(seconds_elapsed, "Z")
            end_time = MPI.Wtime()
            execution_time = end_time - start_time
            print('')

            #receive timer values from each process and calculate total execution time
            total_time = execution_time
            total_time += comm.recv(source = 1)
            total_time += comm.recv(source = 2)
            total_time += comm.recv(source =3)

        #timing calcAOAulation of box whisker values for other processes
        elif rank == 1:
             receive = comm.recv()
             start_time = MPI.Wtime()
             box_whisker_values(receive, "X")
             end_time = MPI.Wtime()
             execution_time = end_time - start_time
             print('')
             comm.send(execution_time, dest = 0)

        elif rank == 2:
             receive = comm.recv()
             start_time = MPI.Wtime()
             box_whisker_values(receive, "Y")
             end_time = MPI.Wtime()
             execution_time = end_time - start_time
             print('')
             comm.send(execution_time, dest = 0)
        elif rank == 3:
             receive = comm.recv()
             start_time = MPI.Wtime()
             box_whisker_values(receive, "seconds_elapsed")
             end_time = MPI.Wtime()
             execution_time = end_time - start_time
             print('')
             comm.send(execution_time, dest = 0)


        if rank == 0:
            print("\nTotal time to execute box_and_whisker calculation is %s seconds\n\n"% total_time)

finally:
    #this is the built in function from Pandas to determine the box-and-whisker values to validate if the calculations from the box_whisker_values function are correct
          if rank == 0:

              data.dropna(inplace = True)
              print("\n\nThe results from pandas library built-in function to compute box-and-whisker values used to validate the correctness of the calculation:")
              da = data.describe()
              print("\n\n",da, end = "\n\n")
