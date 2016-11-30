##########################################################################################
## Scene Classification                                                                 ##
## Authors : Chris Andrew, Santhoshini Reddy, Nikath Yasmeen, Sai Hima, Sriya Ragini    ##
###################################################################                     ##
## Description: This project was developed as part of the DIP course at IIIT Sri City   ##
## All code is available for free usage for educational purposes                        ##
## Authors do not authorize commercial use of the source code                           ##
##########################################################################################

# The following module shuffles the data to enable 10 fold cross-validation analysis

################ Imports ################
from random import shuffle
################ Global ################
path = "data/"
filename = "data"
################ Source ################
# ------------------------------------
f = open(path+filename+".csv",'r')
data = list()
train_data = list()
train_class = list()
# ------------------------------------
for line in f:
    l = line.strip()
    l = l.split(',')
    l = map(float , l)
    data.append(l)
    # ------------------------------------
f.close()
# ------------------------------------
for i in range(100):
    shuffle(data)
# ------------------------------------
for l in data:
    train_data.append(l[0:-1])
    train_class.append(int(l[-1]))
# ------------------------------------
f = open(path+filename+"_r.csv",'w')
for i in range(len(train_data)):
    for entry in train_data[i]:
        f.write(str(entry)+',')
        # ------------------------------------
    f.write(str(train_class[i])+'\n')
    # ------------------------------------
f.close()
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
