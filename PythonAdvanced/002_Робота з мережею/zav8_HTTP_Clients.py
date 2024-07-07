# ������� HTTP-�볺���, ���� ���������� URL �������, ��� ������ �� ������� �� ����������� ��� (������������).
# ���������� ����� � ��������� ������� �� ��������� ������, ��������� ��� ��������� �������, �� ��������� �� �������
# ������-���, ��������� �� ��� ������.


# ��� ��������� HTTP-�볺���, ���� ������ URL �������, ��� ������ �� ������� � ������ (�����������), �����
# ����������� �������� requests.

import requests

def http_client(url, method, data=None):
    """
    ������ HTTP �����.

    :param url: URL �������
    :param method: ��� ������ (GET, POST, PUT, DELETE)
    :param data: ������� � ������ ��� �������� (�����������)
    """
    method = method.upper()

    try:
        if method == 'GET':
            response = requests.get(url, params=data)
        elif method == 'POST':
            response = requests.post(url, json=data)
        elif method == 'PUT':
            response = requests.put(url, json=data)
        elif method == 'DELETE':
            response = requests.delete(url, json=data)
        else:
            print("�������� ����� HTTP.")
            return

        print(f"������-���: {response.status_code}")
        print("���������:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
        print("\nҳ�� ������:")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"������� �������: {e}")

# ������� ������������
url = "https://jsonplaceholder.typicode.com/posts"
method = "POST"
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

http_client(url, method, data)


# ���������
# ������� http_client:
#
# ������ ��������� url, method �� data.
# ������� ����� ������ (GET, POST, PUT, DELETE) � ������ ��������� �����.
# �������� �������, �������� �� ������� ������-���, ��������� �� ��� ������.
# ��������� ������� ������� �� ��� ��������� ������, �������� �������� �����������.
# ������� ������������:
#
# ����������� ������� http_client ��� ����������� POST ������ �� ������ https://jsonplaceholder.typicode.com/posts
# � ��������� �����.
#
# ������
#
# �������� ��� � ����, ��������� http_client.py.
# �������� ���� �� ��������� Python:
#
# sh
#
#
# python http_client.py
# ��� �볺�� � ������� � ������� ������ ������ HTTP. �� ������ ��������������� ���� ��� ����������� ������ ��
# ��� ������� � ������ �������� �� ������.