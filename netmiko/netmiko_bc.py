from netmiko import ConnectHandler      # import function ConnectHandler from netmiko library

r1 = {                                  # variable definisi device use
        "device_type" : "cisco_ios",
        "ip" : "10.10.10.1",
        "username" : "blank",
        "password" : "blank"
}

conn = ConnectHandler(**r1)

print conn.send_command("show ip int br")