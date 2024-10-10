import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


data = pd.read_excel('../dataset/prix-moyen-au-metre-carre-enregistre-par-commune-2014.xls', skiprows=13, index_col=0)
data.reset_index(inplace=True)
data.drop(data.columns[0], axis=1, inplace=True)
data.drop(data.columns[4:], axis=1, inplace=True)
data = data.drop(data.index[106:])
data['Annee'] = 2014

data2 = pd.read_excel('../dataset/prix-moyen-au-metre-carre-enregistre-par-commune-2015.xls', skiprows=13, index_col=0)
data2.reset_index(inplace=True)
data2.drop(data2.columns[0], axis=1, inplace=True)
data2.drop(data2.columns[4:], axis=1, inplace=True)
data2 = data2.drop(data2.index[106:])
# drop NaN values
data2 = data2.dropna()
data2['Annee'] = 2015

data3 = pd.read_excel('../dataset/prix-moyen-au-metre-carre-enregistre-par-commune-2016.xls', skiprows=13, index_col=0)
data3.reset_index(inplace=True)
data3.drop(data3.columns[0], axis=1, inplace=True)
data3.drop(data3.columns[4:], axis=1, inplace=True)
data3 = data3.drop(data3.index[106:])
# drop NaN values  
data3 = data3.dropna()
data3['Annee'] = 2016

data4 = pd.read_excel('../dataset/prix-moyen-au-metre-carre-enregistre-par-commune-2017.xls', skiprows=13, index_col=0)
data4.reset_index(inplace=True)
data4.drop(data4.columns[0], axis=1, inplace=True)
data4.drop(data4.columns[4:], axis=1, inplace=True)
data4 = data4.drop(data4.index[106:])
# drop NaN values
data4 = data4.dropna()
data4['Annee'] = 2017

data5 = pd.read_excel('../dataset/prix-moyen-au-metre-carre-enregistre-par-commune-2018.xls', skiprows=13, index_col=0)
data5.reset_index(inplace=True)
data5.drop(data5.columns[0], axis=1, inplace=True)
data5.drop(data5.columns[4:], axis=1, inplace=True)
data5 = data5.drop(data5.index[106:])
# drop NaN values
data5 = data5.dropna()
data5['Annee'] = 2018

data6 = pd.read_excel('../dataset/prix-moyen-au-metre-carre-enregistre-par-commune-2019.xls', skiprows=13, index_col=0)
data6.reset_index(inplace=True)
data6.drop(data6.columns[0], axis=1, inplace=True)
data6.drop(data6.columns[4:], axis=1, inplace=True)
data6 = data6.drop(data6.index[106:])
# drop NaN values
data6 = data6.dropna()
data6['Annee'] = 2019

data7 = pd.read_excel('../dataset/prix-moyen-au-metre-carre-enregistre-par-commune-2020.xls', skiprows=13, index_col=0)
data7.reset_index(inplace=True)
data7.drop(data7.columns[0], axis=1, inplace=True)
data7.drop(data7.columns[4:], axis=1, inplace=True)
data7 = data7.drop(data7.index[106:])
# drop NaN values
data7 = data7.dropna()
data7['Annee'] = 2020

data8 = pd.read_excel('../dataset/prix-moyen-au-metre-carre-enregistre-par-commune-2021.xls', skiprows=10, index_col=0)
data8.reset_index(inplace=True)
data8.drop(data8.columns[0], axis=1, inplace=True)
data8.drop(data8.columns[4:], axis=1, inplace=True)
data8 = data8.drop(data8.index[106:])
# drop NaN values
data8 = data8.dropna()
data8['Annee'] = 2021


data9 = pd.read_excel('../dataset/prix-moyen-au-metre-carre-enregistre-par-commune-2022.xls', skiprows=10, index_col=0)
data9.reset_index(inplace=True)
data9.drop(data9.columns[0], axis=1, inplace=True)
data9.drop(data9.columns[4:], axis=1, inplace=True)
data9 = data9.drop(data9.index[106:])
data9 = data9.dropna()
data9['Annee'] = 2022

data10 = pd.read_excel('../dataset/prix-moyen-au-metre-carre-enregistre-par-commune-2023.xls', skiprows=10, index_col=0)
data10.reset_index(inplace=True)
data10.drop(data10.columns[0], axis=1, inplace=True)
data10.drop(data10.columns[4:], axis=1, inplace=True)
data10 = data10.drop(data10.index[106:])
data10 = data10.dropna()
data10['Annee'] = 2023

dataConcat = pd.concat([data, data2, data3, data4, data5, data6, data7, data8, data9, data10])
#save as xlsx
# véfifier si le fichier concat.xlsx existe
# si oui, le supprimer
import os
if os.path.exists('../dataset/concat.xlsx'):
    os.remove('../dataset/concat.xlsx')
# enregistrer le fichier concat.xlsx
dataConcat.to_excel('../dataset/concat.xlsx', index=False)