# -*- coding: utf-8 -*-
from bluetooth import *
import sys
import security

# 获取服务
uuid = "63078d70-feb9-11e7-9812-dca90488bd22"
service_matches = find_service(uuid=uuid)

if len(service_matches) == 0:
    print("找不到对应的服务。")
    sys.exit(1)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print "找到蓝牙服务", first_match

# 创建客户端 Socket
socket = BluetoothSocket(RFCOMM)
socket.connect((host, port))

my_public_key = security.get_public_key()
socket.send(my_public_key)

server_public_key = socket.recv(1024)
print 'server_public_key', server_public_key

# 收发数据
while True:
    q = raw_input("我：")
    if q == "exit":
        break
    elif q:
        # 向客户端发送内容
        socket.send(q)

    # 获取客户发送的内容
    print "对方：", socket.recv(1024)

# 关闭连接
socket.close()
