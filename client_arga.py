import sys, socket, select, string

uname = []

if __name__ == "__main__":
         
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    try :
        s.connect(('localhost', 8080))
    except :
        
        sys.exit()
    
    sys.stdout.write('Ketik username[spasi]nama yang kamu inginkan: '); 
    uname = sys.stdin.readline().rstrip('\n')
    sys.stdout.flush()
    s.send(uname)    
    user = uname.split(' ', 1)
    	
    flag= "OK"
    datas = s.recv(4096)
    if flag != str(datas):
	sys.stdout.write(datas)
	print "\nSambungan akan terputus\n"
	sys.exit()

    print 'Tersambung ke ruang chat. Mulai chatting dengan teman anda sebagai: ' + str(user[1])
         
    while 1:
        socket_list = [sys.stdin, s]
         
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print '\nTerputus dari server'
                    sys.exit()
                else :
                    sys.stdout.write(data)
                         
            else :
                msg = sys.stdin.readline()
                s.send(msg)
             
