#take an input from user
math=int(input('enter the marks in math:'))
science=int(input('enter the marks in science:'))
english=int(input('enter the marks in english:'))
marathi=int(input('enter the marks in marathi:'))
geography=int(input('enter the marks in geography:'))
#perform operation
total=math+science+english+marathi+geography
percentage=(total/500)*100
#display result
print('total marks obtained in 5 subjects is:',total)
print(f"total marks obtained in 5 subjects is {total} and percentage is {percentage}%")