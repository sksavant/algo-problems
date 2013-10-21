#!/usr/bin/python
import re

ipv4regex = re.compile('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')
ipv6regex = re.compile('[0-9abcdef]+\:[0-9abcdef]+\:[0-9abcdef]+\:[0-9abcdef]+\:[0-9abcdef]+\:[0-9abcdef]+\:[0-9abcdef]+\:[0-9abcdef]+\Z')

n = int(raw_input())
for i in range(n):
    s = raw_input()
    #print s,
    try:
        ip=map(int,ipv4regex.findall(s)[0].split('.'))
        try:
            for ipblock in ip:
                assert 0<=ipblock<=255
            print "IPv4"
            continue
        except AssertionError:
            pass
    except IndexError:
        pass
    try:
        ip=ipv6regex.findall(s)[0].split(':')
        assert len(ip)==8
        try:
            #for ipblock in ip:
            #    assert len(ipblock)==4
            print "IPv6"
            continue
        except AssertionError:
            pass
    except IndexError:
        pass
    print "Neither"
