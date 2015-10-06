import sys, socket, select

HOST = '' 
SOCKET_LIST = []
LOGIN = []
RECV_BUFFER = 4096 
PORT = 8080

def server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    SOCKET_LIST.append(server_socket)
 
    print "port = " + str(PORT)
 
    while 1:

        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
      
        for sock in ready_to_read:
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
            else:
                try:
			data=sock.recv(4)
			x=0
			if data=='log ' :
			  LOGIN.append(sock.recv(4))
			if data=='list' :
			  for x in range(len(LOGIN)) :
			      sock.send(LOGIN[x])
              
                except:
                    continue

    server_socket.close()
    
def broadcast (server_socket, sock, message):
    for socket in SOCKET_LIST:
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                socket.close()
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)
 
if __name__ == "__main__":

    sys.exit(server())


         
