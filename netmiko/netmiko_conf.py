from netmiko import ConnectHandler
import getpass

ip_router = raw_input("IP Router: ")
username = raw_input("Username: ")
password = getpass.getpass()

config_list = ['int lo0','ip address 10.0.0.1 255.255.255.255', 'int lo1','ip address 10.0.0.2 255.255.255.255']

r1 = {
        "device_type" : "cisco_ios",
        "ip" : ip_router,
        "username" : usename,
        "password" : password
}

conn = ConnectHandler(**r1)

print conn.send_config_set(config_list)
print conn.send_command("show ip int brief")