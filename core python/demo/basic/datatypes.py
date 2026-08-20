#numeric 
#1 int 
var=10
print(type(var))
#2 float
var=3.14
print(type(var))
#3.complex
var=2+3j # complex contain numeric +imaganery values
print(type(var))
#### text
#1.str
var='this is single quout'
var="this is double quout"
var='''this isn mulitiy line text
first line
second line'''
var="""this isn mulitiy line text
first line
second line"""
print(type(var))

####sequential
 #1.list
var=[10,20,30,40]
print(type(var))
#2.tuple
var=(10,20,30,40)
print(type(var))
#3.range
var=range(1,100)
print(type(var))

####set type
#1.set
var={10,20,30,40}
print(type(var))
#2.frozenset
var=frozenset({10,20,30,40})
print(type(var))


####Mapping
#1.dict
var={1:'python',2:'java',3:'c'}
print(var)
print(type(var))


####other
#1.bool
var=True
print(type(var))
#2.Nonetype
var=None
print(type(var))
