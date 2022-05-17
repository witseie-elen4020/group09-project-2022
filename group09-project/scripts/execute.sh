#! /bin/bash

#export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
cd /home/group09/group09-project-2022/group09-project/src
#-n = number of processes
#-c = number of cpu(s) per process
#number of processes specified should be equal to the number of 4 data sets (X, Y, Z and seconds_elapsed) = 4 processes
srun -c 4 -n 4 --mpi=pmi2 python3 parallel.py /data/elen4020/project/small/9IWgmjUj.csv
