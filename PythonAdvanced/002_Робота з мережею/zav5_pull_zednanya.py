# ������� ��������� �� ��������� ��������� ������������ pull �'������ � ���� ������. �������������� ������ ab,
# ����������� ���� ������������ (https://ru.wikipedia.org/wiki/ApacheBench).


# ab (ApacheBench) - �� ������ ���������� ����� ��� ���������� ������������� HTTP-�������. ���� �������� ��������� ������
# ������� ������ �� ���-������� � ��������� �������������, ��������� �������� ������ �� ������� ����������
# ������ �� �������.

# ������ ��������� ������ ab
# -n <requests>: ʳ������ ������, �� ������ �������.
# -c <concurrency>: ʳ������ ���������� ������.
# -t <timelimit>: ��������� �� ����� ����� � ��������.
# -k: ������������ �������� �'������ (Keep-Alive).
# -H <header>: ��������� ��������� �� ������.

# ������� ������������ ab

# sh

# ab -n 1000 -c 10 http://www.example.com/
# ��� ������� ������� 1000 ������ �� http://www.example.com/ � 10 ����������� �'���������.

# ������ pull �'������ �� ������������
# ��� ������������ pull �'������ ����� ��������������� �������� -k, ���� ������ ����� Keep-Alive. � ����� ����� ����
# TCP-�'������� ��������������� ��� ������ HTTP-������, �� ������ �������� � ������ �������������.

# ������������ ������ ab ��� ����� ������ �'������
# ��� Keep-Alive (���� ����� �� �'�������)

# sh

# ab -n 1000 -c 10 http://www.example.com/
# � Keep-Alive (������� ������ �� ���� �'�������)

# sh

# ab -n 1000 -c 10 -k http://www.example.com/
# ����� ���������� ab
# ϳ��� ��������� ����� ������ ab ������� ��������� ��� ��� ������������� �������, ���������:

# Time taken for tests: ���, ���������� �� ��������� ��� ������.
# Complete requests: �������� ������� ��������� ������.
# Failed requests: ʳ������ �������� ������.
# Requests per second: ʳ������ ������, ���������� �������� �� �������.
# Time per request: ������� ��� ������� ������ ������.
# Transfer rate: �������� �������� �����

# ������� ���������� ��������� ab

# sh


# This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
# Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
# Licensed to The Apache Software Foundation, http://www.apache.org/
#
# Benchmarking www.example.com (be patient)
# Completed 100 requests
# Completed 200 requests
# Completed 300 requests
# ...
#
# Finished 1000 requests
#
#
# Server Software:        Apache/2.4.41
# Server Hostname:        www.example.com
# Server Port:            80
#
# Document Path:          /
# Document Length:        234 bytes
#
# Concurrency Level:      10
# Time taken for tests:   2.345 seconds
# Complete requests:      1000
# Failed requests:        0
# Total transferred:      345000 bytes
# HTML transferred:       234000 bytes
# Requests per second:    426.82 [#/sec] (mean)
# Time per request:       23.45 [ms] (mean)
# Time per request:       2.35 [ms] (mean, across all concurrent requests)
# Transfer rate:          143.12 [Kbytes/sec] received
#
# Connection Times (ms)
#               min  mean[+/-sd] median   max
# Connect:        1    2   1.2      2      10
# Processing:     5   21   4.3     20      30
# Waiting:        4   19   4.5     18      28
# Total:          6   23   4.5     22      35
#
# Percentage of the requests served within a certain time (ms)
#   50%     22
#   66%     24
#   75%     26
#   80%     28
#   90%     32
#   95%     33
#   98%     34
#   99%     35
#  100%     35 (longest request)
# ֳ ��� ����������� ������� ������������� ������� �� ������� ��������� ��������, ��� �� ������ ���� ������ ���
# ������� �������� ������� ������.
