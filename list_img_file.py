import glob
import os
lists = glob.glob('medico_2018_trainval_v1/images/*.jpg')
fo = open('trainval.txt',"w")
for i in lists:
    fo.write(os.path.basename(i).replace('.jpg','')+'\n')
fo.close()
