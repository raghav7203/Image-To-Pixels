import os,png,array
import csv
import numpy as np
import pandas as pd

import time

from PIL import Image


os.chdir('zero/')

columnNames = list()

for i in range(784):
    pixel = 'pixel'
    pixel += str(i)
    columnNames.append(pixel)


train_data = pd.DataFrame(columns = columnNames)
start_time = time.time()
for i in range(1,8):
    t = i
    img_name = str(t)+'.png'
    img = Image.open(img_name)
    rawData = img.load()
        #print rawData
    data = []
    for y in range(28):
        for x in range(28):
            data.append(rawData[x,y][0])
    print (i)
    k = 0
        #print data
    train_data.loc[i] = [data[k] for k in range(784)]
    #print train_data.loc[0]

print ("Done")
print  (time.time()-start_time)
print (train_data)

train_data.to_csv("train_converted.csv",index = False)
print ("Done1")
print  (time.time()-start_time)




data = pd.read_csv("train_converted.csv")

labels = ['0' for i in range(7)]

data.insert(0, "label", labels)

data.to_csv("output.csv",index = False)

os.remove('train_converted.csv')
