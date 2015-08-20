import json
import pprint

import requests

resp = requests.get('http://localhost:3000/info/data')

pp = pprint.PrettyPrinter(width=-1)

print '--------------------------'
# pp.pprint(url.read().__dict__)

print resp.status_code
for key, value in resp.headers.items():
    print "{:20} {}".format(key.upper() + ":", value)
# print json.dumps(resp.headers.items()., sort_keys=True)
# pprint.pprint(resp.headers)
print
print json.loads(resp.content)
