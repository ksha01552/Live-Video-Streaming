import socket, cv2, pickle, struct

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print(" HOST IP :", host_ip)
port = 9999

socket_addr = (host_ip, port)

server_socket.bind(socket_addr)

server_socket.listen(5)
print(" Server listening on : ", socket_addr)

while True:
    client_socket , addr = server_socket.accept()
    print("Got connection from : ", addr)
    if client_socket:
        vid = cv2.VideoCapture(0)
        while(vid.isOpened()):
            img, frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            client_socket.sendall(message)
            cv2.imshow("Transmitting video", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()