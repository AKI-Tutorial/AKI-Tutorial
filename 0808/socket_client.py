# -*- coding: utf-8 -*-
'''

1.スライドのフローチャートを参照しながら,
  以下のmain()内のコードを正しく並び替えて動作させて下さい.

(2.余裕があれば)
   #の部分に,その処理が何を行っているかネットで調べて簡単に記述して下さい.

'''

import socket

def main():


    '''1'''
    sock.close() # 


    '''2'''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 


    '''3'''
    host = '192.168.0.13' # 
    port = 4005


    '''4'''
    try:
        sock.connect((host, port)) # 
    except:
        print 'ERROR: Cannnot connect'
        sock.close()
        return


    '''5'''
    while True:  

        try:      
            msg = raw_input() # キーボードから入力を受け取る.

            if msg == 'quit': # 終了条件
                sock.send('quit'.format('b'))
                break
        
            else: # 
                sock.send(msg.format('b'))
                print 'Complete :', sock.recv(4096)

        except: # 例外処理が起きたら終了する
            sock.send('quit'.format('b'))
            break


    return


if __name__ == '__main__':
    
    main()


