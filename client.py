import socket
import time
import os
import platform
import threading


class client:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        while True:
            self.server_ip = input('Enter Server IP: ')
            self.server_port = 12345
            if len(self.server_ip.split('.')) < 4:
                continue
            break
        print('Finding connection')
        time.sleep(1)

    @property
    def make_connection(self):
        while True:
            try:
                server = (self.server_ip, self.server_port)
                self.client_socket.connect(server)
                print('Connected!')
                return True
            except:
                print('..')
                time.sleep(0.1)
                print('..' * 2)
                time.sleep(0.1)
                print('..' * 6)
                time.sleep(0.1)
                if platform.system().lower().startswith('win'):
                    os.system('cls')
                    continue
                os.system('clear')

    def send_sms(self, msg):
        self.client_socket.send(msg.encode())

    def receive_sms(self):
        while True:
            data = ''
            data = self.client_socket.recv(1024).decode()
            time.sleep(0.001)
            print(data)

    def chat_room(self, name):
        if self.make_connection:
            Receiving_cio = threading.Thread(target=self.receive_sms)
            Receiving_cio.daemon = True
            Receiving_cio.start()
            self.name = name
            while True:
                message = input()
                message = f"\n{self.name}:  {message}\n"
                self.send_sms(message)
                continue


def clientr(name):
    Client = client()
    Client.chat_room(name)
