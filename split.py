import os
from random import sample
from shutil import copyfile


def split_data(dir,frac,train='trainA'):

    files = os.listdir(dir)
    nbr = int(len(files)*frac)
    selected_files =  sample(files, nbr)
    res_dir='./summer2winter_splitted/data_'+str(frac*100)+'/'+train
    if not os.path.isdir(res_dir):
        os.makedirs(res_dir)
    
    for i in range(len(selected_files)):
        source = os.path.join(dir,selected_files[i])
        target = os.path.join(res_dir,selected_files[i])
        copyfile(source,target)


per = [0.2,0.4,0.6,0.8,1.0]



for i in per:
    dir1 = './summer2winter/trainA'
    split_data(dir1,i,'trainA')
    dir2 = './summer2winter/trainB'
    split_data(dir2,i,'trainB')

## split 40 
#split_data(dir1,0.4,'trainA')
#split_data(dir2,0.4,'trainB')

## split 60 
#split_data(dir1,0.6,'trainA')
#split_data(dir2,0.6,'trainB')

## split 80 
#split_data(dir1,0.8,'trainA')
#split_data(dir2,0.8,'trainB')

## split 80 
#split_data(dir1,1,'trainA')
#split_data(dir2,1,'trainB')

