# ELEN4020-Project

## Computing Box-Whisker values for IMU data on the Jaguar cluster
The main source code developed for this application is found in the src folder and is named **parallel.py**.
Individual processes are launched for the computation and timed. The total execution time of the entire program
is printed at the end of execution. program can read csv file in any directory in th /data folder.
The program compute box_whisker for the whole data data.

#parallel program
In executing the program, the following are worth noting:
-python v3.10.0 has been used in developing the code
-The following additional libraries are needed to run the code
.pandas
.mpi4py
.re
.sys
.numpy
.time

##To run this program

directory path for csv file should be supplied as rguments argument.The group09 home folder of the jaguar cluster
contains all the code for this application. 
cd into the scripts folder through this filepath: **/home/group09/group09-project-2022/group09-project/scripts**.
Execute the script file named **execute.sh** by typing **sh execute.sh** hit enter. 
This should run the **parallel.py** which is found in **/home/group09-project-2022/group09-project/src**.
To run a different file, open the exeute.sh file and replace the directory path of the csv file

##example of command to running the program to test a smal file:
srun -c 4 -n 4 --mpi=pmi2  python3 serial.py /data/elen4020/project/small/9IWgmjUj.csv

##example of command to running the program to test a smal file:
srun -c 4 -n 4 --mpi=pmi2  python3 serial.py /data/elen4020/project/large/TZEoekWF.csv


You can just simple cd into **/home/group09-project-2022/group09-project/src** and run the command above in the 
bash terminal.
  
###-n = number of processes
###-c = number of cpu(s) per process

#if you use the gitHUb code just cd into the /group09-project-2022/group09-project/scripts and execute the bash srcipt
#or cd into /group09-project-2022/group09-project/src and run the command example above in bash terminal following the same steps above. 



