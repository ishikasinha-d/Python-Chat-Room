import socket
import time
import threading

# creating a socket
# AF_INET : Address familt IPv4
# SOCK_DGRAM : Connectionless Protocol i.e UDP (User Datagram Protocol)
s= socket.socket( socket.AF_INET, socket.SOCK_DGRAM)

ip = input(" Enter your IP: ")
port = input( "Enter port no. you want to run this server on")

# binding the port/address to the socket 
s.bind(( ip, port ))

ip_server= input(" Enter server side IP: ")
port_server= input(" Enter port no.")
def receive():
    while True:
        response=s.recvfrom(1024)     
        mssg_server= response[0].decode()   # Message from server in "string format"
        print ("\n"+ip_server + " : " + mssg_server )
        print ("Time : "+ curr_time)

def send():
    while True:
        s.sendto( input().encode(), ( ip_server, port_server ))

# finding time
x= time.asctime( time.localtime() )
y=x.split(' ')
curr_time= "{} {}{} {}".format(y[3],y[1],y[2],y[4])

# applying multithreading
thread1= threading.Thread( target= receive )
thread2= threading.Thread( target= send )
thread1.start()
thread2.start()