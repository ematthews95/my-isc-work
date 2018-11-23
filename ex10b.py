band = ['mel', 'geri', 'victoria', 'mel', 'emma']
counts = {}
for name in band:
	if name not in counts:
		counts[name] = 1
	else: 
		counts[name] = counts[name] + 1
		# count[name] += 1 

for name in counts:
	print(name)
	
	
