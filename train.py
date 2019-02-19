import pre_data as pre
import pandas as pd
import numpy as np

tempp = []

for number in range(100):

    #number = int(input('Number of Jump : '))

    ans = pre.pre_data("train_data.csv",number)

    data = pre.d("train_data.csv")


    #print(data[len(data)-number-1:len(data)-1])

    for i in range(1326):
        #print (ans[data[len(data)-number-1:len(data)-1]])
        try:
            data+=ans[data[len(data)-number-1:len(data)-1]]
        except KeyError:
            continue

    #print(data)

    src = pre.d("AAPL.csv")

    percent = 0

    for i in range(len(data)):
        if(src[i] == data[i]):
            percent+=1

    percent = percent/len(data)

    if percent == 1 :
        break

    print(percent)

    tempp.append(percent)

for i in range(len(tempp)):
    if tempp[i] == max(tempp):
        print(i)

