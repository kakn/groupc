# Reading the file

import csv
import re
import langid
from langid.langid import LanguageIdentifier, model

# Creates a header (for keys) and a dictionary

header = ["id", "gender", "age", "topic", "sign", "date", "text"]
blogdict = {}
for element in header:
	blogdict[element] = []
	
	
# Creates an empty list to append each row in our data

lines = []

# Opens our data and appends each row to the empty list

with open("sample.csv",'r') as f:
	for idx, row in enumerate(csv.reader((line.replace('\0','') for line in f), delimiter=",")):
        # a row is a list containing all elements in a line
		
		# RegEx to remove every symbol that isn't a letter or number
		s = row[6]
		s = re.sub('\W+', " ", s)
		row[6] = s
		print(row[6])
		
		lines.append(row)
		
		if idx == 100:
			break
		
# Adds the data from each line to the dictionary with corresponding keys

# Initiates a langid instance that normalizes the probabilities of language identification
identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)

for line in lines:
	if identifier.classify[0](line[6]) and langid[1](line[6]) > 0.5:
		blogdict["id"].append(line[0])
		blogdict["gender"].append(line[1])
		blogdict["age"].append(line[2])
		blogdict["topic"].append(line[3])
		blogdict["sign"].append(line[4])
		blogdict["date"].append(line[5])
		blogdict["text"].append(line[6])
	
print("prut")
