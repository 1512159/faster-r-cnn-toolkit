import glob
import os
from shutil import copyfile,rmtree
NAME = 'normal-z-line'
INP_DIR = 'normal-z-line/'
OUT_DIR = 'demo_to_dataset/'+INP_DIR
IMG_DIR = OUT_DIR + 'images/'
META_DIR = OUT_DIR + 'meta/'

def create(dir_path):
    if not os.path.exists(dir_path):
        rmtree(dir_path, ignore_errors=True)
        os.makedirs(dir_path)

create(OUT_DIR)
create(IMG_DIR)
create(META_DIR)

items = glob.glob(INP_DIR+'*.txt')
count = 0
for i,item in enumerate(items):
    fi = open(item,"r")
    lines = fi.readlines()
    if len(lines)==0:
        continue
    count += 1
    fo = open(META_DIR+str(i).zfill(5)+'.txt',"w")
    for line in lines:
        info = line.strip().split(' ')
        x1 = str(int(float(info[2])))
        y1 = str(int(float(info[3])))
        x2 = str(int(float(info[4])))
        y2 = str(int(float(info[5])))
        fo.write(x1+' '+y1+' '+x2+' '+y2+' '+NAME+'\n')
    fo.close()
    copyfile(item.replace('.txt','.jpg'),IMG_DIR+str(i).zfill(5)+'.jpg')

print('Total: '+str(count))


