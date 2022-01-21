def flattern(data):
	output = []
	for item in data:
		if type(item) == list:
			output += flattern(item)
		else:
			output.append(item)
		return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본", example)
print("변환", flattern(example))
