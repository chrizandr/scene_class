##########################################################################################
## Scene Classification                                                                 ##
## Authors : Chris Andrew, Santhoshini Reddy, Nikath Yasmeen, Sai Hima, Sriya Ragini    ##
###################################################################                     ##
## Description: This project was developed as part of the DIP course at IIIT Sri City   ##
## All code is available for free usage for educational purposes                        ##
## Authors do not authorize commercial use of the source code                           ##
##########################################################################################

################ Imports ################
import cv2
################ Source ################
# ---------------------------------------------------------------------
# For illumination normalization we decided to go with global histogram equilization
# Local histogram equilization can also be acheived for the image, which is more useful in retaining fine features
# Since we were mostly interested in the structure of the image rather than the finer details in it, we went for global equilization
# The function normalizeImage does both local and global equilization based on the whether the flag parameter is set to "g" or "l"
# ---------------------------------------------------------------------
# normalizeImage(img , flag) -> result
# img : input image
# flag : flag to identify the type of normalization to be done (flag in ['g','l'])
# result : normalized image
# ------------------------------------
def normalizeImage(img, flag):
        r_img = None
        if flag == 'g':
            r_img = cv2.equalizeHist(img)
        elif flag == 'l':
            clahe = cv2.createCLAHE()
            r_img = clahe.apply(img)
        return r_img
