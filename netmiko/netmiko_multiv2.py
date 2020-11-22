from netmiko import ConnectHandler
import getpass

username = raw_input("Username: ")
password = getpass.getpass()

for x in range(1,3):
  router = {
        "device_type" : "cisco_ios",
        "ip" : "10.10.10.{}".format(x),
        "username" : username,
        "password" : password
  }

  conn = ConnectHandler(**router)
  print "IP Address on {}".format(router["ip"])
  print conn.send_command("show ip int brief")
  print "\n"