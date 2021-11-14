import pandas as pd
import numpy as np
import csv
import math
from sklearn import neighbors, datasets
from numpy.random import permutation
from sklearn.metrics import precision_recall_fscore_support
from sklearn import svm
from pandas import DataFrame

cs_file = "cutofflist.csv"
data = pd.read_csv(cs_file,encoding= 'unicode_escape')
processed_data = data[['kcet','college']]
random_indices = permutation(data.index)
test_cutoff = math.floor(len(data)/5)
print(test_cutoff)
test = processed_data.loc[random_indices[1:test_cutoff]]
train = processed_data.loc[random_indices[test_cutoff:]]
train_output_data = train['college']
print("train Output data", train_output_data)
train_input_data = train
train_input_data = train_input_data.drop('college',1)
print("train input data", train_input_data)
test_output_data = test['college']
print("test Output data", test_output_data)
test_input_data = test
test_input_data = test_input_data.drop('college',1)
print("test input data", test_input_data)



class algorithms():
    
    def euclideanDistance(self,data1, data2, length):
        distance = 0
        for x in range(length):
            distance += np.square(data1[x] - data2[x])
        return np.sqrt(distance)


    def knn(self,trainingSet, testInstance, k):
        print(k)
        distances = {}
        sort = {}
        length = testInstance.shape[1]
        for x in range(len(trainingSet)):
            dist = self.euclideanDistance(testInstance, trainingSet.iloc[x], length)
            distances[x] = dist[0]
        sorted_d = sorted(distances.items(), key=lambda x: x[1])
        neighbors = []
        for x in range(k):
            neighbors.append(sorted_d[x][0])
        classVotes = {}
        for x in range(len(neighbors)):
            response = trainingSet.iloc[neighbors[x]][-1]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=lambda x: x[1], reverse=True)
        return (sortedVotes, neighbors)
                    
    def predictSVM(self,kcet):
        clf =svm.SVC(kernel='linear')    
        clf.fit(train_input_data,train_output_data)
        marks=float(kcet)
        output_college1=clf.predict([[marks]])
        output_college=output_college1[0]
        return output_college
    
    def predictKNN(self,kcet):
        data = pd.read_csv('cutofflist.csv',encoding= 'unicode_escape')
        kcet = float(kcet)
        testSet = [[kcet]]
        test = pd.DataFrame(testSet)
        k = 5
        result, neigh = self.knn(processed_data, test, k)
        list1 = []
        list2 = []
        for i in result:
            list1.append(i[0])
        for i in result:
            list2.append(i[1])
        for i in list1:
            print(i)
        return list1
    
    def top_ten(self):
        data = pd.read_csv('cutofflist.csv',encoding= 'unicode_escape')
        my_list1=data.nlargest(10, ['kcet'])
        my_list=my_list1.values.tolist()
        return my_list
    
    def get_by_range(self,start,end,results):
        res=results
        data = pd.read_csv('cutofflist.csv',encoding= 'unicode_escape')
        my_data=data = data[(data['kcet'] >= start) & (data['kcet'] <= end)]
        l1=data.head(res)
        my_list=l1.values.tolist()  
        return my_list

        
        




