#!/usr/bin/env python
# Attribution: https://medium.com/python-in-plain-english/pandas-and-multiprocessing-how-to-create-dataframes-in-a-parallel-way-72f9b18ea72f
import pandas
import psutil
import time
import os
from pathlib import Path
from multiprocessing import Pool
def get_files(directory,pattern):
    '''
    Get the files of a directory
    '''
    for path in Path(directory).rglob(pattern):
        yield path.absolute()
def process_file(filename):
    ''''
    Read an xls file, retun a dataframe   
    ''''
    return pandas.read_excel(filename,index_col=None)
def pd_wrapper(directory,pattern,processes=-1):
    # Decide how many proccesses will be created
    sum_size = 0
    if processes <=0:
        num_cpus = psutil.cpu_count(logical=False)
    else:
        num_cpus = processes
   files = []
   # Get files based on pattern and their sum of size
   for file in get_files(directory=directory,pattern=pattern):
       sum_size =sum_size + os.path.getsize(file)
       files.append(file)
    print('files:%s,size:%s bytes, procs:%s'%(len(files),sum_size,num_cpus))
    # Create the pool
    process_pool = Pool(processes=num_cpus)
    start = time.time()
    # Start processes in the pool
    dfs = process_pool.map(process_file, files)
    # Concat dataframes to one dataframe
    data = pandas.concat(dfs, ignore_index=True)
    end = time.time()
    print('Completed in: %s sec'%(end - start))
    return data
if __name__ == '__main__':
    #control how many processes you have at once with processes
    df = pd_wrapper(directory='./xls',pattern='*.xls',processes=-1)
    print(df.count)