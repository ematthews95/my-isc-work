def calc_hypo(a,b):
	if type(a) not in (int, float) or type(b) not in (int,float):
		print("bad arguement")
		return False 
	elif a <=0 or b <=0:
		print("bad arguement")
		return False 
	else:
		hypo = (a**2 + b**2)**0.5
		return hypo
	
print(calc_hypo('a',4))

