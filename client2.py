import sys, socket, select
 
def client2():

    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
   
    try :
        s.connect((host, port))
    except :
        sys.exit()
     
    sys.stdout.write('Client 2: '); sys.stdout.flush()
     
    while 1:
        socket_list = [sys.stdin, s]

        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:            
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    sys.stdout.write('Client 2: '); sys.stdout.flush()     
            
            else :
                msg = sys.stdin.readline()
                s.send(msg)
                sys.stdout.write('Client 2: '); sys.stdout.flush() 

if __name__ == "__main__":

    sys.exit(client2())
