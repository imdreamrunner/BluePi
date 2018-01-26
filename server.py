# -*- coding: utf-8 -*-
from bluetooth import *

# 设置服务 UUID
uuid = "63078d70-feb9-11e7-9812-dca90488bd22"

# 创建服务端 Socket
bluetooth_socket = BluetoothSocket(RFCOMM)
bluetooth_socket.bind(("", PORT_ANY))
bluetooth_socket.listen(1)

# 创建布告服务
advertise_service(
    bluetooth_socket,
    "Chat On Pi",
    service_id=uuid,
    service_classes=[uuid, SERIAL_PORT_CLASS],
    profiles=[SERIAL_PORT_PROFILE],
)

# 获取客户端连接
client, client_info = bluetooth_socket.accept()
print "客户连接：", client_info

while True:
    # 获取客户发送的内容
    data = client.recv(1024)
    print "对方：", data

    q = raw_input("我：")
    if q == "exit":
        break
    elif q:
        # 向客户端发送内容
        client.send(q)

# 关闭客户端连接
client.close()

# 关闭服务器连接。
bluetooth_socket.close()
