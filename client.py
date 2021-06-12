import socket,cv2, pickle,struct

#To create the socket it is same for both server and client
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '192.168.56.1' 
port = 2222
print("Socket Created")
print("\t\t\t\n*************************************************")

#To connect with server 
client_socket.connect((host_ip,port))
data = b""
payload_size = struct.calcsize("Q")
print("Socket Accept")
print("\t\t\t\n*************************************************")

#To capture the reciving video
while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4*1024) # 4K
        if not packet: break
        data+=packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q",packed_msg_size)[0]
    
    while len(data) < msg_size:
        data += client_socket.recv(4*1024)
    frame_data = data[:msg_size]
    data  = data[msg_size:]
    frame = pickle.loads(frame_data)
    cv2.imshow("RECEIVING VIDEO",frame)
    key = cv2.waitKey(1) & 0xFF
    if key  == ord('q'):
        break
client_socket.close()