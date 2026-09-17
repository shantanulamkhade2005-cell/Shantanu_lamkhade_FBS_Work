def student(n):
    print(f'student {n}')
    marks=0
    for j in range(1,6):
        marks=int(input('enter the mark of subject'))
    print(marks)
    if(n==3):
        return 0
    student(n+1)
student(n=1)

    

