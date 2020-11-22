import paramiko
import time
import getpass

ip_address = raw_input("IP Address: ")
username = raw_input("Username: ")
password = getpass.getpass()

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username, password=password)

print "Success login to {}".format(ip_address)
conn = ssh_client.invoke_shell()

conn.send("conf t\n")
conn.send("int lo20\n")
conn.send("ip add 10.0.0.20 255.255.255.255\n")
time.sleep(1)

output = conn.recv(65535)
print output

ssh_client.close()

