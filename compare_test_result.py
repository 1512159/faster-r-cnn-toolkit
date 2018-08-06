import os
import glob
from matplotlib import pyplot as plt 
from matplotlib import patches 
import cv2

IMDB_TEST = 'medico_2018_v2/images/'
META_DB   = 'medico_2018_v2/meta/'
DEMO_RESULT = 'demo_result_v2_3/'
TEST_RESULT = 'test_result/dyed-lifted-polyp.txt'
OUTPUT_DIR = 'compare_result/'
imgname = '00448' 
def process(imgname):
    gt_img = cv2.imread(IMDB_TEST+imgname+'.jpg')
    gt_img = cv2.cvtColor(gt_img,cv2.COLOR_BGR2RGB)

    fi = open(META_DB+imgname+'.txt',"r")
    lines = fi.readlines()
    fig,ax = plt.subplots(1)
    # plt.subplot(122)
    plt.imshow(gt_img)
    # plt.imshow()
    for line in lines:
        info = line.split(' ')
        x1 = int(info[0])
        y1 = int(info[1])
        x2 = int(info[2])
        y2 = int(info[3])
        name = info[4].strip()
        rect = patches.Rectangle((x1,y1), x2 - x1, y2 - y1, fill=False,
                            edgecolor='green', linewidth=2)
        ax.add_patch(rect)
        plt.text(x1, y1-10,
                        '{:s}'.format(name),
                        bbox=dict(facecolor='green', alpha=0.5),
                        fontsize=5, color='white')
    fi.close()
    #DRAW RESULT BBOX
    fi = open(DEMO_RESULT+'result_'+imgname+'.txt',"r")
    lines = fi.readlines()
    plt.imshow(gt_img)
    for line in lines:
        info = line.strip().split(' ')
        name = info[0]
        score = float(info[1])
        x1 = int(float(info[2]))
        y1 = int(float(info[3]))
        x2 = int(float(info[4]))
        y2 = int(float(info[5]))
        
        rect = patches.Rectangle((x1,y1), x2 - x1, y2 - y1, fill=False,
                            edgecolor='red', linewidth=2)
        ax.add_patch(rect)
        plt.text(x1, y2+10,
                        '{:s} {:.3f}'.format(name,score),
                        bbox=dict(facecolor='red', alpha=0.5),
                        fontsize=5, color='white')
    fi.close()
    plt.axis('off')
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    plt.savefig(OUTPUT_DIR+'/'+imgname+'.jpg')
    plt.close('all')
# plt.show()

fi = open(TEST_RESULT)
lines = fi.readlines()
for line in lines:
    line = line.strip()
    info = line.split(' ')
    if info[0] != 'correct':
        print(info[1])
        process(info[1])