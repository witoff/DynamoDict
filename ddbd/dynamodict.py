# The Dictionary Subclass
import collections
class DynamoDict(collections.MutableMapping):
    """Overiding Python dict to allow for simple operations"""

    def __init__(self, table):
        self.table = table

        # Get this table's hash key name
        keys = table.describe()['Table']['KeySchema']
        self.hash_key = [k for k in keys if k['KeyType'] == 'HASH'][0]['AttributeName']

    def __getitem__(self, key):
        params = {self.hash_key: key}

        if not self.table.has_item(**params):
            raise KeyError(key)
        item = self.table.get_item(**params)

        # Convert item to dict and remove our hash_key
        d = dict(item)
        d.pop(self.hash_key)

        return d

    def __setitem__(self, key, value):

        # Make sure 'value' is a dict so each key/value will be saved to thes object
        assert isinstance(value, dict)
        print 'key: ', key, 'value: ', value

        # Don't overwrite the inserted value object
        params = value.copy()

        #add hashkey/key to these main params
        params[self.hash_key] = key

        print params
        # put_item returns false when not successful, so thrown an exception
        if not self.table.put_item(data=params, overwrite=True):
            raise Exception('item save failure')
        print 'item saved'

    def __delitem__(self, key):
        params = {self.hash_key : key}
        if not self.table.delete_item(**params):
            raise Exception('item delete failure')

    def __iter__(self):
        return DynamoKeyIter(self.table, self.hash_key)

    def __len__(self):
        #N.B. the .count() method is very eventually
        #  consistent (~6 hours).  Shouldn't be used here

        # TODO: Replace wish a query for hash_key count
        return len([k for k in iter(self)])

    def __keytransform__(self, key):
        return key

# An Iterator helper
class DynamoKeyIter(object):
    """ Create at iterator that only returns your hash keys"""
    def __init__(self, table, hash_key):
        self.hash_key = hash_key
        self.scanner = table.scan(attributes=[self.hash_key])

    def __iter__(self):
        return self
    def next(self):
        item = self.scanner.next()
        return dict(item)[self.hash_key]
