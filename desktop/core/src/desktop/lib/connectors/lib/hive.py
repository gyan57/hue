
from builtins import object
class Hive(object):
  NAME = 'Hive'
  TYPE = 'hive'

  VERSION = 1
  APP = 'notebook'
  INTERFACE = 'hiveserver2'
  PROPERTIES = [
    {'name': 'server_host', 'value': ''},
    {'name': 'server_port', 'value': ''},
  ]
