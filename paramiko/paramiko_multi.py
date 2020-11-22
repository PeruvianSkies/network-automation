# del interface with paramiko
import paramiko
import time
import getpass

ip_address_list = ['10.10.10.1','10.10.10.2']
username = raw_input("Username: ")
password = getpass.getpass()

for ip_address in ip_address_list:
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip_address,username=username, password=password)

    print "Success login to {}".format(ip_address)
    conn = ssh_client.invoke_shell()

    conn.send("conf t\n")

    for x in range(20):
        if ip_address == "10.10.10.2":
          if x < 10 or x == 19:
            continue
        conn.send("no int lo{}\n".format(x))
        time.sleep(0.5)

    output = conn.recv(65535)
    print output

    ssh_client.close()