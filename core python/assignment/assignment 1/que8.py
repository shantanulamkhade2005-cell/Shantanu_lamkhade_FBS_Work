day=int(input('enter the day:'))
year=day//365
week=(day%365)//7
days=(day%365)%7
print(f'the year is {year} and the week is {week} and the day is {days}')