import paramiko                     # library paramiko
import time                         # library time

ip_address = '10.10.10.1'           # ip address router
username = 'blank'
password = 'blank'

ssh_client = paramiko.SSHClient()   # function sshClient from paramiko
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())    # auto add policy
ssh_client.connect(hostname=ip_address,username=username, password=password)

print "Success login to {}".format(ip_address)
conn = ssh_client.invoke_shell()    # enter cisco shell

conn.send("conf t\n")
conn.send("int lo20\n")
conn.send("ip add 10.0.0.20 255.255.255.255\n")
time.sleep(1)                       # suspend 1 second

output = conn.recv(65535)           # output cmd receive 65535byte
print output

ssh_client.close()