import telnetlib                                    # library telnet

host = "10.10.10.1"                                 # IP router cisco telnet
user = "cisco"                                      # user dan pass router cisco
password = "cisco"

tn = telnetlib.Telnet(host)                         # connect ke host

tn.read_until("Username: ")                         # read user
tn.write(user + "\n")

tn.read_until("Password: ")                         # read password
tn.write(password + "\n")

tn.write("conf t\n")                                # mode config
tn.write("int lo0\n")                               # interface loopback 0
tn.write("ip address 1.1.1.1 255.255.255.255\n")    # ip address for loopback 0
tn.write("end\n")                                   # exit config
tn.write("exit\n")                                  # exit

print tn.read_all()                                 # read for output telnet