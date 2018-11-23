import numpy.ma as MA 
a = MA.masked_array(data=range(10), fill_value = -999)
print(a, a.fill_value)
a[2] = MA.masked
print(a)
print(a.mask)

b=[]
b = MA.where(a<7)
print(b) 
print(b.fill_value)

