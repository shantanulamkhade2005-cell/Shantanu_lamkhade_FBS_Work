cost=int(input('enter the cost of product'))
sell=int(input('enter selling price'))
if(cost<=sell):
    c=sell-cost
    print(f'product make an {c} profit')
else:
    d=cost-sell
    print(f'product make {d} loss')