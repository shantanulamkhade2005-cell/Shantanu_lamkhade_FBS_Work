#1.Structure : []
li=[10,20,30,40,3.14,'abc']
print(type(li))

#2.Types of data :hetrogenous
  # different type sof datatypes
print(li)

#3. sequence: order 
   # not change in order


#4. changable: mutable
  #  change in orignal list without changing the order or address
print(id(li))
li[2]=50
print(li)
print(id(li))
#5. Duplication :allowed
  # Duplicat value is allowed
li=[10,10,20,30]
print(li)