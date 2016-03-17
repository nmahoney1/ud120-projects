#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

#print(enron_data['YEAGER F SCOTT'])

#print(sum(enron_data[x]['poi'] for x in enron_data.keys() if enron_data[x]['poi'] == True))

#print(enron_data.keys())

#print(enron_data['PRENTICE JAMES'])

#print(enron_data['PRENTICE JAMES']['total_stock_value'])

#print(enron_data['SKILLING JEFFREY K']['total_payments'])
#print(enron_data['FASTOW ANDREW S']['total_payments'])
#print(enron_data['LAY KENNETH L']['total_payments'])

#print(enron_data['SKILLING JEFFREY K']['email_address'])
"""
email = []
salary = []

salary = [enron_data[x]['salary'] for x in enron_data.keys() if enron_data[x]['salary'] != 'NaN']
print(len(salary))

email = [enron_data[x]['email_address'] for x in enron_data.keys() if enron_data[x]['email_address'] != 'NaN']
print(len(email))
"""

total_payments = []
total_payments = [enron_data[x] for x in enron_data.keys() if enron_data[x]['total_payments'] == 'NaN']
print(total_payments)
poi = []
print(len(total_payments))
print(len(enron_data))
#poi = [total_payments[x] for x in 21 if "poi': False" in total_payments[x]]
#print(len(poi))
#print(len(total_payments)/len(enron_data.keys()))