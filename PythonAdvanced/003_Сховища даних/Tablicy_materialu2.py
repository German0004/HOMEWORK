# ��� ������� ��������� � �������� 4 ������� ����������������� ��������� �������, ��� ���� ������ �������� ���� ���
# �������� ������� ������ � �������� �������� �� ������.


import json
import math

def calculate_average_weight(file_path):
    # ������� ����� � �����
    with open(file_path, 'r') as file:
        data = json.load(file)

    # ��������, �� ��� �� ������
    if not data:
        return "No data available"

    # ���������� �������� ���� �� ������� ��������
    total_weight = 0
    count = 0

    for item in data:
        if 'weight' in item:
            total_weight += item['weight']
            count += 1

    # ��������, �� � ���� � ���� �������
    if count == 0:
        return "No valid weights found"

    # ���������� ���������� �������� ����
    average_weight = total_weight / count

    # ���������� �� ������
    return round(average_weight)

# ������ ������� �� ��������� ����������
file_path = 'materials.json'
average_weight = calculate_average_weight(file_path)
print(f"The average weight, rounded to the nearest integer, is: {average_weight}")


# ��������� ����:
# ������� �����: ³������ ���� materials.json � ��������� ���� ���� � ����� data.
# �������� �� ������ ���: ���� data �������, ������� ������� �������� �����������.
# ���������� �������� ���� �� �������: ����� �� ������� �������� � data, ������� �������� ���� �� total_weight �
# ������� ������� ������.
# ���������� ���������� ��������: ĳ���� �������� ���� �� ������� ��������.
# ���������� �� ������: ����������� ������� round() ��� ���������� ���������� �������� �� ����������� ������ �����.
