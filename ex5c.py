with open("weather.csv") as reader:
	line=reader.readline()
	print("first",line)
	rain=[]
	total = 0
	count = 0
	for line in reader.readlines():
		count += 1
		total += len(line) 
		print(line) 
rain = line.extract(

