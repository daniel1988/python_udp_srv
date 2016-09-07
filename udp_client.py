#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *
import yaml

class UdpClient:

    def __init__(self):
        f = open('cfg.yaml')
        cfg = yaml.load(f)
        if not cfg:
            HOST = '127.0.0.1'
            PORT = '8800'
            self.ADDR = (HOST, PORT)
        else:
            self.ADDR = (cfg['host'], cfg['port'])
        self.udp_cli = socket(AF_INET, SOCK_DGRAM)


    def sendMsg(self, data):
        self.udp_cli.sendto(data, self.ADDR)
        print self.udp_cli.recvfrom(1024)

    def input(self):
        while True:
            data = raw_input('> ')
            self.udp_cli.sendto(data, self.ADDR)
            data = self.udp_cli.recvfrom(1024)
            if not data:
                break
            print data
        self.udp_cli.close()

udpCli = UdpClient()
udpCli.sendMsg('Hello world')
udpCli.input()