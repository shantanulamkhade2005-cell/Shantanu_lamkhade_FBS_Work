def pattern(n):
    for i in range(n):
        if(i==0 or i==n-1):
            print("*"*n)
        else:
            for j in range(n-1-i):
                print(' ',end="")
            print('*')

pattern(n=15)