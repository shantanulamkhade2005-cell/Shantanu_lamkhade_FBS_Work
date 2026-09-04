n=int(input('enter the numbers of students:'))
for i in range(1,n+1):
    print(f'student{i}')
    science=int(input('enter the science mark:'))
    math=int(input('enter the math mark:'))
    history=int(input('enter the history mark:'))
    marathi=int(input('enter the marathi mark:'))
    english=int(input('enter the english mark:'))
    total=science+math+history+marathi+english
    percentage=(total/500)*100
    print(f'total marks of student{i} is {total}, percentage is {percentage}')
    if(percentage<=70):
        print(f'average student {i} with percentage {percentage}')