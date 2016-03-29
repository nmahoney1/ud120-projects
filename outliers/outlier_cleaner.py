#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    # make a list of tuples
    for x in range(0, len(predictions)):
        new = ages[x], net_worths[x], abs(predictions[x] - net_worths[x])
        cleaned_data.append(new)
        
    cleaned_data.sort(key = lambda tup: tup[2])
    return cleaned_data[:81]

