from napalm import get_network_driver           # import function get_network_driver from library napalm

driver = get_network_driver("ios")              # ios is driver name , check support devices in napalm docs
ios_r1 = driver("10.10.10.1","blank","blank")   # router device ip,username,password
ios_r1.open()                                   # connect ssh router

r1_ip = ios_r1.get_interfaces_ip()              # function in napalm, check napalm docs
#r1_facts = ios_r1.get_facts()                   
print r1_ip

ios_r1.close()                                  # disconnect from ssh