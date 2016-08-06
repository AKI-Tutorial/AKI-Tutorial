# -*- coding: utf-8 -*-
'''
@author Kan Mayoshi <k_mayoshi@ac.jaxa.jp>
Usage: $ python socket_server.py
'''

import socket
import thread

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.0.13' # サーバーのIPアドレス
port = 4005


def main():
  
    sock.bind((host, port)) # portを開く
    sock.listen(5) # 接続を待つ
  
    try:
        while True: 
            conn, address = sock.accept() # listen中に申請が来たら受け付ける, connには相手の情報が入る
            print 'connected with...', address
            thread.start_new_thread(handler, (conn, address))
  
    except:  
        sock.close()


def handler(clientsock, addr):

    while True:
        msg = clientsock.recv(4096) # メッセージを受信

        if msg == 'quit'.format('b'): # 通信終了      
            break
    
        else: # メッセージを表示、送り返す
            print msg
            clientsock.send(msg) 

    print 'End connection with...', addr
    clientsock.close()

    
if __name__ == '__main__':
    main()


