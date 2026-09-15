p1=int(input('enter the cost of product 1'))
p2=int(input('enter the cost of product 2'))
p3=int(input('enter the cost of product 3'))
p4=int(input('enter the cost of product 4'))
p5=int(input('enter the cost of product 5'))
total=p1+p2+p3+p4+p5
if(total>=1000):
    total*=0.82
    print('total after adding the gst=',total)
else:
    print('total=',toatl)