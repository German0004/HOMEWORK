# �������� ������� ��� �� ����� ��������� TCP, ���� ����� ����� ��'���������� ������ �볺���� ��
# ����������� �������������.


# �������� ����� ������ � ����� �������

# 1_SERVER

import socket
import threading

# ������������ �������
HOST = '127.0.0.1'  # ��������� ����
PORT = 12345        # ���� ��� ���������������

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

# ³������� ����������� ��� ���������� �볺����
def broadcast(message):
    for client in clients:
        client.send(message)

# ������� ���������� �� �볺���
def handle_client(client):
    while True:
        try:
            # ������ ����������� �� �볺���
            message = client.recv(1024)
            broadcast(message)
        except:
            # ��������� � ���������� �볺���
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} ������� ���!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

# ������ ����� ���������
def receive():
    while True:
        client, address = server.accept()
        print(f'ϳ�������� � {str(address)}')

        # ����� � ���������� ���������
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'�������� �볺���: {nickname}')
        broadcast(f'{nickname} ��������� �� ����!'.encode('utf-8'))
        client.send('ϳ��������� �� �������!'.encode('utf-8'))

        # ������ ������� ���������� �볺��� � �������� ������
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print('������ ��������...')
receive()


# �������� ������ ����� ��������� � ����� ������ � ����� � ������� ������

# 2_CLIENTS

import socket
import threading

# ������������ �볺���
nickname = input("������ ��� ��������: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))

# ������ ���������� �� �������
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            # �������� ���������� ��� ��������� �������
            print("������� �������!")
            client.close()
            break

# ³������� ���������� �� ������
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

# ������ ������ ��� ������� � �������� ����������
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

# ���������
#
# ������:
#
# ������������� ��� ��������������� �� ���������� ���� � �����.
# ������ ���������� �볺��� � ������ ��.
# � �������� ������ �������� ����������� �� ������� �볺���.
# ³�������� ������� ����������� ��� ���������� �볺����.
#
# �볺��:
#
# ϳ���������� �� �������.
# ³�������� �������� �� ������ ��� ���������.
# � ������� ������� ������ ����������� �� ������� � ��������� ����������� �� ������.
# ������
# �������� ��������� ��� (server.py).
# �������� �볺������� ��� (client.py) � ������ ��������� �� �� ����� �������, ��� ����������� �� ������� � ������
# ����������� �������������.