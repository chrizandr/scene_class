import cv2
import numpy as np
import pdb
import os

from Gabor import *
from normalize import *
from segment import *

def label(dir):
    if dir == "coast/" or dir == "street/" or dir ==  "inside_city/" or dir == "tallbuilding/":
        return '1'
    else:
        return '0'

# Frequencies, orientations and the Gaussian envelope used are declared globally first
frequencies = [4,8,16,32]
angles = map(getangle , [0,45,90,135,180,225,270,315])
gkernel = makeGaussianKernel((4,4),3)

G_filters = list()

for frequency in frequencies:
    for angle in angles:
        kernel = makeGaborKernel(gkernel,frequency,angle)
        G_filters.append(kernel)

f = open("data/raw.csv", "wb")
base_dir = "/home/chris/sem5/DIP/Project/dataset/"
sub_dirs = ["coast/" , "highway/" , "mountain/" , "street/" , "forest/" , "inside_city/" , "Opencountry/" , "tallbuilding/"]

for sub_dir in sub_dirs:
    files = os.listdir(base_dir + sub_dir)
    for name in files:
        if name[-4:] == ".jpg":
            print "Processing ",base_dir + sub_dir + name
            img = cv2.imread(base_dir + sub_dir + name)
            g_img = img[:,:,0] + img[:,:,1] + img[:,:,2]
            g_img = g_img / 3
            ng_img = normalizeImage(g_img,'g')
            segments = segmentImage(ng_img)
            vector = list()
            for segment in segments:
                for pair in G_filters:
                    filter_p = pair[0]
                    filter_n = pair[1]
                    gamma = powerSpectrum(segment)
                    G_p = Gaborfilter(segment,filter_p)
                    G_n = Gaborfilter(segment,filter_n)
                    feature = (gamma*G_p) - (gamma*G_n)
                    vector.append(feature.sum())
            for i in vector:
                f.write(str(i)+',')
            f.write(label(sub_dir)+'\n')
            print "No errors"
f.close()
print "Done :)"
pdb.set_trace()
