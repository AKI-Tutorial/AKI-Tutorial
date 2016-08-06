# -*- coding: utf-8 -*-
'''
@author Kan Mayoshi <k_mayoshi@ac.jaxa.jp>
Usage: $ python socket_server.py

・どう問題にするか
  関数を選択肢として与えておいて、それと別でブロック図みたいのを見せて、その通りに組ませるとか？
'''

import socket
import thread

# socketの形式の指定
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET->IPv4を使用する # SOCK_STREAM->TCP/IPを用いたSTREAM型のソケット

host = '192.168.2.2' # serverのIPアドレスとポート番号
port = 4005

def main():
  
  sock.bind((host, port)) # portを開く
  sock.listen(5) # 接続を待つ、backlog=5
  
  while True: 
    conn, address = sock.accept() # listen中に申請が来たら受け付ける, connには相手の情報が入る
    print 'connected with...', address
    thread.start_new_thread(handler, (conn, address))

def handler(clientsock, addr):

  while True:
    msg = clientsock.recv(4096) # メッセージを受信 ,4096は最大のbufsize

    if msg == 'quit'.format('b'): # 通信終了
      print 'End connection with...',addr
      sock.close()
      break
    
    else:
      print msg
      clientsock.send(msg) # メッセージを送り返す

  
if __name__ == '__main__':
    
    main()
