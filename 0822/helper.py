#!/usr/bin/env python
""" Helper function for command serialization

@author  Kyohei Otsu <kyon@ac.jaxa.jp>
@date    2016-08-19

Usage:
    $ python helper.py
"""

import struct

cmd_seq = 0


def serialize(hexstr):
    ''' Convert hex string into byte lists '''
    assert len(hexstr) % 2 == 0

    serstr = ''
    for h in [hexstr[i:i+2] for i in range(0, len(hexstr), 2)]:
        serstr += chr(int(h, base=16))
    return serstr


def capsulate(cmd):
    ''' Append header and convert to byte strings'''
    global cmd_seq
    cmd_seq += 1

    marker = '0020f3fa00000000'
    sender_id = '0010'
    seq = '{:04d}'.format(cmd_seq)
    cmd_type = cmd[0]
    packet = None
    if len(cmd) > 1:
        cmd_arg = struct.pack('f', float(cmd[1:]))
    else:
        cmd_arg = struct.pack('f', float(0))
    packet = serialize(marker + sender_id + seq) + cmd_type + cmd_arg
    #print(marker + sender_id + seq) + cmd_type + cmd_arg
    return packet


## Sample code
if __name__ == '__main__':

    cmd = 'd20'
    cmd_byte = capsulate(cmd)

    print 'Original:', cmd
    print 'Packet  :', ' '.join("{:02x}".format(ord(c)) for c in cmd_byte)

