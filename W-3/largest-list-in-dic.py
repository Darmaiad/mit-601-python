animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    largestListSize = -1
    keyWithLargestList = ''
    for key in aDict:
        currentLen = len(aDict[key])
        if currentLen > largestListSize:
            largestListSize = currentLen
            keyWithLargestList = key
    return keyWithLargestList

print(biggest(animals))
