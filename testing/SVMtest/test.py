import pickle
import pandas as pd

import numpy as np

svm=pickle.load(open('svm3.pkl','rb'))
normaliser=pickle.load(open('normaliser3.pkl','rb'))


data=pd.read_excel('data.xlsx',sheetname=2)

features=data.iloc[:,:18]

#print features

norm_features=normaliser.transform(features)


alienresult=data.iloc[:,20]
earthresult=svm.predict(norm_features)

print np.array(alienresult)==earthresult

