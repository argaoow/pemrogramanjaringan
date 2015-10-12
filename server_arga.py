import sys, socket, select

HOST = '' 
login = []
address = []
sockets = []

def broadcast_data (sock, message):
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                socket.close()
                CONNECTION_LIST.remove(socket)

if __name__ == "__main__":
     
    CONNECTION_LIST = []
    RECV_BUFFER = 4096
    PORT = 8080
     
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    CONNECTION_LIST.append(server_socket)
 
    print "Server berada di port " + str(PORT)
 
    while 1:
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
 
        for sock in read_sockets:
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print "Client (%s, %s) tersambung" % addr

            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
			if(data == 'list\n'):
				sock.send("\nList client yang tersambung:\n")
				for i in range (len(login)):
					sock.send(login[i])
					sock.send("\n")
			if(len(data) > 0) :
				isi = data.split(' ', 1)	
				if isi[0] == "username":
					flag=0
					for i in range (len(login)):
						if str(isi[1]) == str(login[i]):
							flag=1
					if flag==0:
	   			 		address.append(str(sock.getpeername()))
	    					login.append(str(isi[1]))
						sockets.append(sock)
						print "Client "+str(sock.getpeername())+" usernamenya: "+str(isi[1])
						broadcast_data(sock, str(isi[1])+" memasuki ruang chat\n")
						sock.send("OK")
					if flag==1:
						sock.send("\nUsername telah terpakai\n")
						sock.close()
		      			        CONNECTION_LIST.remove(sock)
					        continue
				elif isi[0] == "sendall":
					user=login[address.index(str(sock.getpeername()))]
		                	broadcast_data(sock, "\n" + 'dari ' + user + ': ' + str(isi[1]))
				elif isi[0] == "sendto":
					user=login[address.index(str(sock.getpeername()))]
					isi_sendto = str(isi[1]).split(' ', 1)
					flag=0
					tujuan = isi_sendto[0]
					for i in range (len(login)):
						if login[i]==tujuan:
							arrtuju=i
							flag=1
					if flag==0 :
						sock.send("Username yang dituju tidak ada\n")						
					else:
						sockets[arrtuju].send("\n" + 'dari ' + user + ': ' + str(isi_sendto[1]))


				elif data != 'list\n':
					sock.send("\rCommand yang dipakai tidak tersedia. Coba lagi\n")
					             
                 
                except:
		    off=login[sockets.index(sock)]
                    broadcast_data(sock, "Client "+ off +" sedang offline\n")
                    print "Client "+ off +" sedang offline"
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
     
    server_socket.close()
