import socket

hostname = "examplehost.com"
ip_address = socket.gethostbyname(hostname)

print("Hello!")
print(f"The IP address of {hostname} is {ip_address}")