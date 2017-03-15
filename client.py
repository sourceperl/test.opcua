#!/usr/bin/env python3

from opcua import Client

if __name__ == '__main__':
    client = Client('opc.tcp://localhost:4840/freeopcua/server/')
    try:
        client.connect()
        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        root = client.get_root_node()
        # Now getting a variable node using its browse path
        myvar = root.get_child(['0:Objects', '2:MyObject', '2:MyVariable'])
        myvar2 = root.get_child(['0:Objects', '2:MyObject', '2:MyVariable2'])
        print('myvar data value: %s' % myvar.get_data_value())
        print('myvar2 data value: %s' % myvar2.get_data_value())
    finally:
        client.disconnect()
