from random import shuffle

path = "data/"
filename = "new"

f = open(path+filename+".csv",'r')
data = list()
train_data = list()
train_class = list()

for line in f:
    l = line.strip()
    l = l.split(',')
    l = map(float , l)
    data.append(l)
f.close()

for i in range(100):
    shuffle(data)

for l in data:
    train_data.append(l[0:-1])
    train_class.append(int(l[-1]))

f = open(path+filename+"_r.csv",'w')
for i in range(len(train_data)):
    for entry in train_data[i]:
        f.write(str(entry)+',')
    f.write(str(train_class[i])+'\n')
f.close()
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
