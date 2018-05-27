# Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters. 
# For example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]
# This function takes in a list of strings and returns a list of strings. Your function should not modify aList.

L = ["apple", "cat", "dog", "banana"]

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    filteredList = []
    for listElement in aList:
        if len(listElement) < 4:
            filteredList.append(listElement)
    return filteredList

print('The sublist is: ' + str(lessThan4(L)))