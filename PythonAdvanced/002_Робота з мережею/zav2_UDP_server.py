# ������� UDP-������, ���� ����� �� ����������� ��� ��� ������� � �����. ³� ������ ����������� ������� �������,
# �� ���� ������������� ��������, � ����� ��� ��'������� � �������. ������� UDP-�볺���, ���� ����������� ���������
# ������������� �������� �� ������, ����������� ��� ���� ����������.


# UDP-������

import socket

# ��������� UDP-������
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ����'���� ������ �� ������ � �����
server_socket.bind(('localhost', 12345))
print("UDP the server is running and listening on the port 12345...") # ������ �������� � �������������� �� �����

# �������� �������������� ��������
devices = set()

while True:
    # ��������� ����� �� �볺���
    data, client_address = server_socket.recvfrom(1024)
    device_id = data.decode()

    # ���� �������������� ��������
    if device_id not in devices:
        devices.add(device_id)
        print(f"New device connected: {device_id}") #  ����� ������� ���������:

    # ³������� ������������ �볺��� (�����������)
    server_socket.sendto(b'The device is registered', client_address) # ������� ������������
# UDP-�볺��

import socket

# ��������� ������������� ��������
device_id = "device_12345"

# ��������� UDP-������
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ³������� ����� �� ������
client_socket.sendto(device_id.encode(), ('localhost', 12345))

# ��������� ������ �� ������� (�����������)
data, server_address = client_socket.recvfrom(1024)
print(f"A response was received from the server: {data.decode()}") # �������� ������� �� �������:

# �������� ������ (�����������)
client_socket.close()

# ���� ������
# UDP-������:

# ������� UDP-����� � ����'��� ���� �� ����� 12345.
# ���������� ����������� �� �볺���.
# ������ ������� �������������� �������� � ������ devices.
# ��� �������� ������ �������������� ����� ���� � �������.
# UDP-�볺��:

# ������� ��������� ������������� ��������.
# ������� UDP-�����.
# ³�������� ������������� �� ������.
# ������ ������������ �� ������� (�����������).
# �������� �������� ������, � ���� �볺�� ��� �������� ������. �� ������ ��������� ����� �볺��� � ������ ����������������,
# ��� ��������, �� ������ ����� �� ��� ����������.