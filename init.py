from nepustil_dns_api import existsRecord, addRecord, getRecords

for i in range(1,255):
    # Check if Record Exists
    if(not existsRecord(str(i))):
        # Add Record if not Exists
        addRecord(str(i)+".210.236.85.cloud.meros.systems", str(i))
# Print all Records
print(getRecords())