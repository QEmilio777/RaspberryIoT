from server_library import Server

server = Server()
server.begin("Soy el servidor de prueba, en el puerto: ")

while True:
    
    message_from_client = server.hear()
    print(message_from_client)
    
    server.send("recibí tu mensaje")