import os 
import glob
from random import shuffle
from shutil import copyfile
INP_DIR = 'all_polyps/'
OUT_DIR = 'medico_2018_v2/'
DEMO_DIR = 'medico_demo/'
if not os.path.exists(OUT_DIR+'Main/'):
    os.makedirs(OUT_DIR+'Main/')
if not os.path.exists(OUT_DIR+'images/'):
    os.makedirs(OUT_DIR+'images/')
if not os.path.exists(OUT_DIR+'meta/'):
    os.makedirs(OUT_DIR+'meta/')
def merge():
    all_items = glob.glob(INP_DIR+'*/images/*.jpg')
    shuffle(all_items)
    shuffle(all_items)
    fo = open(OUT_DIR+'Main/all_img.txt',"w")
    for idx,item in enumerate(all_items):
        copyfile(item,OUT_DIR+'images/'+str(idx).zfill(5)+'.jpg')
        copyfile(item.replace('images','meta').replace('.jpg','.txt'),OUT_DIR+'meta/'+str(idx).zfill(5)+'.txt')
        fo.write(str(idx).zfill(5)+'\n')
    fo.close()
def write2file(inpList, outFile):
    fo = open(outFile,"w")
    for i in inpList:
        fo.write(i)
    fo.close()

def split():
    fi = open(OUT_DIR+'Main/all_img.txt',"r")
    items = fi.readlines()
    N = len(items)
    shuffle(items)
    TEST = items[:int(0.15 * N)]
    TRAIN = items[int(0.15 * N):]
    write2file(TEST,OUT_DIR+'Main/test.txt')
    write2file(TRAIN,OUT_DIR+'Main/trainval.txt')
    
def export_test_for_demo():
    fi = open(OUT_DIR+'Main/test.txt')
    if not os.path.exists(DEMO_DIR):
        os.makedirs(DEMO_DIR)
    items = fi.readlines()
    for item in items:
        print(item)
        copyfile(OUT_DIR+'images/'+item.strip()+'.jpg',DEMO_DIR+item.strip()+'.jpg')

if __name__ == '__main__':
    # merge()
    # split()
    export_test_for_demo()

