# json
'''
import json
data = {'name':'Codenow','age':7}
print(type(data))

parsed_data = json.dumps(data)
print(parsed_data)
print(len(parsed_data))
print(type(parsed_data))
res = json.loads(parsed_data)
print(res)

sample = json.loads('[12,3,4,5]')
print(sample)
'''

# collections
'''
from collections import Counter
data = ['A','B','C','A','A','A','C']
r = Counter(data)
print(r)
print(type(r))

h = dict(Counter(data))
print(h)
print(type(h))

'''




