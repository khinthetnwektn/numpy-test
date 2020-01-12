from os import listdir, path
from xml.etree.ElementTree import Element
from xml.dom import minidom
import xml, pandas as pd
import xml.etree.ElementTree as ET

filePath = "../test"
print("Files are there => ", filePath)
filelist = listdir(filePath)

def findCsv(folder, newPath):
	for file in folder:
		if file.endswith(".csv"):
			csv2xml(file, newPath)			

def csv2xml(name, newPath):
	csvName = path.join(newPath, name)
	xmlfile = path.join(newPath, name.replace(".csv", ".xml"))

	# data frame from csv file
	data = pd.read_csv(csvName, names = ['x', 'y', 'width','height', 'tag'])
	#to dictionary
	dic = data.to_dict('index')
	
	xml = Element('annotation')
	for i, d in data.iterrows():
		sub_element1 = Element('object')
		
		child = Element('tag')
		child.text = str(d['tag'])
		sub_element1.append(child)
		for f in d.index:
			sub_element2 = Element('bndbox')
			
			child1 = Element('x')
			child1.text = str(d['x'])
			sub_element2.append(child1)

			child2 = Element('y')
			child2.text = str(d['y'])
			sub_element2.append(child2)

			child3 = Element('width')
			child3.text = str(d['width'])
			sub_element2.append(child3)

			child4 = Element('height')
			child4.text = str(d['height'])
			sub_element2.append(child4)

		sub_element1.append(sub_element2)
		xml.append(sub_element1)
			
	xmltree = ET.ElementTree(xml)
	xmltree = minidom.parseString(ET.tostring(xmltree.getroot())).toprettyxml()
	xmltree = xmltree[23:-1]
	
	with open(xmlfile, "w") as file:
		file.write(xmltree)

for file in filelist:
	if path.isdir(path.join(filePath, file)):
		newPath = path.join(filePath, file)
		subFolder = listdir(newPath)
		findCsv(subFolder, newPath)
	elif file.endswith('.csv'):
		csv2xml(file, filePath)
