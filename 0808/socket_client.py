# -*- coding: utf-8 -*-
import sys
import socket
from contextlib import closing

def main():
  host = '192.168.11.32'
  # port = 88
  port = 4002

  bufsize = 4096

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  with closing(sock):
    sock.connect((host, port))
    # connectする
    msg = sys.argv[1].format('b')
    sock.send(msg)
    print(sock.recv(bufsize))
  return

if __name__ == '__main__':
  main()