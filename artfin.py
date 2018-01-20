import sys
import re


def checkoktet(oktet):
    return 1 if ((oktet >= 0) and (oktet <= 255)) else 0


def is_ipaddr(ipaddr):
    if (re.fullmatch(ippat, ipaddr)):
        ipaddr = ipaddr.split('.')
        for oktet2 in ipaddr:
            if (checkoktet(int(oktet2)) == 0):
                return 0
        return 1


def is_ipnet(ipaddr):
    if (re.fullmatch(ipnetpat, ipaddr)):
        ipaddr = ipaddr.split('/')
        if not (is_ipaddr(ipaddr[0])):
            return 0
        if (int((ipaddr[1])) > 32):
            return 0
        if (is_true_ipnet(ipaddr[0], ipaddr[1]) == 0):
            return 0
        return 1


def is_true_ipnet(ipaddr, ipmask):
    ipaddr = ipaddr.split('.')
    ipstr = ''
    for oktet in ipaddr:
        ipstr += str(format(int(oktet), '08b'))
    ipmask = '1' * int(ipmask) + '0' * (32 - int(ipmask))
    if ((int(ipstr, 2) & int(ipmask, 2)) == int(ipstr, 2)):
        return 1
    return 0


def is_iprange(ipaddr):
    if (re.fullmatch(iprangepat, ipaddr)):
        ipaddr = ipaddr.split('-')
        if ((is_ipaddr(ipaddr[0]) == 0) or (is_ipaddr(ipaddr[1]) == 0)):
            return 0
        return 0 if (ipstr2int(ipaddr[1]) <= ipstr2int(ipaddr[0])) else 1
    return 0


def ipstr2int(ipaddr):
    ipaddr = ipaddr.split('.')
    ipstr = ''
    for oktet in ipaddr:
        ipstr += str(format(int(oktet), '08b'))
    return int(ipstr, 2)


def ipcheck(ip):
    if (is_ipaddr(ip)):
        return ("this is ip")
    if (is_ipnet(ip)):
        return ("this is subnet")
    if (is_iprange(ip)):
        return ("this is iprange")
    return ("unknown")


sys.argv.pop(0)
ippat = r"(\d{1,3}[\.]){3}\d{1,3}"
ipnetpat = r"(\d{1,3}[\.]){3}\d{1,3}\/\d{1,2}"
iprangepat = r"(\d{1,3}[\.]){3}\d{1,3}-(\d{1,3}[\.]){3}\d{1,3}"
for args in sys.argv:
    print(args)
    print(ipcheck(args))
