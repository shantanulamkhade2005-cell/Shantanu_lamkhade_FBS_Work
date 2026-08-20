#input phase
p=int(input('enter the principal amount:'))
r=int(input('enter the rate of interest:'))
t=int(input('enter the time in years:'))
#perform operation
Compound_interest=p*(1+r/100)**t-p
#output phase
print('the compound interest is:',Compound_interest)