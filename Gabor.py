##########################################################################################
## Scene Classification                                                                 ##
## Authors : Chris Andrew, Santhoshini Reddy, Nikath Yasmeen, Sai Hima, Sriya Ragini    ##
###################################################################                     ##
## Description: This project was developed as part of the DIP course at IIIT Sri City   ##
## All code is available for free usage for educational purposes                        ##
## Authors do not authorize commercial use of the source code                           ##
##########################################################################################

################ Imports ################
from cv2 import getGaussianKernel
import numpy as np
################ Source ################


# makeGaborKernel creates two Gabor filters of opposite symmetry to be used for Gabor filtering of the image
# makeGaborKernel(gkernel , f , theta) -> he , ho
# gkernel : numpy 2D array that contains the gaussian kernel that is to be used to create the filters
# f : frequency of the filters
# theta : orientation of the filter
# he , ho : the output filters coresponding to opposite symmetry filters (he : sin wave filter , ho : cosine wave filter )
def makeGaborKernel(gkernel,f,theta):
    he=np.arange(gkernel.size).reshape(gkernel.shape)
    ho=np.arange(gkernel.size).reshape(gkernel.shape)
    he=he.astype(np.float64)
    ho=ho.astype(np.float64)
    for i in range(he.shape[0]):
        for j in range(he.shape[1]):
            val= 2*np.pi*f*((i+1)*np.cos(theta)+(j+1)*np.sin(theta))
            he[i,j]=gkernel[i,j]*np.cos(val)
    for i in range(ho.shape[0]):
        for j in range(ho.shape[1]):
            val= 2*np.pi*f*((i+1)*np.cos(theta)+(j+1)*np.sin(theta))
            ho[i,j]=gkernel[i,j]*np.sin(val)
    return he,ho

def makeGaussianKernel(ksize, sigma):
    kx=getGaussianKernel(ksize[0],sigma);
    ky=getGaussianKernel(ksize[1],sigma);
    kernel = kx*ky.transpose()
    return kernel
