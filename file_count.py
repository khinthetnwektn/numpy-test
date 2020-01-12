from os import listdir, path

filePath = "../test"
files = listdir(filePath)
totalCsv = 0

def countCsv(folder):
	count = 0
	for file in folder:
		if file.endswith('.csv'):
			count +=1
	return count

for file in files:
	if path.isdir(path.join(filePath, file)):
		subFolder = listdir(path.join(filePath, file))
		totalCsv += countCsv(subFolder)
	elif file.endswith('.csv'):
		totalCsv +=1		

print("CSV File Count: {} files".format(totalCsv))
