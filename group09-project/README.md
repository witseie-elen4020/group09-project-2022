# ELEN4020-Project
## Computing Box-Whisker values for IMU data on the Jaguar cluster
The main current working serial source code developed for this application is found in the src folder and is named **serial.py**.
Individual processes are launched for the computation and timed. The total execution time of the entire program is printed at the end of execution.
Only the computational part of the code is timed.

## Execution Instructions
In executing the program, the following are worth noting:
-python v2.7.18 has been used in developing the code
-The following additional libraries are needed to run the code
*1* pandas
*2* re
*4* numpy
*5* time
*6* sys

The group09 home folder of the jaguar cluster contains all the code for this application.
cd into the src folder through this filepath: **/home/group09/group09-project/src**.
Execute the script file named **serial.py** by typing **python3 serial.py* hit enter.

The range of time for this version is automically from the minimum to maximum value from the csv.
