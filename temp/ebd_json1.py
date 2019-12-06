# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:52:10 2019

@author: kdje0
"""

import json
import os

price = { "date" : "2019-09-17",
            "price" : {
                    "Apple" : 80,
                    "Orange" : 55,
                    "Banana" : 40
            },
            "markets" : ["마트하나", "마트둘", "Mart-III"]
        }

with open(os.path.dirname(os.path.abspath(__file__))+'\price.json', 
          	'w', encoding='utf-8') as f:
            json.dump(price, f, ensure_ascii=False, indent='\t')

price_loaded = json.load(open(os.path.dirname(os.path.abspath(__file__))+'\price.json', 
             			'r', encoding="utf-8"))

for mkt in price_loaded["markets"] : 
    print(mkt)
