# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:05:11 2019

@author: kdje0
"""

import urllib
import os.path
import json

url = "https://api.github.com/repositories"
filename = "repo.json"

if not os.path.exists(url):
    urllib.request.urlretrieve(url, filename)
    
items = json.load(open(filename, "r", encoding="utf-8"))

for item in items:
    description = item["description"]
    if description is not None:
        print(item["name"] + " : " + description)
