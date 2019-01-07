import numpy as np
import pandas as pd 
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime

A = []
B = []

stocks = 'AAPL'

start_date='01/01/2010'
end_date ='01/01/2017'

data = web.DataReader(stocks,data_source='yahoo',start=start_date,end=end_date)['Adj Close']

U = 0
E = 0
D = 0

for i in range(1,len(data)):
    if data[i] > data[i-1]:
        A.append('U')
        U += 1
    elif data[i] == data[i-1]:
        A.append('E')
        E += 1
    elif data[i] < data[i-1]:
        A.append('D')
        D += 1
UU = 0
UD = 0
UE = 0
DU = 0
DD = 0
DE = 0
EU = 0
ED = 0
EE = 0
count = 0

for i in range(len(A)):
    if A[i-1] == 'U':
        if A[i] == 'U':
            UU += 1
            count += 1
        elif A[i] == 'D':
            UD += 1
            count += 1
        elif A[i] == 'E':
            UE += 1
            count += 1
    elif A[i-1] == 'D':
        if A[i] == 'U':
            DU += 1
            count += 1
        elif A[i] == 'D':
            DD += 1
            count += 1
        elif A[i] == 'E':
            DE += 1
            count += 1
    elif A[i-1] == 'E':
        if A[i] == 'U':
            EU += 1
            count += 1
        elif A[i] == 'D':
            ED += 1
            count += 1
        elif A[i] == 'E':
            EE += 1
            count += 1

print('P(U[t]|U[t-1]) =',(UU/count)/(U/len(A)))
print('P(U[t]|D[t-1]) =',(UD/count)/(D/len(A)))
print('P(U[t]|E[t-1]) =',(UE/count)/(E/len(A)))
print('P(D[t]|U[t-1]) =',(DU/count)/(U/len(A)))
print('P(D[t]|D[t-1]) =',(DD/count)/(D/len(A)))
print('P(D[t]|E[t-1]) =',(DE/count)/(E/len(A)))
print('P(E[t]|U[t-1]) =',(EU/count)/(U/len(A)))
print('P(E[t]|D[t-1]) =',(ED/count)/(D/len(A)))
print('P(E[t]|E[t-1]) =',(EE/count)/(E/len(A)))