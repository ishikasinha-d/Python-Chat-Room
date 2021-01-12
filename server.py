import socket
import time
import threading

# creating a socket
# AF_INET : Address familt IPv4
# SOCK_DGRAM : Connectionless Protocol i.e UDP (User Datagram Protocol)
s= socket.socket( socket.AF_INET, socket.SOCK_DGRAM)

ip = input("Enter server side IP: ")
port = int(input( "Enter port no. : "))

# binding the port/address to the socket 
s.bind(( ip, port ))

def receive():
    global ip_client, port_client
    while True:
        response=s.recvfrom(1024)     
        ip_client= response[1][0]           # IP of client
        port_client= response[1][1]
        mssg_client= response[0].decode()   # Message from client in "string format"
        print ("\n"+ip_client + " : " + mssg_client )
        print ("Time : "+ curr_time)

def send():
    while True:
        s.sendto( input().encode(), ( ip_client, port_client ))

# finding time
x= time.asctime( time.localtime() )
y=x.split(' ')
curr_time= "{} {}{} {}".format(y[3],y[1],y[2],y[4])

# applying multithreading
thread1= threading.Thread( target= receive )
thread2= threading.Thread( target= send )
thread1.start()
thread2.start()
