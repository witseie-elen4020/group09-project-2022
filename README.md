# ELEN4020-Project

The src contains two python scripts, the serial.py which compute the box-whisker values for the maximum time range of the csv file and the parallel.py which is not 
yet complete but currently allow the user to insert the mimimum and maximum time values specifying the range to compute the box_whisker values.

#serial program:
In executing the program, the following are worth noting:
-python v3.10.0 has been used in developing the code
-The following additional libraries are needed to run the code
 . pandas
 . re
 . numpy
 . time
 . sys

-he serial.py does a normal execution of box_whisker computation. the group09-project folder of the jaguar cluster contains all the code for the serial.py.
-cd into the src folder throught the filepath /home/group09/group09-project/src.
-Execute the script file named serial.py by typing 'python3 serial.py directoryOfTheCSVFleToTest'

 example: python3 serial.py /data/elen4020/project/small/9IWgmjUj.csv

-note the last argument should be the path to the CSV file you want to test. the serial program is designed to allow different CSV files from different directory
to be tested. hence only up to 500 mb files can be tested and beyond that the execution time takes more that 4 minutes to execute large data csv files of 1MG and above
 
#parallel program
as stated this program is not yet complete to perform multiprocessing. this is currently a serial program that is modified to either take two arguments or four arguments

-For two arguments: similar to serial.py file, supply the python script name and the directory of the csv file to compute the box_whisker. the parallel will compute box_whosker 
for the maximum time range of the csv file from the lowest time value to the maximum time value

 example: python3 serial.py /data/elen4020/project/small/9IWgmjUj.csv

-For four arguments: supply the python script name, the directory of the csv file to compute box_whisker, the minimum and maximum time values to specify the time range where to
compute box-whisker. The minumum and maximum time values can be picked from the csv file by typing "cat filedirectory"to view and pick your range values. 

example: cat /data/elen4020/project/small/9IWgmjUj.csv       => this will display the (IWgmjUj.csv data file where one could choose the time ranges and be extra sure to pick correct time values values)

now example to execute box_whisker with time range parallel.py: python3 parallel.py /data/elen4020/project/small/9IWgmjUj.csv 1577972805874981400 1577972805906871000

## Computing Box-Whisker values for IMU data on the Jaguar cluster
The total execution time of the entire program is timed for only the box_whisker computation and displayed. and aslo the built in function from Pandas library to compute box_whisker values is used to validate the 
correctnes of the results.

#if you use the gitHUb code just cd into the src in bash command line and follow the same steps above. the MakeFile is yet to be made. 
