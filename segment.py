##########################################################################################
## Scene Classification                                                                 ##
## Authors : Chris Andrew, Santhoshini Reddy, Nikath Yasmeen, Sai Hima, Sriya Ragini    ##
###################################################################                     ##
## Description: This project was developed as part of the DIP course at IIIT Sri City   ##
## All code is available for free usage for educational purposes                        ##
## Authors do not authorize commercial use of the source code                           ##
##########################################################################################

# The module divides a given 256x256 image into 16 64x64 images

################ Imports ################
import numpy as np
################ Source ################
# ------------------------------------
def segmentImage(img):
    # ------------------------------------
    if img.shape == (256,256):
        segments = list()
        for i in range(0,256,64):
            for j in range(0,256,64):
                segments.append(img[i:i+64,j:j+64])
        return segments
    # ------------------------------------
    else:
        return None
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
