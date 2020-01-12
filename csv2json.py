from os import listdir, path
import json
import pandas as pd

filePath = "../test"
print("Files are there => ", filePath)
filelist = listdir(filePath)

def findCsv(folder, newPath):
	for file in folder:
		if file.endswith(".csv"):
			csv2json(file, newPath)			

def csv2json(name, newPath):
	csvName = path.join(newPath, name)
	jsonfile = path.join(newPath, name.replace(".csv", ".json"))
	
	# data frame from csv file
	data = pd.read_csv(csvName, names = ['x', 'y', 'width','height', 'tag'])
	dic = data.to_dict('index')

	newkey =[]
	newdict = []	
	for i,v in dic.items():
		data = {}
		if i < 10:
			newkey.append('record_0{}'.format(i+1))
		else:
			newkey.append('record_{}'.format(i+1))
		for p,val in v.items():
			data[p] = str(val)
		newdict.append(data)
	finaldict = dict(zip(newkey, newdict))

	with open(jsonfile, "w") as jf:
		json.dump(finaldict, jf, indent=4)

for file in filelist:
	if path.isdir(path.join(filePath, file)):
		newPath = path.join(filePath, file)
		subFolder = listdir(newPath)
		findCsv(subFolder, newPath)
	elif file.endswith('.csv'):
		csv2json(file, filePath)
