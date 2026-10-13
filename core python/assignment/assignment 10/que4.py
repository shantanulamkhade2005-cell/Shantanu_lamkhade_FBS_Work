li=[10,40,50,84,60,90,80]
start=0
end=len(li)-1
while(start<end):
    li[start],li[end]=li[end],li[start]
    start+=1
    end-=1

print(li)


