# -*- coding: utf-8 -*-
'''
複数通信
一行ごとに送り返す
surver1 vs client 複数通信
'''



import socket
from contextlib import closing



def main():
  
  # 相手のIPアドレスとポート番号の設定
  host = '192.168.11.32' # server側のIPアドレス
  port = 4005 # このport番号を開く！

  # socketの形式の指定
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # AF_INET->IPv4を使用する
  # SOCK_STREAM->TCP/IPを用いたSTREAM型のソケット

  backlog = 10
  bufsize = 4096
  # 受信するbufsizeのサイズ

  with closing(sock): # withを抜ける(通信を終了する)たら、socket通信を閉じる？
    sock.bind((host, port)) 
    # portを開いとく
    # IPアドレスがなかったらエラーでる
    '''調べる'''
    sock.listen(backlog) # 相手からの接続待ち、いくつのbacklogまで見るか？
    


    while True: # 多分withで通信を終えるとここに戻る
      conn, address = sock.accept() # ここで待機してるらしい
      # print 'connected with...', conn
      # accept→接続リクエストを受け取って、対応するIPアドレスとポート番号を返す
      # 多分通信相手のIPアドレスが送られてくるはず

      with closing(conn):
        msg = conn.recv(bufsize) # メッセージを受信
        conn.send(msg) # メッセージを送り返す
        print msg

  return

if __name__ == '__main__':
    # print 'start'
    main()