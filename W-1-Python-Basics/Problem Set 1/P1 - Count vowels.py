# Sample test case
s = 'azcbobobegghakl'

vowelCount = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowelCount+=1
print('Number of vowels: ' + str(vowelCount))
    