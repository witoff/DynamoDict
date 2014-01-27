DynamoDict
==========

Use a subclass of your favorite languages' native dictionary implementation based on DynamoDB


```python
#imports.  Creds are handled automagically or a rich prompt is provided if not available.  Never in code
from ddbd import ddbd

#get the ddbd table
people = ddbd['people']

#append values
if 'rob' not in people:
  people.append('rob')

#scan over the dict
for p in people:
  print 'key: ', p
  print 'value: ', people[p]
  
#keys
p.keys()

#vals
p.values()

```
