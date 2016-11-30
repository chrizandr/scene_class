##########################################################################################
## Scene Classification                                                                 ##
## Authors : Chris Andrew, Santhoshini Reddy, Nikath Yasmeen, Sai Hima, Sriya Ragini    ##
###################################################################                     ##
## Description: This project was developed as part of the DIP course at IIIT Sri City   ##
## All code is available for free usage for educational purposes                        ##
## Authors do not authorize commercial use of the source code                           ##
##########################################################################################

# The following module is used to perform Linear Discriminant analysis on the given data set
# and transform to the best subspace. The module uses the scikit-learn library.

################ Imports ################
from sklearn.lda import LDA
################ Global ################
filenames = ["data_r"]
################ Source ################
# ------------------------------------
for filename in filenames:
    path = "data/"
    f = open(path+filename+".csv",'r')
    train_data = list()
    train_class = list()
    for line in f:
        l = line.strip()
        l = l.split(',')
        l = map(float , l)
        train_data.append(l[0:-1])
        train_class.append(int(l[-1]))
    f.close()
    # ------------------------------------
    clf = LDA()
    trans = clf.fit_transform(train_data,train_class)
    # ------------------------------------
    f = open(path+filename+"_LDA.csv",'w')
    # ------------------------------------
    for i in range(len(train_data)):
        for entry in trans[i]:
            f.write(str(entry)+',')
        f.write(str(train_class[i])+'\n')
    f.close()
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
