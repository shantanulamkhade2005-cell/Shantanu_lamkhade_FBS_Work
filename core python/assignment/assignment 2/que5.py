cost=int(input('enter the cost of book:'))
discount=int(input('enter the discount for book:'))
d=discount/100
final=cost-(cost*d)
print(f'the cost of book after discount is:{final}')