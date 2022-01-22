import os

output = os.listdir(".")
print("os.listdir():", output)
print()

print("# 폴더와 파일 구분하기")
for path in output:
	if os.path.isdir(path):
		print("폴더", path)
	else:
		print("파일", path)
