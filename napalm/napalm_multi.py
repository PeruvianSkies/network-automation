from napalm import get_network_driver
import json

list_router = ["10.10.10.1","10.10.10.2"]

for router in list_router:
  driver = get_network_driver("ios")
  ios_r = driver(router,"blank","blank")
  ios_r.open()

  r_facts = ios_r.get_facts()
# print json.dumps(r1_facts, indent=4)

  hostname = r_facts["hostname"]
  uptime = r_facts["uptime"]

  print "{} standby for {} second".format(hostname, uptime)

  ios_r.close()