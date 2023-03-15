import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import mode
def knn(k_value,height, branch, tree, age):
    train = pd.read_csv('MOCK_DATA.csv')
    print(train)
    # read data from file
    cols = ['Height', 'Branch distance', 'Tree diameter','Age']
    train.rename(columns = {cols[0]:0, cols[1]:1, cols[2]:2, cols[3]:3}, inplace=True)
    train['distance'] = 9999
    # # rename columns header and set new column distances
    target = [height, branch, tree, age ] #pd.Series([30, 200, 180])
    # # create unidentified target columns to predict knn
    train['distance'] = ((train.loc[:,0]-target[0])**2 + (train.loc[:,1]-target[1])**2 + (train.loc[:,2]-target[2])**2 + (train.loc[:,3]-target[3])**2) ** 0.5
    train.loc[::10]
    # # calculate distances by using Euclidean distance
    k = k_value
    train = train.sort_values('distance', ascending=True)
    knn = list(train.head(k).Quality)
    # create graph
    # plotting(train, cols, target)
    return mode(knn)

# def plotting(train, cols, target):
#     colors = {'Poor':'red', 'Good':'Green'}

#     plt.scatter(train[0], train[3], c=train['Quality'].map(colors))
#     plt.show()
#     plt.scatter(target[0], target[3], c='Black', s=50)
#     plt.xlabel(cols[0])
#     plt.ylabel(cols[3])
    # plt.title('Body Scatter Plot')


# Ans = knn(10,5,7,10,100)
# print ("KNN = "+Ans)






    