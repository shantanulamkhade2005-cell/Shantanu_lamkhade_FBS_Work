num=int(input('enter a number:'))
sum=0
while num>0:
    d=num%10
    print(f"digit: {d}")
    sum+=d
    num//=10
print(sum)