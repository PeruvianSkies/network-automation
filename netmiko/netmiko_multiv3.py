from netmiko import ConnectHandler
import getpass

ip_router = raw_input("IP Router (separate by comma): ")
username = raw_input("Username: ")
password = getpass.getpass()

ip_list = ip_router.split(",")
print ip_list

for ip in ip_list:
  router = {
        "device_type" : "cisco_ios",
        "ip" : ip,
        "username" : username,
        "password" : password
  }

  conn = ConnectHandler(**router)
  print "IP Address on {}".format(router["ip"])
  print conn.send_command("show ip int brief")
  print "\n"