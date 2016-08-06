# -*- coding: utf-8 -*-
'''
@author Kan Mayoshi <k_mayoshi@ac.jaxa.jp>
Usage: $ python socket_client.py
'''

import socket

def main():
  
    host = '192.168.0.13'
    port = 4005

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((host, port))
    except:
        print 'ERROR: Cannnot connect'
        sock.close()
        return

    while True:  

        try:      
            msg = raw_input()

            if msg == 'quit': # 終了条件
                sock.send('quit'.format('b'))
                break
        
            else: # メッセージを送る
                sock.send(msg.format('b'))
                print 'Complete :', sock.recv(4096)

        except: # 例外処理が起きたら終了する
            sock.send('quit'.format('b'))
            break

    print 'End connection'
    sock.close()
    return

if __name__ == '__main__':
    main()

