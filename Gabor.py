##########################################################################################
## Scene Classification                                                                 ##
## Authors : Chris Andrew, Santhoshini Reddy, Nikath Yasmeen, Sai Hima, Sriya Ragini    ##
###################################################################                     ##
## Description: This project was developed as part of the DIP course at IIIT Sri City   ##
## All code is available for free usage for educational purposes                        ##
## Authors do not authorize commercial use of the source code                           ##
##########################################################################################

################ Imports ################
from cv2 import getGaussianKernel, filter2D
import numpy as np
################ Source ################

# ---------------------------------------------------------------------
# makeGaborKernel creates two Gabor filters of opposite symmetry to be used for Gabor filtering of the image
# makeGaborKernel(gkernel , f , theta) -> he , ho
# gkernel : numpy 2D array(float) that contains the gaussian kernel that is to be used to create the filters
# f : frequency of the filters : float(cycles/pixel)
# theta : orientation of the filter : float (radians)
# he , ho : the output filters coresponding to opposite symmetry filters (he : sin wave filter , ho : cosine wave filter )
# ------------------------------------
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

# ---------------------------------------------------------------------
# makeGaussianKernel creates 2D gaussian kernel of specified size and variance
# ksize : size of the gaussian kernel : 2 tuple integers (m,n) [m rows and n columns]
# sigma : variance of the kernel : float
# ------------------------------------
def makeGaussianKernel(ksize, sigma):
    kx=getGaussianKernel(ksize[0],sigma);
    ky=getGaussianKernel(ksize[1],sigma);
    kernel = kx*ky.transpose()
    return kernel

# ---------------------------------------------------------------------
# Gaborfilter creates the gaussian enveloped power spectrum of the image.
# img : input image
# kernel : numpy 2D array(float) that contains the Gabor kernel that is to be used
# p_spectrum : The resultant Gaussian enveloped power spectrum
# ------------------------------------
def Gaborfilter(img, kernel):
    r_img = filter2D(img,-1,kernel)
    f = np.fft.fft2(r_img)
    fshift = np.fft.fftshift(f)
    p_spectrum = np.abs(fshift)
    p_spectrum = p_spectrum * p_spectrum
    return p_spectrum

# ---------------------------------------------------------------------
# powerSpectrum returns the absolute squared power spectrum of the frequency domain representation of the image
# img : input image
# p_spectrum : The resultant power spectrum
def powerSpectrum(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    p_spectrum = np.abs(fshift)
    p_spectrum = p_spectrum * p_spectrum
    return p_spectrum
