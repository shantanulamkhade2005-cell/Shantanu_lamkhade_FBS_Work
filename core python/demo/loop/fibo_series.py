num=int(input('enter the how many febonency no you want'))
a=-1
b=1
for i in range(num):
    c=a+b
    print(c ,end = ' ')# end is use for not exicte to next line without next line all on one line
    a=b
    b=c