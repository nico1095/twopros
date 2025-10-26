# Program Name: programB.py 
# Course: IT3883/Section W02
# Student Name: Anthony Giso
# Assignment Number: 4
# Due Date: 10/26/ 2025
# two small python programs to implement basic network communications
# Used Python module and chapters.


import socket


HOST = '127.0.0.1'  
PORT = 40001        


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Program B (Server) listening on {HOST}:{PORT}...")

# programA connected
conn, addr = server_socket.accept()
print(f"Connected by {addr}")


data = conn.recv(1024)
if data:
    received_text = data.decode()
    print(f"message received from programA: {received_text}")

   
    response = received_text.upper()

    
    conn.sendall(response.encode())
    print(f"message sent back to programA: {response}")

# Close and exit connnection
conn.close()
server_socket.close()
