import socket
import sys

# def create_connection:
#     try:
#         global host
#         global port
#         global s
        
#         host = ""
#         port = 1980
        
#         s = socket.socket()
        
#     except socket.error as msg:
#         print("Erro socket: " + str(msg))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostname('www.google.com')

print(ip)