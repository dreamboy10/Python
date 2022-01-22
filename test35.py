import os

def read_folder(path):
	output = os.listdir(path)

	for item in output:
		if os.path.isdir(item):
			read_folder(item)
		else:
			print("파일:", item)

read_folder(".")
