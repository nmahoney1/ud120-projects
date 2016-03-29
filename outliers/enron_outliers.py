#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
data_dict.pop('TOTAL', 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below

for x in data_dict.keys():
    outlier = []
    if data_dict[x]['salary'] != 'NaN':
        if int(data_dict[x]['salary']) > 1000000:
            outlier.append(x)
    for y in outlier:
        if data_dict[y]['bonus'] != 'NaN':    
            if int(data_dict[y]['bonus']) > 4000000:
                print(y)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()