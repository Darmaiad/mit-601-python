# Sample test case
s = 'oboboxrboboogobobbobazbobobboboboboobobomiobobobobbbobb'

bobCount = 0
token = ''

for char in s:
    if char == 'b': 
        if token == '':
            token = char
        if token == 'bo':
            bobCount +=1
            token = 'b'
    elif char == 'o' and token == 'b':
        token = 'bo'
    else:
        token = ''
     
print('Number of times bob occurs is: ' + str(bobCount))
    