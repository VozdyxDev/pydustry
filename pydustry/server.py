from socket import socket, create_connection, AF_INET, SOCK_DGRAM
from time import time
from .models import ByteBuffer
from .models import ServerInfo

GAMEMODES = [
    "survival",
    "sandbox",
    "attack",
    "pvp",
    "editor"
]


class Server():

    def __init__(self, host, server_port = 6567, socketinput_port = 6859):
        self.host = host
        self.server = (host, server_port)
        self.socketinput_port = socketinput_port
        
    def get_status(self):
        s = socket(AF_INET, SOCK_DGRAM)
        s.connect(self.server)
        s.send(b"\xfe\x01")
    
        info = {}
    
        data = s.recv(1024)
        buffer = ByteBuffer(data)
        info["name"] = buffer.read_string()
        info["map"] = buffer.read_string()
        info["players"] = buffer.read_integer()
        info["wave"] = buffer.read_integer()
        info["version"] = buffer.read_integer()
        info["vertype"] = buffer.read_string()
        info["gamemode"] = GAMEMODES[buffer.pop()]
        info["limit"] = buffer.read_integer()
        info["description"] = buffer.read_string()
        info["modename"] = buffer.read_string()
 
        return ServerInfo(**info)
        
    def send_command(self, command):
        s = create_connection((self.host, self.socketinput_port))
        s.sendall(bytes(command.encode()))
        s.close()
        
    def ping(self, timeout = 10.0):
        s = socket(AF_INET, SOCK_DGRAM)
        s.settimeout(timeout)
        s.connect(self.server)
        start_t = time()
        s.sendall(b"\xfe\x01")
        s.recv(1024)
        s.close()
        return(round((time()-start_t)*1000))

