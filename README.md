DynamoDict
==========

A simple DynamoDB ORM that maps Dynamo tables to simple, native python dictionaries.


```python
from ddbd import ddbd

dynamo = ddbd(key="AWS_KEY", secret="AWS_SECRET", region="us-east-1")

# List all existing dicts
print dynamo.list()
# ['table 1', 'table2']

# Retrieve a python dictionary backed by a dynamo table.
#  if the table does not exist, it will create and block until available
d = dynamo.get('ProfileData')

# Treat this table like a native python dict!
print len(d)

# Assign key/vals
d['rob'] = {'eye_color' : 'blue'}

# Iterate
for k in d:
  print '-', k, d[k]

# Extract all keys
print d.keys()

```
