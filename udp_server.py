#!/usr/bin/python
# -*- coding:utf8 -*-

from socket import *
from time import *
import time
import yaml

class UdpServer:
    def __init__(self):
        f = open('cfg.yaml')
        cfg = yaml.load(f)
        if not cfg:
            HOST = '127.0.0.1'
            PORT = '8800'
            self.ADDR = (HOST, PORT)
        else:
            self.ADDR = (cfg['host'], cfg['port'])
        self.udp_srv = socket(AF_INET, SOCK_DGRAM)

    def writeLog(self,data):
        data += "\n"
        file_name = "%s%s" % (time.strftime("%Y%m%d", time.localtime()),".log")
        fp = open(file_name, "ab")
        fp.write(data)

    def run(self):
        # BufferSize
        BUFFSIZE = 1024
        self.udp_srv.bind(self.ADDR)
        try:
            while True:
                print 'waiting the message...'
                data, addr = self.udp_srv.recvfrom(BUFFSIZE)
                print 'received the message: '+data+' from: ', addr
                self.writeLog(data)
                self.udp_srv.sendto('[%s] %s' % (ctime(), data), addr)
        except EOFError, KeyboardInterrupt:
            self.udp_srv.close()


UdpServer().run()
