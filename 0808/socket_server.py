# -*- coding: utf-8 -*-
'''
@author Kan Mayoshi <k_mayoshi@ac.jaxa.jp>
Usage: $ python socket_server.py
'''

import socket
import thread
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.0.13' # サーバーのIPアドレス
port = 4005


def main():
  
    sock.bind((host, port)) # portを開く
    sock.listen(5) # 接続を待つ
  
    while True: 
        try:
            conn, address = sock.accept() # listen中に申請が来たら受け付ける, connには相手の情報が入る
            print 'connected with...', address
            thread.start_new_thread(handler, (conn, address))
        except:  
            sock.close()
            break


def handler(clientsock, addr):

    while True:
        msg = clientsock.recv(4096) # メッセージを受信

        if msg == 'quit'.format('b'): # 通信終了      
            clientsock.send(aa) 
            break
    
        else: # メッセージを表示、送り返す
            print msg, 'from {}'.format(addr)
            if not random.randint(1, 10) % 10:  # for fun
                msg = 'HAHAHA, YOUR COMPUTER IS HACKED!!'
            clientsock.send(msg) 

    print 'End connection with...', addr
    clientsock.close()

aa = str(
'''
　 / )))　　　
`／ イ　　　　(((ヽ
|　(＼　∧＿∧　｜　)
ヽ　ヽ`(´･ω･)／ノ/
　＼ |　⌒Ｙ⌒　/ /
　 ｜ヽ　 ｜　 ﾉ／
''')    
    
if __name__ == '__main__':
    main()

