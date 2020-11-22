## paramiko

* conf t
* username "blank" secret "blank"
* username "blank" privilege 15
* ip domain-name "blank.local"
* crypto key generate rsa modulus 1024
* line vty 0 4
* login local
>ssh "blank"@10.10.10.1

>ssh -l "blank" 10.10.10.1

* ifconfig eth0 10.10.10.10/24