# -*- coding: utf-8 -*-
'''
@author Kan Mayoshi <k_mayoshi@ac.jaxa.jp>
Usage: $ python socket_client.py
'''

import sys
import socket

def main():
  
  host = '192.168.2.2'
  port = 4005

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((host, port)) # connectする


  while True:  
    print 'please input message...'

    try:      
      msg = raw_input()

      if msg == 'quit': # 終了条件
        sock.send('quit'.format('b'))
        print 'End connection'
        sock.close()
        break
      
      else: # メッセージを送る
        sock.send(msg.format('b'))
        print 'Complete :',sock.recv(4096)

    except: # 例外処理のとき
      sock.send('quit'.format('b'))  
      print 'End connection'
      sock.close()
      break

  return

if __name__ == '__main__':
  main()
