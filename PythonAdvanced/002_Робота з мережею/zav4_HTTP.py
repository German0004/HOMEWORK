# ������� ������ �������, ��������� � �����, � ����� ���������� ������ � HTTP-����������� � Python, ��������������
# �������� urllib �� requests.


# ������ ������� HTTP

# HTTP (HyperText Transfer Protocol) - �� �������� ��� �������� ���������� (������, ���������, ����) � ��������.
# ³� ������ �� ��������� �볺��-������: �볺�� ������� ����� �� �������, ������ �������� ����� � ������� �������.

# ������ ���������� HTTP-������:

# ����� ������: ����� ��, ��� ������� ��������. ������ ������:
# GET: ��������� ����� � �������.
# POST: ³������� ����� �� ������.
# PUT: ��������� ����� �� ������.
# DELETE: ��������� ����� �� ������.
# HEAD: ��������� ���� ��������� ������.
# OPTIONS: ��������� ������������ ������ ��� �������.
# URL (Uniform Resource Locator): ����� ������ �������.
# ���������: ̳����� ��������� ���������� ��� ����� ��� �������.
# ҳ��: ̳����� ���, �� ����������� (��� �������� ��������������� � ������� POST, PUT).
# ������ ���������� HTTP-������:
# ��� �����: ����� ��������� ������. ������ ����:
# 200 OK: ����� ������ ��������.
# 404 Not Found: ������ �� ��������.
# 500 Internal Server Error: �������� ������� �������.
# ���������: ̳����� ��������� ���������� ��� �������.
# ҳ��: ̳����� ���, �� ������������ (��� �������� ��������������� ��� �������� HTML, JSON, XML � �.�.).
# ������ � HTTP-����������� � Python

# ��������� urllib
# urllib - �� ���������� �������� Python ��� ������ � URL � HTTP-��������. ������ �����:

# urllib.request: ̳����� ������� ��� �������� �� ������� URL.
# urllib.parse: ̳����� ������� ��� ������� URL.
# urllib.error: ̳����� �������, �� ������ ���� �������� �� ��� ������ � urllib.request.
# urllib.robotparser: ��� ������� ����� robots.txt.


# ������� ������������ urllib.request

import urllib.request

url = 'http://www.example.com'
response = urllib.request.urlopen(url)
html = response.read()

print(html)
# ���������� ������ � ������

import urllib.parse
import urllib.request

url = 'http://www.example.com'
data = urllib.parse.urlencode({'key': 'value'}).encode()
req = urllib.request.Request(url, data=data)
response = urllib.request.urlopen(req)
result = response.read()

print(result)

# ��������� requests
# requests - �� ��������� �������� �������� ��� ������ � HTTP-�������� � Python. ���� ������ ������ ������ ��������
# HTTP-������ �� ������� ��������.

# ������� ������������ requests

import requests

url = 'http://www.example.com'
response = requests.get(url)
html = response.text

print(html)

# ���������� POST-������


import requests

url = 'http://www.example.com'
data = {'key': 'value'}
response = requests.post(url, data=data)
result = response.text

print(result)

# ������ �������� �� urllib �� requests
# �������� ������������: requests �� �������� � ���������� ���������.
# ������� JSON: requests �� ��������� �������� ��� ������� JSON (����� response.json()).
# ������� ����: requests ������� ��� (���� requests.Session), �� �������� �������� ���� �� ���� ���������� �� ��������.
# ����� �����������: requests ����������� �������� ������ ������� HTTP-������, ����� �� ���������, ���������, ����.