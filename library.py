import socket

BUFFER = 1024
SERVER_PORT = 7777

# Returns a server socket created at a given host and port.
def create_server(port):
  # Get the ipv6 information for port
  host = '::'
  info = socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)
  # Extract socket information (addr family, socket type, protocol)
  af, socktype, protocol, canonname, socket_addr = info[0]
  # Initialize socket
  s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
  s.bind(socket_addr)
  s.listen()
  print(f"Server initialized and running on port {port}")
  print(socket_addr)
  return s

# Returns a usable connection to a client that is accessing the server.
def connect_server(s):
  connection, (addr, port) = s.accept()
  print(f"Received connection from: {addr}:{port}")
  return connection, addr, port

# Executes command on server and/or proxy based on mode
def process_command(filepath, connection):
  # Fetch file and return
  f = open(filepath ,'rb')
  # Send file through segments
  segment = f.read(BUFFER)
  while (segment):
    connection.send(segment)
    segment = f.read(BUFFER)
  # Clean up file pointer
  f.close()
