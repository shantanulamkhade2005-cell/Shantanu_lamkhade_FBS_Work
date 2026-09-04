for i in range(1,5):
    for j in range(1,5-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        if(j==4):
            print(j,end=" ")
    print()