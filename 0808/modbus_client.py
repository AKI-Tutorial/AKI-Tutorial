#!/usr/bin/env python
""" 
Sample program for Modbus TCP client
Target Device: Advantech ADAM-6017 AD Converter

@author  Kyohei Otsu <kyon@ac.jaxa.jp>
@date    2016-08-07

Usage:
    $ python modbus_client.py
"""

from pymodbus.client.sync import ModbusTcpClient


def raw2volt(raw):
    ''' convert raw sensor readings to voltage 
        Input: 
            raw: array of 16-bit raw measurements
        Return: 
            converted voltage in -10 -- 10[V]
            
    '''
    nbit = 16                    # bit depth
    maxv = 10.0                  # max volt [V]
    vpb  = 2 * maxv / 2 ** nbit  # voltage per bit
    base = 2 ** (nbit - 1)       # zero point [bit]
    return [(m - base) * vpb for m in raw]


def main():
    ### setup the client ###
    ipaddr = '192.168.201.17'
    port   = 502
    print 'Connecting to', (ipaddr, port)
    client = ModbusTcpClient(ipaddr, port=port)

    ### fetch data ###
    try:
        reg = client.read_input_registers(0, 8)  # data request
        vlt = raw2volt(reg1.registers)  # convert bit to voltage (-10 -- 10[V])
    except:
        print 'Data fetch error. Finishing...'
        client.close()
        return

    ### convert voltage to engineering values ###
    meas = vlt  # TODO: CHANGE THIS

    ### show data ###
    print 'Raw measurement:', vlt
    print 'Engineering value:', meas

    ### finalizing ###
    client.close()


if __name__ == '__main__':
    main()

