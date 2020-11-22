from netmiko import ConnectHandler
import getpass

ip_router = raw_input("IP Router: ")
username = raw_input("Username")
password = getpass.getpass()
command = raw_input("Command: ")

r1 = {
        "device_type" : "cisco_ios",
        "ip" : ip_router,
        "username" : usename,
        "password" : password
}

conn = ConnectHandler(**r1)

print conn.send_command(command)