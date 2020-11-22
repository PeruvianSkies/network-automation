from napalm import get_network_driver
import json

driver = get_network_driver("ios")
ios_r1 = driver("10.10.10.1","blank","blank")
ios_r1.open()

r1_ip = ios_r1.get_interfaces_ip()
print json.dumps(r1_ip, indent=4)

ios_r1.close()