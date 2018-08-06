import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob
import os
from random import shuffle

lists = glob.glob('input/*/Ground Truth/*.tif')
shuffle(lists)

if (not os.path.exists('output/')):
    os.makedirs('output/')

if (not os.path.exists('output/images')):
    os.makedirs('output/images')

if (not os.path.exists('output/meta')):
    os.makedirs('output/meta')

for i,name in enumerate(lists):
    img_path = name.replace('Ground Truth','Original').replace('tif','jpeg')
    if not os.path.exists(img_path):
        continue

    tmp = cv2.imread(img_path)
    cv2.imwrite('output/images/'+str(i).zfill(5)+'.jpg',tmp)

    img = cv2.imread(name,cv2.IMREAD_GRAYSCALE)
    c = np.where(img==(255))
    
    minx = np.min(c[1])
    miny = np.min(c[0])
    maxx = np.max(c[1])
    maxy = np.max(c[0])

    fo = open('output/meta/'+str(i).zfill(5)+'.txt',"w")
    fo.write(str(minx)+' '+str(miny)+' '+str(maxx)+' '+str(maxy)+' polyp')
    fo.close()



# print(minx,miny,maxx,maxy)

# img2 = cv2.imread('output/images/00019.jpg',cv2.IMREAD_COLOR)
# img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

# fo = open('output/meta/00019.txt')
# tmp = fo.readline().split(' ')
# cv2.rectangle(img2,(int(tmp[0]),int(tmp[1])),(int(tmp[2]),int(tmp[3])),(0,255,0),3) 
# plt.subplot(121)
# plt.imshow(img2)
# plt.subplot(122)
# plt.imshow(img2)
# plt.show()

