# file: rfcomm-server.py
# auth: Albert Huang <albert@csail.mit.edu>
# desc: simple demonstration of a server application that uses RFCOMM sockets
#
# $Id: rfcomm-server.py 518 2007-08-10 07:20:07Z albert $

from bluetooth import *

bluetooth_socket = BluetoothSocket(RFCOMM)
bluetooth_socket.bind(("", PORT_ANY))
bluetooth_socket.listen(1)

port = bluetooth_socket.getsockname()[1]

uuid = "63078d70-feb9-11e7-9812-dca90488bd22"

advertise_service(
    bluetooth_socket,
    "Chat On Pi",
    service_id=uuid,
    service_classes=[uuid, SERIAL_PORT_CLASS],
    profiles=[SERIAL_PORT_PROFILE],
)

print("Waiting for connection on RFCOMM channel %d" % port)

client, client_info = bluetooth_socket.accept()
print("Accepted connection from ", client_info)

try:
    while True:
        data = client.recv(1024)
        client.send("Hi there, I receive %s" %  data)
        if len(data) == 0:
            print "break"
            break
        print("received [%s]" % data)
except IOError:
    print "io error"
    pass

print("Client disconnected")

client.close()
bluetooth_socket.close()
print("all done")
