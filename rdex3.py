import netCDF4
ds = netCDF4.Dataset("ggas2014121200_00-18.nc")
for v in ds.variables: 
	print(v)
sst = ds.variables['SSTK']
print(sst) 

for x in sst.dimensions:
	print(x, len(x))
	
print(sst.shape, sst.size)
	
for attr in sst.ncattrs(): 
	print(attr, '=', getattr(sst, attr))
print('bishes love egencia')
