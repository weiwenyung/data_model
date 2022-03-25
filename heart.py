import pandas as pd
from sklearn import ensemble
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import accuracy_score
def step1():
    df = pd.read_csv('heart.csv')
    n = len(df) + 1
    nlist = range(1,n)
    df.insert(0, "ID" , nlist)
    df.to_csv('step1.csv',index = 0,header = 1)
def step2(number,number1):
    df1 = pd.read_csv('step1.csv')
    training_data, testing_data = train_test_split(df1, test_size =int(number1)/100)
    training_data.to_csv('training_data.csv', index = 0 ,header = 1)
    testing_data.to_csv('testing_data.csv', index = 0 ,header = 1)
    df2atr = training_data.iloc[:,:int (number) + 1]
    df2btr1 = training_data.iloc[:,:1]
    df2btr2 = training_data.iloc[:,int (number) + 1 : int (len(training_data.columns)) - 1 ]
    df2btr = pd.concat([df2btr1,df2btr2], axis = 1)
    df2atr.to_csv('step2A_training.csv', index = 0 , header = 1)
    df2btr.to_csv('step2B_training.csv', index = 0 , header = 1)
    df2ate = testing_data.iloc[:,:int (number) + 1]
    df2bte1 = testing_data.iloc[:,:1]
    df2bte2 = testing_data.iloc[:,int (number) + 1 : int (len(testing_data.columns)) - 1 ]
    df2bte = pd.concat([df2bte1, df2bte2], axis = 1)
    df2ate.to_csv('step2A_testing.csv', index = 0 , header = 1)
    df2bte.to_csv('step2B_testing.csv', index = 0 , header = 1)
def step3(AttributesA,AttributesB):
    for a in range(0,len(AttributesA)):
        age_max = df2atr[(AttributesA[a])].max()
        age_min = df2atr[(AttributesA[a])].min()
        average = ((age_max - age_min) +1) / int(segmentation)
        df2atr[(AttributesA[a])] = ((df2atr[(AttributesA[a])] - age_min) // average) + 1
    for b in range(0,len(AttributesB)):
        age_max = df2btr[(AttributesB[b])].max()
        age_min = df2btr[(AttributesB[b])].min()
        average = ((age_max - age_min) +1) / int(segmentation)
        df2btr[(AttributesB[b])] = ((df2btr[(AttributesB[b])] - age_min) // average) + 1
    df2atr.to_csv('step3A_training.csv', index = 0, header = 1)
    df2btr.to_csv('step3B_training.csv', index = 0, header = 1)
def ak1():
    df3atr = pd.read_csv('step3A_training.csv')
    alist = list()
    for i in range(0,len(df3atr.index)):
        a = (df3atr[df3atr.columns[1]] == df3atr[df3atr.columns[1]][i]) 
        if int(k)>len(df3atr.loc[a]):
            df3a = df3atr.loc[a]
            for i in df3a['ID']:
                alist.append(i)
    aclear = set(alist)
    print(aclear)
    print(len(aclear))
    for i in aclear:
        df3atr = df3atr.drop(df3atr[(df3atr['ID'] == i)].index)
    print(df3atr)
    df3atr.to_csv('step3Ak_training.csv', index = 0 , header = 1)
def bk1():
    df3btr = pd.read_csv('step3B_training.csv')
    blist = list()
    for i in range(0,len(df3btr.index)):
        b = (df3btr[df3btr.columns[1]] == df3btr[df3btr.columns[1]][i]) 
        if int(k)>len(df3btr.loc[b]):
            df3b = df3btr.loc[b]
            for i in df3b['ID']:
                blist.append(i)
    bclear = set(blist)
    for i in bclear:
        df3btr = df3btr.drop(df3btr[(df3btr['ID'] == i)].index)
    df3btr.to_csv('step3Bk_training.csv', index = 0 ,header = 1)
def ak2():
    df3atr = pd.read_csv('step3A_training.csv')
    alist = list()
    for i in range(0,len(df3atr.index)):
        a = (df3atr[df3atr.columns[1]] == df3atr[df3atr.columns[1]][i]) \
            &(df3atr[df3atr.columns[2]] == df3atr[df3atr.columns[2]][i]) 
        if int(k)>len(df3atr.loc[a]):
            df3a = df3atr.loc[a]
            for i in df3a['ID']:
                alist.append(i)
    aclear = set(alist)
    print(aclear)
    print(len(aclear))
    for i in aclear:
        df3atr = df3atr.drop(df3atr[(df3atr['ID'] == i)].index)
    print(df3atr)
    df3atr.to_csv('step3Ak_training.csv', index = 0 , header = 1)
def bk2():
    df3btr = pd.read_csv('step3B_training.csv')
    blist = list()
    for i in range(0,len(df3btr.index)):
        b = (df3btr[df3btr.columns[1]] == df3btr[df3btr.columns[1]][i]) \
            &(df3btr[df3btr.columns[2]] == df3btr[df3btr.columns[2]][i]) 
        if int(k)>len(df3btr.loc[b]):
            df3b = df3btr.loc[b]
            for i in df3b['ID']:
                blist.append(i)
    bclear = set(blist)
    for i in bclear:
        df3btr = df3btr.drop(df3btr[(df3btr['ID'] == i)].index)
    df3btr.to_csv('step3Bk_training.csv', index = 0 ,header = 1)
def ak3():
    df3atr = pd.read_csv('step3A_training.csv')
    alist = list()
    for i in range(0,len(df3atr.index)):
        a = (df3atr[df3atr.columns[1]] == df3atr[df3atr.columns[1]][i]) \
            &(df3atr[df3atr.columns[2]] == df3atr[df3atr.columns[2]][i]) \
            &(df3atr[df3atr.columns[3]] == df3atr[df3atr.columns[3]][i]) 
        if int(k)>len(df3atr.loc[a]):
            df3a = df3atr.loc[a]
            for i in df3a['ID']:
                alist.append(i)
    aclear = set(alist)
    print(aclear)
    print(len(aclear))
    for i in aclear:
        df3atr = df3atr.drop(df3atr[(df3atr['ID'] == i)].index)
    print(df3atr)
    df3atr.to_csv('step3Ak_training.csv', index = 0 , header = 1)
def bk3():
    df3btr = pd.read_csv('step3B_training.csv')
    blist = list()
    for i in range(0,len(df3btr.index)):
        b = (df3btr[df3btr.columns[1]] == df3btr[df3btr.columns[1]][i]) \
            &(df3btr[df3btr.columns[2]] == df3btr[df3btr.columns[2]][i]) \
            &(df3btr[df3btr.columns[3]] == df3btr[df3btr.columns[3]][i])
        if int(k)>len(df3btr.loc[b]):
            df3b = df3btr.loc[b]
            for i in df3b['ID']:
                blist.append(i)
    bclear = set(blist)
    for i in bclear:
        df3btr = df3btr.drop(df3btr[(df3btr['ID'] == i)].index)
    df3btr.to_csv('step3Bk_training.csv', index = 0 ,header = 1)
def ak4():
    df3atr = pd.read_csv('step3A_training.csv')
    alist = list()
    for i in range(0,len(df3atr.index)):
        a = (df3atr[df3atr.columns[1]] == df3atr[df3atr.columns[1]][i]) \
            &(df3atr[df3atr.columns[2]] == df3atr[df3atr.columns[2]][i]) \
            &(df3atr[df3atr.columns[3]] == df3atr[df3atr.columns[3]][i]) \
            &(df3atr[df3atr.columns[4]] == df3atr[df3atr.columns[4]][i]) 
        if int(k)>len(df3atr.loc[a]):
            df3a = df3atr.loc[a]
            for i in df3a['ID']:
                alist.append(i)
    aclear = set(alist)
    print(aclear)
    print(len(aclear))
    for i in aclear:
        df3atr = df3atr.drop(df3atr[(df3atr['ID'] == i)].index)
    print(df3atr)
    df3atr.to_csv('step3Ak_training.csv', index = 0 , header = 1)
def bk4():
    df3btr = pd.read_csv('step3B_training.csv')
    blist = list()
    for i in range(0,len(df3btr.index)):
        b = (df3btr[df3btr.columns[1]] == df3btr[df3btr.columns[1]][i]) \
            &(df3btr[df3btr.columns[2]] == df3btr[df3btr.columns[2]][i]) \
            &(df3btr[df3btr.columns[3]] == df3btr[df3btr.columns[3]][i]) \
            &(df3btr[df3btr.columns[4]] == df3btr[df3btr.columns[4]][i])
        if int(k)>len(df3btr.loc[b]):
            df3b = df3btr.loc[b]
            for i in df3b['ID']:
                blist.append(i)
    bclear = set(blist)
    for i in bclear:
        df3btr = df3btr.drop(df3btr[(df3btr['ID'] == i)].index)
    df3btr.to_csv('step3Bk_training.csv', index = 0 ,header = 1)
def ak5():
    df3atr = pd.read_csv('step3A_training.csv')
    alist = list()
    for i in range(0,len(df3atr.index)):
        a = (df3atr[df3atr.columns[1]] == df3atr[df3atr.columns[1]][i]) \
            &(df3atr[df3atr.columns[2]] == df3atr[df3atr.columns[2]][i]) \
            &(df3atr[df3atr.columns[3]] == df3atr[df3atr.columns[3]][i]) \
            &(df3atr[df3atr.columns[4]] == df3atr[df3atr.columns[4]][i]) \
            &(df3atr[df3atr.columns[5]] == df3atr[df3atr.columns[5]][i]) 
        if int(k)>len(df3atr.loc[a]):
            df3a = df3atr.loc[a]
            for i in df3a['ID']:
                alist.append(i)
    aclear = set(alist)
    print(aclear)
    print(len(aclear))
    for i in aclear:
        df3atr = df3atr.drop(df3atr[(df3atr['ID'] == i)].index)
    print(df3atr)
    df3atr.to_csv('step3Ak_training.csv', index = 0 , header = 1)
def bk5():
    df3btr = pd.read_csv('step3B_training.csv')
    blist = list()
    for i in range(0,len(df3btr.index)):
        b = (df3btr[df3btr.columns[1]] == df3btr[df3btr.columns[1]][i]) \
            &(df3btr[df3btr.columns[2]] == df3btr[df3btr.columns[2]][i]) \
            &(df3btr[df3btr.columns[3]] == df3btr[df3btr.columns[3]][i]) \
            &(df3btr[df3btr.columns[4]] == df3btr[df3btr.columns[4]][i]) \
            &(df3btr[df3btr.columns[5]] == df3btr[df3btr.columns[5]][i])
        if int(k)>len(df3btr.loc[b]):
            df3b = df3btr.loc[b]
            for i in df3b['ID']:
                blist.append(i)
    bclear = set(blist)
    for i in bclear:
        df3btr = df3btr.drop(df3btr[(df3btr['ID'] == i)].index)
    df3btr.to_csv('step3Bk_training.csv', index = 0 ,header = 1)
def ak6():
    df3atr = pd.read_csv('step3A_training.csv')
    print(len(df3atr.index))
    alist = list()
    for i in range(0,len(df3atr.index)):
        a = (df3atr[df3atr.columns[1]] == df3atr[df3atr.columns[1]][i]) \
            &(df3atr[df3atr.columns[2]] == df3atr[df3atr.columns[2]][i]) \
            &(df3atr[df3atr.columns[3]] == df3atr[df3atr.columns[3]][i]) \
            &(df3atr[df3atr.columns[4]] == df3atr[df3atr.columns[4]][i]) \
            &(df3atr[df3atr.columns[5]] == df3atr[df3atr.columns[5]][i]) \
            &(df3atr[df3atr.columns[6]] == df3atr[df3atr.columns[6]][i])
        if int(k)>len(df3atr.loc[a]):
            df3a = df3atr.loc[a]
            for i in df3a['ID']:
                alist.append(i)
    aclear = set(alist)
    print(aclear)
    print(len(aclear))
    for i in aclear:
        df3atr = df3atr.drop(df3atr[(df3atr['ID'] == i)].index)
    print(df3atr)
    df3atr.to_csv('step3Ak_training.csv', index = 0 , header = 1)
def bk6():
    df3btr = pd.read_csv('step3B_training.csv')
    blist = list()
    for i in range(0,len(df3btr.index)):
        b = (df3btr[df3btr.columns[1]] == df3btr[df3btr.columns[1]][i]) \
            &(df3btr[df3btr.columns[2]] == df3btr[df3btr.columns[2]][i]) \
            &(df3btr[df3btr.columns[3]] == df3btr[df3btr.columns[3]][i]) \
            &(df3btr[df3btr.columns[4]] == df3btr[df3btr.columns[4]][i]) \
            &(df3btr[df3btr.columns[5]] == df3btr[df3btr.columns[5]][i]) \
            &(df3btr[df3btr.columns[6]] == df3btr[df3btr.columns[6]][i])
        if int(k)>len(df3btr.loc[b]):
            df3b = df3btr.loc[b]
            for i in df3b['ID']:
                blist.append(i)
    bclear = set(blist)
    for i in bclear:
        df3btr = df3btr.drop(df3btr[(df3btr['ID'] == i)].index)
    df3btr.to_csv('step3Bk_training.csv', index = 0 ,header = 1)
def ak7():
    df3atr = pd.read_csv('step3A_training.csv')
    alist = list()
    for i in range(0,len(df3atr.index)):
        a = (df3atr[df3atr.columns[1]] == df3atr[df3atr.columns[1]][i]) \
            &(df3atr[df3atr.columns[2]] == df3atr[df3atr.columns[2]][i]) \
            &(df3atr[df3atr.columns[3]] == df3atr[df3atr.columns[3]][i]) \
            &(df3atr[df3atr.columns[4]] == df3atr[df3atr.columns[4]][i]) \
            &(df3atr[df3atr.columns[5]] == df3atr[df3atr.columns[5]][i]) \
            &(df3atr[df3atr.columns[6]] == df3atr[df3atr.columns[6]][i]) \
            &(df3atr[df3atr.columns[7]] == df3atr[df3atr.columns[7]][i])
        if int(k)>len(df3atr.loc[a]):
            df3a = df3atr.loc[a]
            for i in df3a['ID']:
                alist.append(i)
    aclear = set(alist)
    print(aclear)
    print(len(aclear))
    for i in aclear:
        df3atr = df3atr.drop(df3atr[(df3atr['ID'] == i)].index)
    print(df3atr)
    df3atr.to_csv('step3Ak_training.csv', index = 0 , header = 1)
def bk7():
    df3btr = pd.read_csv('step3B_training.csv')
    print(len(df3btr.index))
    blist = list()
    for i in range(0,len(df3btr.index)):
        b = (df3btr[df3btr.columns[1]] == df3btr[df3btr.columns[1]][i]) \
            &(df3btr[df3btr.columns[2]] == df3btr[df3btr.columns[2]][i]) \
            &(df3btr[df3btr.columns[3]] == df3btr[df3btr.columns[3]][i]) \
            &(df3btr[df3btr.columns[4]] == df3btr[df3btr.columns[4]][i]) \
            &(df3btr[df3btr.columns[5]] == df3btr[df3btr.columns[5]][i]) \
            &(df3btr[df3btr.columns[6]] == df3btr[df3btr.columns[6]][i]) \
            &(df3btr[df3btr.columns[7]] == df3btr[df3btr.columns[7]][i])
        if int(k)>len(df3btr.loc[b]):
            df3b = df3btr.loc[b]
            for i in df3b['ID']:
                blist.append(i)
    bclear = set(blist)
    print(bclear)
    print(len(bclear))
    for i in bclear:
        df3btr = df3btr.drop(df3btr[(df3btr['ID'] == i)].index)
    print(df3btr)
    df3btr.to_csv('step3Bk_training.csv', index = 0 ,header = 1)
def ak8():
    df3atr = pd.read_csv('step3A_training.csv')
    alist = list()
    for i in range(0,len(df3atr.index)):
        a = (df3atr[df3atr.columns[1]] == df3atr[df3atr.columns[1]][i]) \
            &(df3atr[df3atr.columns[2]] == df3atr[df3atr.columns[2]][i]) \
            &(df3atr[df3atr.columns[3]] == df3atr[df3atr.columns[3]][i]) \
            &(df3atr[df3atr.columns[4]] == df3atr[df3atr.columns[4]][i]) \
            &(df3atr[df3atr.columns[5]] == df3atr[df3atr.columns[5]][i]) \
            &(df3atr[df3atr.columns[6]] == df3atr[df3atr.columns[6]][i]) \
            &(df3atr[df3atr.columns[7]] == df3atr[df3atr.columns[7]][i]) \
            &(df3atr[df3atr.columns[8]] == df3atr[df3atr.columns[8]][i])
        if int(k)>len(df3atr.loc[a]):
            df3a = df3atr.loc[a]
            for i in df3a['ID']:
                alist.append(i)
    aclear = set(alist)
    print(aclear)
    print(len(aclear))
    for i in aclear:
        df3atr = df3atr.drop(df3atr[(df3atr['ID'] == i)].index)
    print(df3atr)
    df3atr.to_csv('step3Ak_training.csv', index = 0 , header = 1)
def bk8():
    df3btr = pd.read_csv('step3B_training.csv')
    blist = list()
    for i in range(0,len(df3btr.index)):
        b = (df3btr[df3btr.columns[1]] == df3btr[df3btr.columns[1]][i]) \
            &(df3btr[df3btr.columns[2]] == df3btr[df3btr.columns[2]][i]) \
            &(df3btr[df3btr.columns[3]] == df3btr[df3btr.columns[3]][i]) \
            &(df3btr[df3btr.columns[4]] == df3btr[df3btr.columns[4]][i]) \
            &(df3btr[df3btr.columns[5]] == df3btr[df3btr.columns[5]][i]) \
            &(df3btr[df3btr.columns[6]] == df3btr[df3btr.columns[6]][i]) \
            &(df3btr[df3btr.columns[7]] == df3btr[df3btr.columns[7]][i]) \
            &(df3btr[df3btr.columns[8]] == df3btr[df3btr.columns[8]][i])
        if int(k)>len(df3btr.loc[b]):
            df3b = df3btr.loc[b]
            for i in df3b['ID']:
                blist.append(i)
    bclear = set(blist)
    for i in bclear:
        df3btr = df3btr.drop(df3btr[(df3btr['ID'] == i)].index)
    df3btr.to_csv('step3Bk_training.csv', index = 0 ,header = 1)
def ak9():
    df3atr = pd.read_csv('step3A_training.csv')
    alist = list()
    for i in range(0,len(df3atr.index)):
        a = (df3atr[df3atr.columns[1]] == df3atr[df3atr.columns[1]][i]) \
            &(df3atr[df3atr.columns[2]] == df3atr[df3atr.columns[2]][i]) \
            &(df3atr[df3atr.columns[3]] == df3atr[df3atr.columns[3]][i]) \
            &(df3atr[df3atr.columns[4]] == df3atr[df3atr.columns[4]][i]) \
            &(df3atr[df3atr.columns[5]] == df3atr[df3atr.columns[5]][i]) \
            &(df3atr[df3atr.columns[6]] == df3atr[df3atr.columns[6]][i]) \
            &(df3atr[df3atr.columns[7]] == df3atr[df3atr.columns[7]][i]) \
            &(df3atr[df3atr.columns[8]] == df3atr[df3atr.columns[8]][i]) \
            &(df3atr[df3atr.columns[9]] == df3atr[df3atr.columns[9]][i]) 
        if int(k)>len(df3atr.loc[a]):
            df3a = df3atr.loc[a]
            for i in df3a['ID']:
                alist.append(i)
    aclear = set(alist)
    print(aclear)
    print(len(aclear))
    for i in aclear:
        df3atr = df3atr.drop(df3atr[(df3atr['ID'] == i)].index)
    print(df3atr)
    df3atr.to_csv('step3Ak_training.csv', index = 0 , header = 1)
def bk9():
    df3btr = pd.read_csv('step3B_training.csv')
    blist = list()
    for i in range(0,len(df3btr.index)):
        b = (df3btr[df3btr.columns[1]] == df3btr[df3btr.columns[1]][i]) \
            &(df3btr[df3btr.columns[2]] == df3btr[df3btr.columns[2]][i]) \
            &(df3btr[df3btr.columns[3]] == df3btr[df3btr.columns[3]][i]) \
            &(df3btr[df3btr.columns[4]] == df3btr[df3btr.columns[4]][i]) \
            &(df3btr[df3btr.columns[5]] == df3btr[df3btr.columns[5]][i]) \
            &(df3btr[df3btr.columns[6]] == df3btr[df3btr.columns[6]][i]) \
            &(df3btr[df3btr.columns[7]] == df3btr[df3btr.columns[7]][i]) \
            &(df3btr[df3btr.columns[8]] == df3btr[df3btr.columns[8]][i]) \
            &(df3btr[df3btr.columns[9]] == df3btr[df3btr.columns[9]][i])
        if int(k)>len(df3btr.loc[b]):
            df3b = df3btr.loc[b]
            for i in df3b['ID']:
                blist.append(i)
    bclear = set(blist)
    for i in bclear:
        df3btr = df3btr.drop(df3btr[(df3btr['ID'] == i)].index)
    df3btr.to_csv('step3Bk_training.csv', index = 0 ,header = 1)
def ak10():
    df3atr = pd.read_csv('step3A_training.csv')
    alist = list()
    for i in range(0,len(df3atr.index)):
        a = (df3atr[df3atr.columns[1]] == df3atr[df3atr.columns[1]][i]) \
            &(df3atr[df3atr.columns[2]] == df3atr[df3atr.columns[2]][i]) \
            &(df3atr[df3atr.columns[3]] == df3atr[df3atr.columns[3]][i]) \
            &(df3atr[df3atr.columns[4]] == df3atr[df3atr.columns[4]][i]) \
            &(df3atr[df3atr.columns[5]] == df3atr[df3atr.columns[5]][i]) \
            &(df3atr[df3atr.columns[6]] == df3atr[df3atr.columns[6]][i]) \
            &(df3atr[df3atr.columns[7]] == df3atr[df3atr.columns[7]][i]) \
            &(df3atr[df3atr.columns[8]] == df3atr[df3atr.columns[8]][i]) \
            &(df3atr[df3atr.columns[9]] == df3atr[df3atr.columns[9]][i]) \
            &(df3atr[df3atr.columns[10]] == df3atr[df3atr.columns[10]][i]) 
        if int(k)>len(df3atr.loc[a]):
            df3a = df3atr.loc[a]
            for i in df3a['ID']:
                alist.append(i)
    aclear = set(alist)
    print(aclear)
    print(len(aclear))
    for i in aclear:
        df3atr = df3atr.drop(df3atr[(df3atr['ID'] == i)].index)
    print(df3atr)
    df3atr.to_csv('step3Ak_training.csv', index = 0 , header = 1)
def bk10():
    df3btr = pd.read_csv('step3B_training.csv')
    blist = list()
    for i in range(0,len(df3btr.index)):
        b = (df3btr[df3btr.columns[1]] == df3btr[df3btr.columns[1]][i]) \
            &(df3btr[df3btr.columns[2]] == df3btr[df3btr.columns[2]][i]) \
            &(df3btr[df3btr.columns[3]] == df3btr[df3btr.columns[3]][i]) \
            &(df3btr[df3btr.columns[4]] == df3btr[df3btr.columns[4]][i]) \
            &(df3btr[df3btr.columns[5]] == df3btr[df3btr.columns[5]][i]) \
            &(df3btr[df3btr.columns[6]] == df3btr[df3btr.columns[6]][i]) \
            &(df3btr[df3btr.columns[7]] == df3btr[df3btr.columns[7]][i]) \
            &(df3btr[df3btr.columns[8]] == df3btr[df3btr.columns[8]][i]) \
            &(df3btr[df3btr.columns[9]] == df3btr[df3btr.columns[9]][i]) \
            &(df3btr[df3btr.columns[10]] == df3btr[df3btr.columns[10]][i])
        if int(k)>len(df3btr.loc[b]):
            df3b = df3btr.loc[b]
            for i in df3b['ID']:
                blist.append(i)
    bclear = set(blist)
    for i in bclear:
        df3btr = df3btr.drop(df3btr[(df3btr['ID'] == i)].index)
    df3btr.to_csv('step3Bk_training.csv', index = 0 ,header = 1)
def ak11():
    df3atr = pd.read_csv('step3A_training.csv')
    alist = list()
    for i in range(0,len(df3atr.index)):
        a = (df3atr[df3atr.columns[1]] == df3atr[df3atr.columns[1]][i]) \
            &(df3atr[df3atr.columns[2]] == df3atr[df3atr.columns[2]][i]) \
            &(df3atr[df3atr.columns[3]] == df3atr[df3atr.columns[3]][i]) \
            &(df3atr[df3atr.columns[4]] == df3atr[df3atr.columns[4]][i]) \
            &(df3atr[df3atr.columns[5]] == df3atr[df3atr.columns[5]][i]) \
            &(df3atr[df3atr.columns[6]] == df3atr[df3atr.columns[6]][i]) \
            &(df3atr[df3atr.columns[7]] == df3atr[df3atr.columns[7]][i]) \
            &(df3atr[df3atr.columns[8]] == df3atr[df3atr.columns[8]][i]) \
            &(df3atr[df3atr.columns[9]] == df3atr[df3atr.columns[9]][i]) \
            &(df3atr[df3atr.columns[10]] == df3atr[df3atr.columns[10]][i]) \
            &(df3atr[df3atr.columns[11]] == df3atr[df3atr.columns[11]][i]) 
        if int(k)>len(df3atr.loc[a]):
            df3a = df3atr.loc[a]
            for i in df3a['ID']:
                alist.append(i)
    aclear = set(alist)
    print(aclear)
    print(len(aclear))
    for i in aclear:
        df3atr = df3atr.drop(df3atr[(df3atr['ID'] == i)].index)
    print(df3atr)
    df3atr.to_csv('step3Ak_training.csv', index = 0 , header = 1)
def bk11():
    df3btr = pd.read_csv('step3B_training.csv')
    blist = list()
    for i in range(0,len(df3btr.index)):
        b = (df3btr[df3btr.columns[1]] == df3btr[df3btr.columns[1]][i]) \
            &(df3btr[df3btr.columns[2]] == df3btr[df3btr.columns[2]][i]) \
            &(df3btr[df3btr.columns[3]] == df3btr[df3btr.columns[3]][i]) \
            &(df3btr[df3btr.columns[4]] == df3btr[df3btr.columns[4]][i]) \
            &(df3btr[df3btr.columns[5]] == df3btr[df3btr.columns[5]][i]) \
            &(df3btr[df3btr.columns[6]] == df3btr[df3btr.columns[6]][i]) \
            &(df3btr[df3btr.columns[7]] == df3btr[df3btr.columns[7]][i]) \
            &(df3btr[df3btr.columns[8]] == df3btr[df3btr.columns[8]][i]) \
            &(df3btr[df3btr.columns[9]] == df3btr[df3btr.columns[9]][i]) \
            &(df3btr[df3btr.columns[10]] == df3btr[df3btr.columns[10]][i]) \
            &(df3btr[df3btr.columns[11]] == df3btr[df3btr.columns[11]][i])
        if int(k)>len(df3btr.loc[b]):
            df3b = df3btr.loc[b]
            for i in df3b['ID']:
                blist.append(i)
    bclear = set(blist)
    for i in bclear:
        df3btr = df3btr.drop(df3btr[(df3btr['ID'] == i)].index)
    df3btr.to_csv('step3Bk_training.csv', index = 0 ,header = 1)
def ak12():
    df3atr = pd.read_csv('step3A_training.csv')
    alist = list()
    for i in range(0,len(df3atr.index)):
        a = (df3atr[df3atr.columns[1]] == df3atr[df3atr.columns[1]][i]) \
            &(df3atr[df3atr.columns[2]] == df3atr[df3atr.columns[2]][i]) \
            &(df3atr[df3atr.columns[3]] == df3atr[df3atr.columns[3]][i]) \
            &(df3atr[df3atr.columns[4]] == df3atr[df3atr.columns[4]][i]) \
            &(df3atr[df3atr.columns[5]] == df3atr[df3atr.columns[5]][i]) \
            &(df3atr[df3atr.columns[6]] == df3atr[df3atr.columns[6]][i]) \
            &(df3atr[df3atr.columns[7]] == df3atr[df3atr.columns[7]][i]) \
            &(df3atr[df3atr.columns[8]] == df3atr[df3atr.columns[8]][i]) \
            &(df3atr[df3atr.columns[9]] == df3atr[df3atr.columns[9]][i]) \
            &(df3atr[df3atr.columns[10]] == df3atr[df3atr.columns[10]][i]) \
            &(df3atr[df3atr.columns[11]] == df3atr[df3atr.columns[11]][i]) \
            &(df3atr[df3atr.columns[12]] == df3atr[df3atr.columns[12]][i]) 
        if int(k)>len(df3atr.loc[a]):
            df3a = df3atr.loc[a]
            for i in df3a['ID']:
                alist.append(i)
    aclear = set(alist)
    print(aclear)
    print(len(aclear))
    for i in aclear:
        df3atr = df3atr.drop(df3atr[(df3atr['ID'] == i)].index)
    print(df3atr)
    df3atr.to_csv('step3Ak_training.csv', index = 0 , header = 1)
def bk12():
    df3btr = pd.read_csv('step3B_training.csv')
    blist = list()
    for i in range(0,len(df3btr.index)):
        b = (df3btr[df3btr.columns[1]] == df3btr[df3btr.columns[1]][i]) \
            &(df3btr[df3btr.columns[2]] == df3btr[df3btr.columns[2]][i]) \
            &(df3btr[df3btr.columns[3]] == df3btr[df3btr.columns[3]][i]) \
            &(df3btr[df3btr.columns[4]] == df3btr[df3btr.columns[4]][i]) \
            &(df3btr[df3btr.columns[5]] == df3btr[df3btr.columns[5]][i]) \
            &(df3btr[df3btr.columns[6]] == df3btr[df3btr.columns[6]][i]) \
            &(df3btr[df3btr.columns[7]] == df3btr[df3btr.columns[7]][i]) \
            &(df3btr[df3btr.columns[8]] == df3btr[df3btr.columns[8]][i]) \
            &(df3btr[df3btr.columns[9]] == df3btr[df3btr.columns[9]][i]) \
            &(df3btr[df3btr.columns[10]] == df3btr[df3btr.columns[10]][i]) \
            &(df3btr[df3btr.columns[11]] == df3btr[df3btr.columns[11]][i]) \
            &(df3btr[df3btr.columns[12]] == df3btr[df3btr.columns[12]][i])
        if int(k)>len(df3btr.loc[b]):
            df3b = df3btr.loc[b]
            for i in df3b['ID']:
                blist.append(i)
    bclear = set(blist)
    for i in bclear:
        df3btr = df3btr.drop(df3btr[(df3btr['ID'] == i)].index)
    df3btr.to_csv('step3Bk_training.csv', index = 0 ,header = 1)
def step3_k():
    df3atr = pd.read_csv('step3A_training.csv')
    df3btr = pd.read_csv('step3B_training.csv')
    if len(df3atr.columns) - 1 ==1:
        ak1()
    if len(df3atr.columns) - 1 ==2:
        ak2()
    if len(df3atr.columns) - 1 ==3:
        ak3()
    if len(df3atr.columns) - 1 ==4:
        ak4()
    if len(df3atr.columns) - 1 ==5:
        ak5()
    if len(df3atr.columns) - 1 ==6:
        ak6()
    if len(df3atr.columns) - 1 ==7:
        ak7()
    if len(df3atr.columns) - 1 ==8:
        ak8()
    if len(df3atr.columns) - 1 ==9:
        ak9()
    if len(df3atr.columns) - 1 ==10:
        ak10()
    if len(df3atr.columns) - 1 ==11:
        ak11()
    if len(df3atr.columns) - 1 ==12:
        ak12()
    if len(df3btr.columns) - 1 ==1:
        bk1()
    if len(df3btr.columns) - 1 ==2:
        bk2()
    if len(df3btr.columns) - 1 ==3:
        bk3()
    if len(df3btr.columns) - 1 ==4:
        bk4()
    if len(df3btr.columns) - 1 ==5:
        bk5()
    if len(df3btr.columns) - 1 ==6:
        bk6()
    if len(df3btr.columns) - 1 ==7:
        bk7()
    if len(df3btr.columns) - 1 ==8:
        bk8()
    if len(df3btr.columns) - 1 ==9:
        bk9()
    if len(df3btr.columns) - 1 ==10:
        bk10()
    if len(df3btr.columns) - 1 ==11:
        bk11()
    if len(df3btr.columns) - 1 ==12:
        bk12()
def step4():
    df3aktr = pd.read_csv('step3Ak_training.csv')
    df3bktr = pd.read_csv('step3Bk_training.csv')
    merged_df = pd.merge(df3aktr,df3bktr)
    print(merged_df)
    merged_df.to_csv('step4_training.csv',index = 0, header = 1)
def step5():
    df2atr_original = pd.read_csv('step2A_training.csv')
    df2btr_original = pd.read_csv('step2B_training.csv')
    df2ate_original = pd.read_csv('step2A_testing.csv')
    df2bte_original = pd.read_csv('step2B_testing.csv')
    df4tr = pd.read_csv('step4_training.csv')
    df2ate_list_original = df2ate_original.iloc[:,1:len(df2ate_original.columns)].values.tolist()
    df2bte_list_original = df2bte_original.iloc[:,1:len(df2bte_original.columns)].values.tolist()
    df2atr_original_list = df2atr_original.iloc[:,1:len(df2atr_original.columns)].values.tolist()
    df2btr_original_list = df2btr_original.iloc[:,1:len(df2btr_original.columns)].values.tolist()
    df4atr_list = df4tr.iloc[:,1:int (number) +1].values.tolist()
    df4btr_list = df4tr.iloc[:,int (number) +1:len(df4tr.columns)].values.tolist()
    df4ate_list = df2ate_original.iloc[:,1:len(df2ate_original.columns)].values.tolist()
    df4bte_list = df2bte_original.iloc[:,1:len(df2bte_original.columns)].values.tolist()
    '''training A Data'''
    df5atr_SVM_original = pd.DataFrame()
    df5atr_SVM_original['ID'] = df2atr_original.iloc[:,0]
    df5atr_SVM = pd.DataFrame()
    df5atr_SVM['ID'] = df4tr.iloc[:,0]
    df5atr_Random_original = pd.DataFrame()
    df5atr_Random_original['ID'] = df2atr_original.iloc[:,0]
    df5atr_Random = pd.DataFrame()
    df5atr_Random['ID'] = df4tr.iloc[:,0]
    df5atr_NN_original = pd.DataFrame()
    df5atr_NN_original['ID'] = df2atr_original.iloc[:,0]
    df5atr_nnet = pd.DataFrame()
    df5atr_nnet['ID'] = df4tr.iloc[:,0]
    '''testing A Data'''
    df5ate_SVM_original = pd.DataFrame()
    df5ate_SVM_original['ID'] = df2ate_original.iloc[:,0]
    df5ate_SVM = pd.DataFrame()
    df5ate_SVM['ID'] = df2ate_original.iloc[:,0]
    df5ate_Random_original = pd.DataFrame()
    df5ate_Random_original['ID'] = df2ate_original.iloc[:,0]
    df5ate_Random = pd.DataFrame()
    df5ate_Random['ID'] = df2ate_original.iloc[:,0]
    df5ate_NN_original = pd.DataFrame()
    df5ate_NN_original['ID'] = df2ate_original.iloc[:,0]
    df5ate_nnet = pd.DataFrame()
    df5ate_nnet['ID'] = df2ate_original.iloc[:,0]
    '''training B Data'''
    df5btr_SVM_original = pd.DataFrame()
    df5btr_SVM_original['ID'] = df2btr_original.iloc[:,0]
    df5btr_SVM = pd.DataFrame()
    df5btr_SVM['ID'] = df4tr.iloc[:,0]
    df5btr_Random_original = pd.DataFrame()
    df5btr_Random_original['ID'] = df2btr_original.iloc[:,0]
    df5btr_Random = pd.DataFrame()
    df5btr_Random['ID'] = df4tr.iloc[:,0]
    df5btr_NN_original = pd.DataFrame()
    df5btr_NN_original['ID'] = df2btr_original.iloc[:,0]
    df5btr_nnet = pd.DataFrame()
    df5btr_nnet['ID'] = df4tr.iloc[:,0]
    '''testing B Data'''
    df5bte_SVM_original = pd.DataFrame()
    df5bte_SVM_original['ID'] = df2bte_original.iloc[:,0]
    df5bte_SVM = pd.DataFrame()
    df5bte_SVM['ID'] = df2bte_original.iloc[:,0]
    df5bte_Random_original = pd.DataFrame()
    df5bte_Random_original['ID'] = df2bte_original.iloc[:,0]
    df5bte_Random = pd.DataFrame()
    df5bte_Random['ID'] = df2bte_original.iloc[:,0]
    df5bte_NN_original = pd.DataFrame()
    df5bte_NN_original['ID'] = df2bte_original.iloc[:,0]
    df5bte_nnet = pd.DataFrame()
    df5bte_nnet['ID'] = df2bte_original.iloc[:,0]
    '''original A Data'''
    for i in range(1,len(df2btr_original.columns)):
        '''original的SVM'''
        data_list_bsun_original = df2btr_original.iloc[:,i].values.tolist()
        X = df2atr_original_list
        Y = np.array(data_list_bsun_original).astype('int')
        SVM_model = SVC()
        SVM_model.fit(X,Y)
        y_pred = SVM_model.predict(X)
        df5atr_SVM_original['b'+str(i)] = y_pred
        y_pred = SVM_model.predict(df2ate_list_original)
        df5ate_SVM_original['b'+str(i)] = y_pred
        '''original的Randomforset'''
        rf_model = ensemble.RandomForestRegressor()
        X = df2atr_original_list
        Y = np.array(data_list_bsun_original)
        rf_model.fit(X,Y)
        y_pred = rf_model.predict(X)
        df5atr_Random_original['b'+str(i)] = y_pred
        y_pred = rf_model.predict(df2ate_list_original)
        df5ate_Random_original['b'+str(i)] = y_pred
        '''original的NN'''
        NN_model = MLPClassifier()
        X = df2atr_original_list
        Y = np.array(data_list_bsun_original).astype('int')
        NN_model.fit(X,Y)
        y_pred = NN_model.predict(X)
        df5atr_NN_original['b'+str(i)] = y_pred
        y_pred = NN_model.predict(df2ate_list_original)
        df5ate_NN_original['b'+str(i)] = y_pred
    df5atr_SVM_original.to_csv('step5A_training_SVM_original.csv',index = 0 , header = 1)
    df5ate_SVM_original.to_csv('step5A_testing_SVM_original.csv', index = 0 , header = 1)
    df5atr_Random_original.to_csv('step5A_training_Random_original.csv', index = 0 , header = 1)
    df5ate_Random_original.to_csv('step5A_testing_Random_original.csv', index = 0 , header = 1)
    df5atr_NN_original.to_csv('step5A_training_NN_original.csv', index = 0 , header = 1)
    df5ate_NN_original.to_csv('step5A_testing_NN_original.csv', index = 0 , header = 1)
    '''original B Data'''
    for j in range(1,len(df2atr_original.columns)):
        '''original的SVM'''
        data_list_asun_original = df2atr_original.iloc[:,j].values.tolist()
        X = df2btr_original_list
        Y = data_list_asun_original
        SVM_model = SVC()
        SVM_model.fit(X,Y)
        y_pred = SVM_model.predict(X)
        df5btr_SVM_original['a'+str(j)] = y_pred
        y_pred = SVM_model.predict(df2bte_list_original)
        df5bte_SVM_original['a'+str(j)] = y_pred
        '''original的Randomforset'''
        rf_model = ensemble.RandomForestRegressor()
        rf_model.fit(X,Y)
        y_pred = rf_model.predict(X)
        df5btr_Random_original['a'+str(j)] = y_pred
        y_pred = rf_model.predict(df2bte_list_original)
        df5bte_Random_original['a'+str(j)] = y_pred
        '''original的NN'''
        NN_model = MLPClassifier()
        NN_model.fit(X,Y)
        y_pred = NN_model.predict(X)
        df5btr_NN_original['a'+str(j)] = y_pred
        y_pred = NN_model.predict(df2bte_list_original)
        df5bte_NN_original['a'+str(j)] = y_pred
    df5btr_SVM_original.to_csv('step5B_training_SVM_original.csv',index = 0 , header = 1)
    df5bte_SVM_original.to_csv('step5B_testing_SVM_original.csv', index = 0 , header = 1)
    df5btr_Random_original.to_csv('step5B_training_Random_original.csv', index = 0 , header = 1)
    df5bte_Random_original.to_csv('step5B_testing_Random_original.csv', index = 0 , header = 1)
    df5btr_NN_original.to_csv('step5B_training_NN_original.csv', index = 0 , header = 1)
    df5bte_NN_original.to_csv('step5B_testing_NN_original.csv', index = 0 , header = 1)
    
    coun = 1
    for k in range(int (number)+1,len(df4tr.columns)):
        '''SVM'''
        data_list_bsun = df4tr.iloc[:,k].values.tolist()
        X = df4atr_list
        Y = data_list_bsun
        SVM_model = SVC()
        print(X)
        print(Y)
        SVM_model.fit(X, Y)
        y_pred = SVM_model.predict(X)
        df5atr_SVM['b'+str(coun)] = y_pred
        y_pred = SVM_model.predict(df4ate_list)
        df5ate_SVM['b'+str(coun)] = y_pred
        '''Random'''
        rf_model = ensemble.RandomForestRegressor()
        rf_model.fit(X,Y)
        y_pred = rf_model.predict(X)
        df5atr_Random['b'+str(coun)] = y_pred
        y_pred = rf_model.predict(df4ate_list)
        df5ate_Random['b'+str(coun)] = y_pred
        '''NN'''
        NN_model = MLPClassifier()
        NN_model.fit(X,Y)
        y_pred = NN_model.predict(X)
        df5atr_nnet['b'+str(coun)] = y_pred
        y_pred = NN_model.predict(df4ate_list)
        df5ate_nnet['b'+str(coun)] = y_pred
        
        coun+=1
        
    df5atr_SVM.to_csv('step5A_training_SVM.csv',index = 0, header = 1)
    df5ate_SVM.to_csv('step5A_testing_SVM.csv' ,index = 0, header = 1)
    df5atr_Random.to_csv('step5A_training_Random.csv',index = 0, header = 1)
    df5ate_Random.to_csv('step5A_testing_Random.csv' ,index = 0, header = 1)
    df5atr_nnet.to_csv('step5A_training_nnet.csv',index = 0, header = 1)
    df5ate_nnet.to_csv('step5A_testing_nnet.csv' ,index = 0, header = 1)
    
    for l in range(1, int (number)+1):
        '''SVM'''
        data_list_asun = df4tr.iloc[:,l].values.tolist()
        X = df4btr_list
        Y = data_list_asun
        SVM_model = SVC()
        SVM_model.fit(X,Y)
        y_pred = SVM_model.predict(X)
        df5btr_SVM['a'+str(l)] = y_pred
        y_pred = SVM_model.predict(df4bte_list)
        df5bte_SVM['a'+str(l)] = y_pred
        '''Random'''
        rf_model = ensemble.RandomForestRegressor()
        rf_model.fit(X,Y)
        y_pred = rf_model.predict(X)
        df5btr_Random['a'+str(j)] = y_pred
        y_pred = rf_model.predict(df4bte_list)
        df5bte_Random['a'+str(j)] = y_pred
        '''NN'''
        NN_model = MLPClassifier()
        NN_model.fit(X,Y)
        y_pred = NN_model.predict(X)
        df5btr_nnet['a'+str(j)] = y_pred
        y_pred = NN_model.predict(df4bte_list)
        df5bte_nnet['a'+str(j)] = y_pred
        
    df5btr_SVM.to_csv('step5B_training_SVM.csv',index = 0,header = 1)
    df5bte_SVM.to_csv('step5B_testing_SVM.csv', index = 0 , header = 1)
    df5btr_Random.to_csv('step5B_training_Random.csv',index = 0, header = 1)
    df5bte_Random.to_csv('step5B_testing_Random.csv' ,index = 0, header = 1)
    df5btr_nnet.to_csv('step5B_training_nnet.csv',index = 0, header = 1)
    df5bte_nnet.to_csv('step5B_testing_nnet.csv' ,index = 0, header = 1)
def step6():
    '''training A data 加入原始資料'''
    df2atr_original = pd.read_csv('step2A_training.csv')
    df5atr_SVM_original = pd.read_csv('step5A_training_SVM_original.csv')
    df5atr_SVM = pd.read_csv('step5A_training_SVM.csv')
    df5atr_Random_original = pd.read_csv('step5A_training_Random_original.csv')
    df5atr_Random = pd.read_csv('step5A_training_Random.csv')
    df5atr_NN_original = pd.read_csv('step5A_training_NN_original.csv')
    df5atr_nnet = pd.read_csv('step5A_training_nnet.csv')
    merged_df6atr_SVM_original = pd.merge(df2atr_original,df5atr_SVM_original)
    merged_df6atr_SVM = pd.merge(df2atr_original,df5atr_SVM)
    merged_df6atr_Random_original = pd.merge(df2atr_original,df5atr_Random_original)
    merged_df6atr_Random = pd.merge(df2atr_original,df5atr_Random)
    merged_df6atr_NN_original = pd.merge(df2atr_original,df5atr_NN_original)
    merged_df6atr_NN = pd.merge(df2atr_original,df5atr_nnet)
    merged_df6atr_SVM_original.to_csv('step6A_training_SVM_original.csv', index = 0 , header = 1)
    merged_df6atr_SVM.to_csv('step6A_training_SVM.csv', index = 0 , header = 1)
    merged_df6atr_Random_original.to_csv('step6A_training_Random_original.csv', index = 0 , header = 1)
    merged_df6atr_Random.to_csv('step6A_training_Random.csv', index = 0 , header = 1)
    merged_df6atr_NN_original.to_csv('step6A_training_NN_original.csv' , index = 0 , header = 1)
    merged_df6atr_NN.to_csv('step6A_training_NN.csv' , index = 0 , header = 1)
    '''training B data 加入原始資料'''
    df2btr_original = pd.read_csv('step2B_training.csv')
    df5btr_SVM_original = pd.read_csv('step5B_training_SVM_original.csv')
    df5btr_SVM = pd.read_csv('step5B_training_SVM.csv')
    df5btr_Random_original = pd.read_csv('step5B_training_Random_original.csv')
    df5btr_Random = pd.read_csv('step5B_training_Random.csv')
    df5btr_NN_original = pd.read_csv('step5B_training_NN_original.csv')
    df5btr_NN = pd.read_csv('step5B_training_nnet.csv')
    merged_df6btr_SVM_original = pd.merge(df2btr_original,df5btr_SVM_original)
    merged_df6btr_SVM = pd.merge(df2btr_original,df5btr_SVM)
    merged_df6btr_Random_original = pd.merge(df2btr_original,df5btr_Random_original)
    merged_df6btr_Random = pd.merge(df2btr_original,df5btr_Random)
    merged_df6btr_NN_original = pd.merge(df2btr_original,df5btr_NN_original)
    merged_df6btr_NN = pd.merge(df2btr_original,df5btr_NN)
    merged_df6btr_SVM_original.to_csv('step6B_training_SVM_original.csv', index = 0 , header = 1)
    merged_df6btr_SVM.to_csv('step6B_training_SVM.csv', index = 0 , header = 1)
    merged_df6btr_Random_original.to_csv('step6B_training_Random_original.csv', index = 0 , header = 1)
    merged_df6btr_Random.to_csv('step6B_training_Random.csv', index = 0 , header = 1)
    merged_df6btr_NN_original.to_csv('step6B_training_NN_original.csv', index = 0 , header = 1)
    merged_df6btr_NN.to_csv('step6B_training_NN.csv', index = 0 , header = 1)
    '''testing A data 加入原始資料'''
    df2ate_original = pd.read_csv('step2A_testing.csv')
    df5ate_SVM_original = pd.read_csv('step5A_testing_SVM_original.csv')
    df5ate_SVM = pd.read_csv('step5A_testing_SVM.csv')
    df5ate_Random_original = pd.read_csv('step5A_testing_Random_original.csv')
    df5ate_Random = pd.read_csv('step5A_testing_Random.csv')
    df5ate_NN_original = pd.read_csv('step5A_testing_NN_original.csv')
    df5ate_NN = pd.read_csv('step5A_testing_nnet.csv')
    merged_df6ate_SVM_original = pd.merge(df2ate_original,df5ate_SVM_original)
    merged_df6ate_SVM = pd.merge(df2ate_original,df5ate_SVM)
    merged_df6ate_Random_original = pd.merge(df2ate_original,df5ate_Random_original)
    merged_df6ate_Random = pd.merge(df2ate_original,df5ate_Random)
    merged_df6ate_NN_original = pd.merge(df2ate_original,df5ate_NN_original)
    merged_df6ate_NN = pd.merge(df2ate_original,df5ate_NN)
    merged_df6ate_SVM_original.to_csv('step6A_testing_SVM_original.csv', index = 0 , header = 1)
    merged_df6ate_SVM.to_csv('step6A_testing_SVM.csv', index = 0 , header = 1)
    merged_df6ate_Random_original.to_csv('step6A_testing_Random_original.csv', index = 0 , header = 1)
    merged_df6ate_Random.to_csv('step6A_testing_Random.csv', index = 0 , header = 1)
    merged_df6ate_NN_original.to_csv('step6A_testing_NN_original.csv', index = 0 , header = 1)
    merged_df6ate_NN.to_csv('step6A_testing_NN.csv', index = 0 , header = 1)
    '''testing B data 加入原始資料'''
    df2bte_original = pd.read_csv('step2B_testing.csv')
    df5bte_SVM_original = pd.read_csv('step5B_testing_SVM_original.csv')
    df5bte_SVM = pd.read_csv('step5B_testing_SVM.csv')
    df5bte_Random_original = pd.read_csv('step5B_testing_Random_original.csv')
    df5bte_Random = pd.read_csv('step5B_testing_Random.csv')
    df5bte_NN_original = pd.read_csv('step5B_testing_NN_original.csv')
    df5bte_NN = pd.read_csv('step5B_testing_nnet.csv')
    merged_df6bte_SVM_original = pd.merge(df2bte_original,df5bte_SVM_original)
    merged_df6bte_SVM = pd.merge(df2bte_original,df5bte_SVM)
    merged_df6bte_Random_original = pd.merge(df2bte_original,df5bte_Random_original)
    merged_df6bte_Random = pd.merge(df2bte_original,df5bte_Random)
    merged_df6bte_NN_original = pd.merge(df2bte_original,df5bte_NN_original)
    merged_df6bte_NN = pd.merge(df2bte_original,df5bte_NN)
    merged_df6bte_SVM_original.to_csv('step6B_testing_SVM_original.csv', index = 0 , header = 1)
    merged_df6bte_SVM.to_csv('step6B_testing_SVM.csv', index = 0 , header = 1)
    merged_df6bte_Random_original.to_csv('step6B_testing_Random_original.csv', index = 0 , header = 1)
    merged_df6bte_Random.to_csv('step6B_testing_Random.csv', index = 0 , header = 1)
    merged_df6bte_NN_original.to_csv('step6B_testing_NN_original.csv', index = 0 , header = 1)
    merged_df6bte_NN.to_csv('step6B_testing_NN.csv', index = 0 , header = 1)
def step7():
    
    df1 = pd.read_csv('step1.csv')
    dft = pd.DataFrame(df1,columns=['ID','target'])
    dft.to_csv('target.csv' , index = 0 , header = 1)
    '''SVM與SVM,Random,RR的預測'''
    '''原始A的SVM-SVM'''
    df6atr_SVM_original = pd.read_csv('step6A_training_SVM_original.csv')
    df6atrt_SVM_original = pd.merge(df6atr_SVM_original,dft)
    df7atr_SVM_original = df6atrt_SVM_original.iloc[:,1:len(df6atrt_SVM_original.columns)-1].values.tolist()
    df7atrt_SVM_original = df6atrt_SVM_original.iloc[:,len(df6atrt_SVM_original.columns)-1].values.tolist()
    df6ate_SVM_original = pd.read_csv('step6A_testing_SVM_original.csv')
    df6atet_SVM_original = pd.merge(df6ate_SVM_original,dft)
    df7ate_SVM_original = df6atet_SVM_original.iloc[:,1:len(df6atet_SVM_original.columns)-1].values.tolist()
    df7atet_SVM_original = df6atet_SVM_original.iloc[:,len(df6atet_SVM_original.columns)-1].values.tolist()
    X = df7atr_SVM_original
    Y = df7atrt_SVM_original
    SVM_model = SVC()
    SVM_model.fit(X,Y)
    y_pred_SVM = SVM_model.predict(df7ate_SVM_original)
    
    X = np.array(y_pred_SVM).reshape(-1,1)
    Y = np.array(df7atet_SVM_original)
    SVM_model = SVC()
    SVM_model.fit(X,Y)
    y_pred_SVM = SVM_model.predict(X)
    print('原A-SVM_SVM精準度:'+str(accuracy_score(Y, y_pred_SVM)))
    Aoriginal = str(accuracy_score(Y, y_pred_SVM))
    '''處理過A的SVM-SVM'''
    df6atr_SVM = pd.read_csv('step6A_training_SVM.csv')
    df6atrt_SVM = pd.merge(df6atr_SVM,dft)
    df7atr_SVM = df6atrt_SVM.iloc[:,1:len(df6atrt_SVM.columns)-1].values.tolist()
    df7atrt_SVM = df6atrt_SVM.iloc[:,len(df6atrt_SVM.columns)-1].values.tolist()
    df6ate_SVM = pd.read_csv('step6A_testing_SVM.csv')
    df6atet_SVM = pd.merge(df6ate_SVM,dft)
    df7ate_SVM = df6atet_SVM.iloc[:,1:len(df6atet_SVM.columns)-1].values.tolist()
    df7atet_SVM = df6atet_SVM.iloc[:,len(df6atet_SVM.columns)-1].values.tolist()
    X = df7atr_SVM
    Y = df7atrt_SVM
    SVM_model = SVC()
    SVM_model.fit(X,Y)
    y_pred_SVM = SVM_model.predict(df7ate_SVM)
    X = np.array(y_pred_SVM).reshape(-1,1)
    Y = np.array(df7atet_SVM)
    SVM_model = SVC()
    SVM_model.fit(X,Y)
    y_pred_SVM = SVM_model.predict(X)
    print('處理過A-SVM_SVM精準度:'+str(accuracy_score(Y, y_pred_SVM)))
    A = str(accuracy_score(Y, y_pred_SVM))
    '''原始B的SVM-SVM'''
    df6btr_SVM_original = pd.read_csv('step6B_training_SVM_original.csv')
    df6btrt_SVM_original = pd.merge(df6btr_SVM_original,dft)
    df7btr_SVM_original = df6btrt_SVM_original.iloc[:,1:len(df6btrt_SVM_original.columns)-1].values.tolist()
    df7btrt_SVM_original = df6btrt_SVM_original.iloc[:,len(df6btrt_SVM_original.columns)-1].values.tolist()
    df6bte_SVM_original = pd.read_csv('step6A_testing_SVM_original.csv')
    df6btet_SVM_original = pd.merge(df6bte_SVM_original,dft)
    df7bte_SVM_original = df6btet_SVM_original.iloc[:,1:len(df6btet_SVM_original.columns)-1].values.tolist()
    df7btet_SVM_original = df6btet_SVM_original.iloc[:,len(df6btet_SVM_original.columns)-1].values.tolist()
    
    X = df7btr_SVM_original
    Y = df7btrt_SVM_original
    SVM_model = SVC()
    SVM_model.fit(X,Y)
    y_pred_SVM = SVM_model.predict(df7bte_SVM_original)
    X = np.array(y_pred_SVM).reshape(-1,1)
    Y = np.array(df7btet_SVM_original)
    SVM_model = SVC()
    SVM_model.fit(X,Y)
    y_pred_SVM = SVM_model.predict(X)
    print('原B-SVM_SVM精準度:'+str(accuracy_score(Y, y_pred_SVM))) 
    Boriginal = str(accuracy_score(Y, y_pred_SVM))
    '''處理過B的SVM-SVM'''
    df6btr_SVM = pd.read_csv('step6B_training_SVM.csv')
    df6btrt_SVM = pd.merge(df6btr_SVM,dft)
    df7btr_SVM = df6btrt_SVM.iloc[:,1:len(df6btrt_SVM.columns)-1].values.tolist()
    df7btrt_SVM = df6btrt_SVM.iloc[:,len(df6btrt_SVM.columns)-1].values.tolist()
    df6bte_SVM = pd.read_csv('step6B_testing_SVM.csv')
    df6btet_SVM = pd.merge(df6bte_SVM,dft)
    df7bte_SVM = df6btet_SVM.iloc[:,1:len(df6btet_SVM.columns)-1].values.tolist()
    df7btet_SVM = df6btet_SVM.iloc[:,len(df6btet_SVM.columns)-1].values.tolist()
    X = df7btr_SVM
    Y = df7btrt_SVM
    SVM_model = SVC()
    SVM_model.fit(X,Y)
    y_pred_SVM = SVM_model.predict(df7bte_SVM)
    X = np.array(y_pred_SVM).reshape(-1,1)
    Y = np.array(df7btet_SVM)
    SVM_model = SVC()
    SVM_model.fit(X,Y)
    y_pred_SVM = SVM_model.predict(X)
    print('處理過B-SVM_SVM精準度:'+str(accuracy_score(Y, y_pred_SVM)))
    B = str(accuracy_score(Y, y_pred_SVM))
    finish.loc[times] = [Aoriginal,A,Boriginal,B]
    print(times)
step1()   
number = input('請輸入第一筆資料要多少屬性')
finish = pd.DataFrame(columns = ['A_original','A','B_original','B'])
times = 1
number1 = input('訓練資料要佔幾%')
listab = list()
ans = input("請問是否輸入修改資料")
if ans == 'yes':
    AttributesA = input("請輸入需要修改的A屬性").split(',')
    AttributesB = input("請輸入需要修改的B屬性").split(',')
segmentation = input('要分成幾等份?')
k = input("請輸入k值")
for m in range(1,21):
    step2(number,number1)
    df2atr = pd.read_csv('step2A_training.csv')
    df2btr = pd.read_csv('step2B_training.csv')
    step3(AttributesA,AttributesB)
    step3_k()
    step4()
    step5()
    step6()
    finish.to_csv('finish.csv', index = 0 , header = 1)
    step7()
    times+=1
print(finish)