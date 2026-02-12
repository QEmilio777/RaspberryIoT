import socket

class Server:
    def __init__(self,
                 server_ip="0.0.0.0",
                 server_port=2222,
                 buffer_size=1024,
                 timeout=2):

        self.server_address = (server_ip, server_port)
        self.buffer_size = buffer_size
        self.timeout = timeout

        self.sock = None
        self.last_data = None
        self.last_addr = None

    def begin(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.server_address)
        self.sock.settimeout(self.timeout)
        print(f"Server listening on {self.server_address}")

    def hear(self):
        try:
            data, addr = self.sock.recvfrom(self.buffer_size)
            self.last_data = data
            self.last_addr = addr
            return data.decode()
        except socket.timeout:
            return None

    def send(self, msg, addr=None):
        if not self.sock:
            raise RuntimeError("Server not initialized")

        target = addr if addr else self.last_addr
        if not target:
            return

        self.sock.sendto(msg.encode(), target)

    def close(self):
        if self.sock:
            self.sock.close()
            self.sock = None
        