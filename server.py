from functions import *
import socket
import threading
import time


class Server:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 12345

    def __init__(self):
        server_config = (self.host, self.port)
        self.server.bind(server_config)
        self.server.listen(5)
        print("\nWaiting for Connection....")

        self.clientsocket, self.addr = self.server.accept()
        print("Connecting from ", self.addr)

    def receive_sms(self):
        try:
            while True:
                data = self.clientsocket.recv(1024).decode()
                time.sleep(0.001)
                print(data)
        except Exception as ex:
            print("The below error have occured please checkout")
            print(ex)

    def chat(self, name):
        self.Receiving_ciao = threading.Thread(target=self.receive_sms)
        self.Receiving_ciao.daemon = True
        self.Receiving_ciao.start()
        self.name = name
        while True:
            server_message = input()
            server_message = f"\n{self.name}:  {server_message}\n"
            self.clientsocket.send(server_message.encode())


def run(name):
    Server_m = Server()
    Server_m.chat(name)
    Server_m.Receiving_ciao.join()
    Server_m.server.close()
