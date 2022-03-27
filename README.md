# Nepustil RDNS API
Python API um PTR DNS Records für IP Adressen eines Subnetz zu setzen.

## Usage
In der `main.py` die Variablen User und Passwort setzen.
```python
BASE_URL="https://dnsadm.nepustil.net/index.cgi"
user=""
password=""
```

Zum Import der Library:
```python
from nepustil_dns_api import existsRecord, removeRecord, addRecord, getRecords

# Check if Record Exists
if(existsRecord("111")):
    # Remove Record if Exists
    removeRecord("111")
# Add Record
addRecord("test.de", "111")
# Print all Records
print(getRecords())
```