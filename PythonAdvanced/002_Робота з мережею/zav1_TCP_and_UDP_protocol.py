# ������� ������ �������, ��������� �� �����, � ����� ���������� ������ � TCP �� UDP ����������� � Python.


# ������ ������� TCP �� UDP ���������
# TCP (Transmission Control Protocol)
# �'������� ��������: TCP ���������� �'������� �� �볺���� � �������� ����� ��������� �����, �� ��������� �������� ��'����.
# ��������: TCP ������� �������� ����� � ����������� ������� �� ��� �����.
# �������� �������: TCP ����������� �������� ����������� ��� � �������� �������� ��������� ������ ��� ������������ �������� �����.
# �������� ������: TCP ��������� ��������� ������� ����� ��� ��������� �������������� �����.
# UDP (User Datagram Protocol)
# ����'������� ��������: UDP �� ���������� �'������� ����� ��������� �����, �� ������ ���� �������, ��� ���� �������.
# ����� ��������: UDP �� ������� �������� ����� � �� ��������� �� ���������� �������.
# ����� ��������: ������� ���� �������� ��������, UDP �������� ��� �������, �� ���������� ������ �������� �����
# (���������, �������� ���� ��� ������-����).
# ������ � TCP �� UDP � Python
# TCP � Python
# ��� ������ � TCP � Python ��������������� ������ socket.

#                   ������� TCP �������:
import socket

# ��������� TCP ������
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ����'���� ������ �� ������ � �����
server_socket.bind(('localhost', 12345))

# ������� ��������������� (�������� 5 ���������� ���������)
server_socket.listen(5)
print("������ �������� � �������������� �� ����� 12345...")

while True:
    # ��������� ����������
    client_socket, client_address = server_socket.accept()
    print(f"ϳ�������� �볺��� � �������: {client_address}")

    # ��������� ����� �� �볺���
    data = client_socket.recv(1024)
    print(f"�������� ���: {data.decode()}")

    # ³������� ������ �볺���
    client_socket.sendall(b'����� �� �������!')

    # �������� �'������� � �볺����
    client_socket.close()

#                   ������� TCP �볺���:
import socket

# ��������� TCP ������
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ϳ��������� �� �������
client_socket.connect(('localhost', 12345))

# ³������� ����� �� ������
client_socket.sendall(b'����� ������!')

# ��������� ������ �� �������
data = client_socket.recv(1024)
print(f"�������� �������: {data.decode()}")

# �������� �'�������
client_socket.close()


# UDP � Python
# ��� ������ � UDP � Python ����� ��������������� ������ socket.

#                   ������� UDP �������:
import socket

# ��������� UDP ������
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ����'���� ������ �� ������ � �����
server_socket.bind(('localhost', 12345))
print("UDP ������ �������� � �������������� �� ����� 12345...")

while True:
    # ��������� ����� �� �볺���
    data, client_address = server_socket.recvfrom(1024)
    print(f"�������� ��� �� {client_address}: {data.decode()}")

    # ³������� ������ �볺���
    server_socket.sendto(b'����� �� UDP �������!', client_address)

#                   ������� UDP �볺���:
import socket

# ��������� UDP ������
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ³������� ����� �� ������
client_socket.sendto(b'����� UDP ������!', ('localhost', 12345))

# ��������� ������ �� �������
data, server_address = client_socket.recvfrom(1024)
print(f"�������� �������: {data.decode()}")

# �������� ������ (�����������)
client_socket.close()
ϳ������
TCP �������� ��� �������, �� ������� �������� �������� �����, ����� �� ���-�������, ���� �����, ���������� ���������.
UDP �������� ��� �������, �� ������� �������� � ������ ��������, ����� �� �������� ����, ������� �� ���� ������,
������-����.
ֳ �������� ������������ ������ ������������ TCP �� UDP ��������� � Python ��� ��������� ������� �� �볺���.
