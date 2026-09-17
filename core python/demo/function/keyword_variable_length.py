def emp(**data):
    print(type(data))
    for key,val in data.items():
        print(key,':',val)
emp(id=101,name='ABC',dept='It',sal=10000)