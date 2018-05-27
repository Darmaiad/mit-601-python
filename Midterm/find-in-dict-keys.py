# Write a Python function that returns a list of keys in aDict with the value target. 
# The list of keys you return should be sorted in increasing order. 
# The keys and values in aDict are both integers. 
# (If aDict does not contain the value target, you should return an empty list.)
# This function takes in a dictionary and an integer and returns a list.

sampleDict = {5: 10, 2: 20, 3: 30, 4: 20, 1:20, 8:20, 7:20 }

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    keyList = []
    for key in aDict.keys():
        if aDict[key] == target:
            keyList.append(key)

    keyList.sort()
    return keyList

print('The sorted key list is: ' + str(keysWithValue(sampleDict, 20)))  