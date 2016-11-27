import pdb
from sklearn.lda import LDA

filenames = ["new_r"]
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

    clf = LDA()
    trans = clf.fit_transform(train_data,train_class)

    f = open(path+filename+"_LDA.csv",'w')

    for i in range(len(train_data)):
        for entry in trans[i]:
            f.write(str(entry)+',')
        f.write(str(train_class[i])+'\n')
    f.close()
pdb.set_trace()
