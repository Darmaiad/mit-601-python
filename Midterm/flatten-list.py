# Write a function to flatten a list. The list contains other lists, strings, or ints.
# For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

L = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    flatList = []

    for listItem in aList:
        if type(listItem) == list:              
            flatList.extend(flatten(listItem))
        else:
            flatList.append(listItem)
    return flatList

print(flatten(L))
                

