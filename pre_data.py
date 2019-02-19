import pandas as pd
import numpy as np

def pre_data(name_of_file,number_of_value):

    data = pd.read_csv(name_of_file)

    dt_close = np.array(data['Close'])

    sim_return = []

    #print(dt_close)

    for i in range(1,len(dt_close)):
        #print(i)
        sim_return.append((dt_close[i]-dt_close[i-1])/dt_close[i-1])

    #print(sim_return)

    state = []
    for i in range(1,len(sim_return)):
        if sim_return[i-1] < sim_return[i]:
            state.append('U')
        elif sim_return[i-1] > sim_return[i]:
            state.append('D')
        elif sim_return[i-1] == sim_return[i]:
            state.append('E')
        else:
            sim_return[i] = sim_return[i-1]
            i-=1


    #print(state)

    tmp = []

    for i in range(0,len(state)-(number_of_value+1)):
        tempp = ''
        if state[i+(number_of_value+1)] == 'U':
            for c in state[i:i+(number_of_value+1)]:
                tempp = tempp+c
            tmp.append(tempp)
            # print("U ",state[i:i+(number_of_value)])
        elif state[i+(number_of_value+1)] == 'D':
            for c in state[i:i+(number_of_value+1)]:
                tempp = tempp+c
            tmp.append(tempp)
            # print("D ",state[i:i+(number_of_value)])
        elif state[i+(number_of_value+1)] == 'E':
            for c in state[i:i+(number_of_value+1)]:
                tempp = tempp+c
            tmp.append(tempp)
            # print("E ",state[i:i+(number_of_value)])

    # print(tmpU)
    # print(tmpD)
    # print(tmpE)

    d_train = {}

    #print (tmp[0][:number_of_value])

    for i in tmp:

        #print(number_of_value)
        d_train.setdefault(i[:number_of_value],{})
        d_train[i[:number_of_value]].setdefault('U',0)
        d_train[i[:number_of_value]].setdefault('D',0)
        d_train[i[:number_of_value]].setdefault('E',0)
        d_train[i[:number_of_value]].setdefault('MAX')
        d_train[i[:number_of_value]][i[number_of_value]] = d_train[i[:number_of_value]][i[number_of_value]]+1

        maxx = 'U'
        if d_train[i[:number_of_value]]['D'] > d_train[i[:number_of_value]]['U'] and d_train[i[:number_of_value]]['D'] > d_train[i[:number_of_value]]['E']:
            maxx = 'D'
        if d_train[i[:number_of_value]]['E'] > d_train[i[:number_of_value]]['D'] and d_train[i[:number_of_value]]['E'] > d_train[i[:number_of_value]]['U']:
            maxx = 'E'
        
        d_train[i[:number_of_value]]['MAX'] = maxx

    #print (d_train['UUDEU'])

    ans = {}
    for i in d_train:
        #print (i)
        ans.setdefault(i,d_train[i]['MAX'])

    return ans

def d(name_of_file):

    data = pd.read_csv(name_of_file)

    dt_close = np.array(data['Close'])

    sim_return = []

    #print(dt_close)

    for i in range(1,len(dt_close)):
        #print(i)
        sim_return.append((dt_close[i]-dt_close[i-1])/dt_close[i-1])

    #print(sim_return)

    state = []
    for i in range(1,len(sim_return)):
        if sim_return[i-1] < sim_return[i]:
            state.append('U')
        elif sim_return[i-1] > sim_return[i]:
            state.append('D')
        elif sim_return[i-1] == sim_return[i]:
            state.append('E')
        else:
            sim_return[i] = sim_return[i-1]
            i-=1
    ans = ''
    for i in state:
        ans+=i

    return ans


if __name__ == "__main__":
    print(pre_data(input('Name of File : '),int(input('Jump : '))))