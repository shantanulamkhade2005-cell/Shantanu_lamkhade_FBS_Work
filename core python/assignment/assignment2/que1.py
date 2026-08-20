hours=int(input("enter the time in hours:"))
minutes=int(input("enter the time in minutes:"))
seconds=int(input("enter the time in seconds:"))
h=hours*3600
m=minutes*60
total_seconds=h+m+seconds
print(f'total time in seconds is {total_seconds}')
