import cv2
import numpy as np
import pdb
from Gabor import *


def getangle(n):
    return (np.float64)(n*np.pi)/180

# Frequencies, orientations and the Gaussian envelope used are declared globally first
frequencies = [1/4,1/8,1/16,1/32]
angles = map(getangle , [0,45,90,135,180,225,270,315])
gkernel = makeGaussianKernel((4,4),3)

G_filters = list()

for frequency in frequencies:
    for angle in angles:
        kernel = makeGaborKernel(gkernel,frequency,angle)
        G_filters.append(kernel)

for pair in G_filters:
    filter_p = pair[0]
    filter_n = pair[1]
