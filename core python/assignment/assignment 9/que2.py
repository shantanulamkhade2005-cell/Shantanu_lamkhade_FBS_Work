def armstrong(tem,num,count,sum=0):
        if tem==0:
            if num==sum:
                print("Number is Armstrong")
            else:
                print("Number is not armstrong ")
            return
        d=tem%10
        sum=sum+d**count
        armstrong(tem//10,num,count,sum)
num=int(input("enter the number "))
tem=num
count=len(str(num))
armstrong(tem,num,count)