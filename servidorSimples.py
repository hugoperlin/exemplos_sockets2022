import socket

HOST ='localhost'
PORT = 12346
BUFSIZ = 1024
ADDR = (HOST, PORT)


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(ADDR)
    server_socket.listen(5)
    server_socket.setsockopt( socket.SOL_SOCKET,socket.SO_REUSEADDR, 1 )
    while True:
        print('Server waiting for connection...')
        client_sock, addr = server_socket.accept()
        print('Client connected from: ', addr)
        while True:
            data = client_sock.recv(BUFSIZ)
            data = data.decode("utf-8")
            print(type(data))
            if not data or data == 'END':
                break
            #print("Received from client: %s" % data.decode('utf-8'))
            print("Received from client {}: {}".format(addr,data))
            try:
                data = data.upper()
                print(data)
                client_sock.send(data.encode('utf-8'))
            except KeyboardInterrupt:
                print("Exited by user")
        client_sock.close()
    server_socket.close()