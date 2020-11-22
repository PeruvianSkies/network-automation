import paramiko
import time
import getpass

ip_address = raw_input("IP Address: ")
username = raw_input("Username: ")
password = getpass.getpass()

loopback = raw_input("Input interface loopback: ")
ip_loopback = raw_input("Input IP Address loopback: ")

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username, password=password)

print "Success login to {}".format(ip_address)
conn = ssh_client.invoke_shell()

conn.send("conf t\n")
conn.send("int {}\n".format(loopback))
conn.send("ip add {}\n".format(ip_loopback))
time.sleep(1)

output = conn.recv(65535)
print output

ssh_client.close()