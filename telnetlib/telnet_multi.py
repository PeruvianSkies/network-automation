import telnetlib

host_list = ['10.10.10.1','10.10.10.2']
user = "cisco"
password = "cisco"

for host in host_list:
    tn = telnetlib.Telnet(host)

    tn.read_until("Username: ")
    tn.write(user + "\n")

    tn.read_until("Password: ")
    tn.write(user + "\n")

    tn.write("conf t\n")

    for x in range(1,10):
        tn.write("int lo{}\n".format(x))
        tn.write("ip address 10.0.0.{} 255.255.255.255\n".format(x))

    tn.write("end\n")
    tn.write("exit\n")

    print tn.read_all()