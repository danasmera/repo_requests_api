#!/usr/bin/env python

import json
import requests
myuser='yourusername'
mypass='yourpassword'

r = requests.get('https://api.github.com/user', auth=(myuser, mypass))
res = r.json()

for item in res:
  print item, '--->' , res.get(item)
