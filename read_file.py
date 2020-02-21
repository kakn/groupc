# Reading the file

import csv
import re
import langid
from langid.langid import LanguageIdentifier, model
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer 
from nltk.stem import LancasterStemmer
from nltk.corpus import stopwords 
porter=PorterStemmer()

def read_file(file):
	# Creates a header (for keys) and a dictionary

	header = ["id", "gender", "age", "topic", "sign", "date", "text"]
	blogdict = {}
	for element in header:
		blogdict[element] = []


	# Creates an empty list to append each row in our data

	lines = []

	# Opens our data and appends each row to the empty list

	with open(file,'r') as f:
		for idx, row in enumerate(csv.reader((line.replace('\0','') for line in f), delimiter=",")):
	        # a row is a list containing all elements in a line

			# RegEx to remove every symbol that isn't a letter or number
			s = row[6]
			s = re.sub("[^\w\d'\s\\t]+", " ", s)
			row[6] = s

			#adds each row to the list
			lines.append(row)

	# Adds the data from each line to the dictionary with corresponding keys

	# Initiates a langid instance that normalizes the probabilities of language identification
	identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)

	for line in lines[0:500]:
		if identifier.classify(line[6])[0] and identifier.classify(line[6])[1] > 0.5:
			blogdict["id"].append(line[0])
			blogdict["gender"].append(line[1])
			blogdict["age"].append(line[2])
			blogdict["topic"].append(line[3])
			blogdict["sign"].append(line[4])
			blogdict["date"].append(line[5])
			blogdict["text"].append(line[6])
	return blogdict

def stem_and_remove_stopwords_Sentence(sentence):
    #Tokenizes the input
    token_words=word_tokenize(sentence)
    token_words
    stop_words = set(stopwords.words('english')) 

    stem_sentence=[]
    for word in token_words:
    	if not word in stop_words:
    		stem_sentence.append(porter.stem(word))
    		stem_sentence.append(" ")
    return "".join(stem_sentence)

def main(): 
	blogdict = read_file("sample.csv")
	for i in range(0,len(blogdict["id"])):
		blogdict["text"][i] = stem_and_remove_stopwords_Sentence(blogdict["text"][i])
	print("\n",blogdict["text"][9:11])

if __name__=='__main__':
	main()





