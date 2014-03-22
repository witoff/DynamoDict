from boto import dynamodb2
from boto.dynamodb2.table import Table
from dynamodict import DynamoDict
import time

class ddbd(object):

  def __init__(self, key=None, secret=None, region=None):
    self.conn = dynamodb2.connect_to_region(region, aws_access_key_id=key, aws_secret_access_key=secret)
    print 'init', self.conn

  def list(self):
    return self.conn.list_tables()['TableNames']


  def get(self, table_name, auto_create=True):

    if table_name not in self.list():
        self.createTable(table_name)

    table = Table(table_name, connection = self.conn)
    return DynamoDict(table)

  def createTable(self, table_name, block=True):
        table = self.conn.create_table(
            attribute_definitions=[{'AttributeName': 'key', 'AttributeType': 'S'}],
            table_name=table_name,
            key_schema=[{u'AttributeName': u'key', u'KeyType': u'HASH'}],
            provisioned_throughput={'ReadCapacityUnits' : 1, 'WriteCapacityUnits': 1})

        if block:
            while self.conn.describe_table(table_name)['Table']['TableStatus'] == 'CREATING':
                time.sleep(.1)
        return table
