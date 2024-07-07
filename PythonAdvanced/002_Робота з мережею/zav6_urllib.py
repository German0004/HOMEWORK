# �������������� ����� https://jsonplaceholder.typicode.com/, ��������� ���������� ��� ���� ������ ��
# �������� ������. ��������� ���������������� � urllib �� ��������� requests. ������������� ��������
# ���������� �������� ������, �������������� urllib, � ���� ���������� ���������� �� ����, �������������� requests.


# ��������� HTTP-������ � ������������� urllib �� requests
# URL ��� ������
# �� ������ ��������������� ����� JSONPlaceholder ��� ��������� ��������� ������:
#
# GET ����� ��� ��������� ��� �����.
# GET ����� ��� ��������� ������ �����.
# POST ����� ��� ��������� ������ �����.
# PUT ����� ��� ��������� ��������� �����.
# DELETE ����� ��� ��������� �����.
# ��������� ������ � ������������� urllib

import urllib.request
import urllib.parse
import json

# 1. GET ����� ��� ��������� ��� �����
url = 'https://jsonplaceholder.typicode.com/posts'
response = urllib.request.urlopen(url)
data = response.read()
posts = json.loads(data)
print("GET �� �����:", posts)

# 2. GET ����� ��� ��������� ������ �����
post_id = 1
url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
response = urllib.request.urlopen(url)
data = response.read()
post = json.loads(data)
print(f"GET ���� {post_id}:", post)

# 3. POST ����� ��� ��������� ������ �����
url = 'https://jsonplaceholder.typicode.com/posts'
data = json.dumps({
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}).encode('utf-8')
headers = {'Content-Type': 'application/json'}
req = urllib.request.Request(url, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(req)
new_post = json.loads(response.read())
print("POST ����� ����:", new_post)

# 4. PUT ����� ��� ��������� ��������� �����
post_id = 1
url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
data = json.dumps({
    'id': post_id,
    'title': 'foo_updated',
    'body': 'bar_updated',
    'userId': 1
}).encode('utf-8')
headers = {'Content-Type': 'application/json'}
req = urllib.request.Request(url, data=data, headers=headers, method='PUT')
response = urllib.request.urlopen(req)
updated_post = json.loads(response.read())
print(f"PUT ��������� ���� {post_id}:", updated_post)

# 5. DELETE ����� ��� ��������� �����
post_id = 1
url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
req = urllib.request.Request(url, method='DELETE')
response = urllib.request.urlopen(req)
print(f"DELETE ���� {post_id}:", response.status)


# ��������� ������ � ������������� requests

import requests

# 1. GET ����� ��� ��������� ��� �����
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
posts = response.json()
print("GET �� �����:", posts)

# 2. GET ����� ��� ��������� ������ �����
post_id = 1
url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
response = requests.get(url)
post = response.json()
print(f"GET ���� {post_id}:", post)

# 3. POST ����� ��� ��������� ������ �����
url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response = requests.post(url, json=data)
new_post = response.json()
print("POST ����� ����:", new_post)

# 4. PUT ����� ��� ��������� ��������� �����
post_id = 1
url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
data = {
    'id': post_id,
    'title': 'foo_updated',
    'body': 'bar_updated',
    'userId': 1
}
response = requests.put(url, json=data)
updated_post = response.json()
print(f"PUT ��������� ���� {post_id}:", updated_post)

# 5. DELETE ����� ��� ��������� �����
post_id = 1
url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
response = requests.delete(url)
print(f"DELETE ���� {post_id}:", response.status_code)

# ��������� urllib �� requests
# �������� ������������:
#
# requests ������ ������ ��������� � ������� HTTP-������.
# urllib ������� ����� ���� ��� ��������� ���������� �������, �������� ��� POST �� PUT ������.

# ������� JSON:

# requests �� ��������� �������� ��� ������� JSON (����� json()).
# � urllib ������� ������ ���������� JSON � ������������� �������� json.

# ��������� ���������:

# � requests ��������� ��������� ���� ������ ����� �������� headers.
# � urllib ������� ��������������� ��'��� Request � ���� �������� ���������.

# ������ ������:

# requests ������� �� HTTP ������ (GET, POST, PUT, DELETE) ����� ������� �������.
# � urllib ������ POST, PUT �� DELETE ���������� ��������� ��'���� Request � ������ ���������� ������.

# ���:

# requests ������� ���, �� �������� �������� ���� �� ���� ���������� �� �������� (����� requests.Session).
# � urllib ������� ���� �������� ������ �� ������ ��������� ����.