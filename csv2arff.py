##########################################################################################
## Scene Classification                                                                 ##
## Authors : Chris Andrew, Santhoshini Reddy, Nikath Yasmeen, Sai Hima, Sriya Ragini    ##
###################################################################                     ##
## Description: This project was developed as part of the DIP course at IIIT Sri City   ##
## All code is available for free usage for educational purposes                        ##
## Authors do not authorize commercial use of the source code                           ##
##########################################################################################

################ Imports ################
# No imports
################ Global ################
folder = "data/"
names = ["data_r_LDA"]
################ Source ################
for name in names:
    train_file = open(folder+name+".csv","r")
    train_data=[]
    train_class=[]
    for line in train_file:
        l = line.strip()
        l = l.split(',')
        l = map(float , l)
        train_data.append(l[0:-1])
        train_class.append(int(l[-1]))
    classnumb = []
    for i in train_class:
        if i not in classnumb:
            classnumb.append(i)
    attribs = len(train_data[0])
    arrfile = open(folder+name+".arff","w")
    arrfile.write("@RELATION " + name + '\n')
    for i in range(attribs):
        arrfile.write("@ATTRIBUTE a"+str(i)+" NUMERIC\n")
    arrfile.write("@ATTRIBUTE class {")
    for i in range(len(classnumb)-1):
        arrfile.write(str(classnumb[i])+',')
    arrfile.write(str(classnumb[len(classnumb)-1])+"}\n")
    arrfile.write("@DATA\n")
    for i in range(len(train_data)):
        for j in train_data[i]:
            arrfile.write(str(j)+",")
        arrfile.write(str(train_class[i])+"\n")
    arrfile.close()
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
