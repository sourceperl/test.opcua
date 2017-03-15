#!/usr/bin/env python3

import time
from opcua import ua, Server


if __name__ == "__main__":
    # setup server
    server = Server()
    server.set_endpoint('opc.tcp://0.0.0.0:4840/freeopcua/server/')

    # setup namespace
    uri = 'http://github.com/sourceperl/test.opcua'
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, 'MyObject')
    myobj2 = objects.add_object(idx, 'MyObject2')
    # myobj
    myvar = myobj.add_variable(idx, 'MyVariable', 6.7)
    myvar2 = myobj.add_variable(idx, 'MyVariable2', 66)
    foovar = myobj2.add_variable(idx, 'Foo', 42)
    # set writable by clients
    myvar.set_writable()
    myvar2.set_writable()

    # start
    server.start()

    try:
        count = 0
        # main loop
        while True:
            time.sleep(1)
            count += 0.1
            myvar.set_value(count)
    finally:
        # close connection
        server.stop()
