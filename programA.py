# Program Name: programA.py 
# Course: IT3883/Section W02
# Student Name: Anthony Giso
# Assignment Number: 4
# Due Date: 10/26/ 2025
# two small python programs to implement basic network communications
# Used Python module and chapters.
import socket


HOST = '127.0.0.1'
PORT = 40001

# makes tcp
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# string input
message = input("Enter message to send to programB ")


client_socket.sendall(message.encode())


response = client_socket.recv(1024)
print(f"message sent back from programB: {response.decode()}")


client_socket.close()
