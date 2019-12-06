# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:55:42 2019

@author: kdje0
"""

import collections
import json
import os

price = collections.OrderedDict() #들어간 순서가 유지되는 dict
fruit = collections.OrderedDict()

fruit["Apple"] = 80
fruit["Orange"] = 55
fruit["Banana"] = 40

market = "마트하나", "마트둘", "Mart-III"

price["date"] = "2019-09-17"
price["price"] = fruit
price["markets"] = market

with open(os.path.dirname(os.path.abspath(__file__))+'\price.json', 
          	'w', encoding='utf-8') as f:
            json.dump(price, f, ensure_ascii=False, indent='\t')

price_loaded = json.load(open(os.path.dirname(os.path.abspath(__file__))+'\price.json', 
             			'r', encoding="utf-8"))
for mkt in price_loaded["markets"] : 
    print(mkt)
