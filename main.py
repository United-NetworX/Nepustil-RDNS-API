from contextlib import redirect_stderr
import requests
import re
from io import StringIO
import csv

BASE_URL="https://dnsadm.nepustil.net/index.cgi"
user=""
password=""

"""Get PTR Records"""
def getRecords():
    action="readzone"
    data = {
        'domain': user,
        'password': password,
        'action': action,
        'resrec': ''
    }
    request = requests.post(BASE_URL, data=data)
    read = False
    res = []
    for line in request.text.splitlines():
        if(line.startswith("254")):
            read=True
            continue
        if(read):
            list = re.sub("\s+", ",", line.strip())
            reader = csv.reader(list.split('\n'), delimiter=',')
            for row in reader:
                res.append(row)
    return res

"""Check if Record Exists"""
def existsRecord(ip):
    res = getRecords()
    for record in res:
        if(record[0] == ip):
            return True
    return False

"""Add PTR Record"""
def addRecord(domain, ip):
    action="doaddrr"
    data = {
        'domain': user,
        'password': password,
        'action': action,
        'resrec': ip,
        'restype': 'PTR',
        'resval': domain+".",
        'resttl': 86400
    }
    request = requests.post(BASE_URL, data=data)
    #print(request.text)

"""Remove PTR Record"""
def removeRecord(ip):
    res = getRecords()
    for record in res:
        if(record[0] == ip):
            domain = record[4]
    action="dodelrr"
    data = {
        'domain': user,
        'password': password,
        'action': action,
        'resrec': ip,
        'restype': 'PTR',
        'resval': domain,
        'resttl': 86400
    }
    request = requests.post(BASE_URL, data=data)

if(existsRecord("111")):
    removeRecord("111")
addRecord("test.de", "111")
print(getRecords())
