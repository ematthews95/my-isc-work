forward = list()
backward = list()
values = ["a", "b", "c"]
for item in values:
	forward.append((item))
	backward.insert(0, item)
print(forward)
print(backward)
forward.reverse()
print(forward)
if forward == backward:
	print("true")
else:
	print("you suck")
