from napalm import get_network_driver
import json

driver = get_network_driver("ios")
ios_r1 = driver("10.10.10.1","blank","blank")
ios_r1.open()

r1_facts = ios_r1.get_facts()
print json.dumps(r1_facts, indent=4)

hostname = r1_facts["hostname"]
uptime = r1_facts["uptime"]

print "{} standby for {} second".format(hostname, uptime)

ios_r1.close()