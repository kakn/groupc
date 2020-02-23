# Reading the file

import csv
import re
import langid
import random
from langid.langid import LanguageIdentifier, model
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer 
from nltk.stem import LancasterStemmer
from nltk.corpus import stopwords 
from nltk import FreqDist
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
    #Making a set of english stopwords from NLTK. Have added additional stopwords to
    #These being = 't, 's,'re, n't, 't, 've,"',",'m,','no,'ll,'well,'d
    stem_sentence=[]
    
    #Looping through the tokenized sentences and removing stopwords and stemming non stop words. 
    for word in token_words:
    	if not word in stop_words:
    		stem_sentence.append(porter.stem(word))
    		stem_sentence.append(" ")
    return "".join(stem_sentence)
	
def freq_model(blogdict):
	#First i takes all blogposts and tokenizes to a new list. 
	Freq_list=[]
	for i in range(0,len(blogdict["text"])): 
		Freq_list.append(word_tokenize(blogdict["text"][i]))
	#Then i transform the list of list to just a single list.
	flat_list = [item for sublist in Freq_list for item in sublist]
	#Where after i use the FreqDist on it. 
	FD=FreqDist(flat_list)
	return FD
	
# Feature extractor
# Inputs text and returns a dictionary with the commons words as keys, 
# and the values True/False if the common word appears in the text

def find_features(document, FD):
	# Creates a list of top 3000 common words in frequency distribution
	word_features = list(w[0] for w in FD.most_common(3000))
	
	words = set(document)
	features = {}
	for w in word_features:
		features[w] = (w in words)
	
	return features

def creating_sets(blogdict, FD):
	documents = [(text, gender)
	for gender in blogdict["gender"]
	for text in blogdict["text"]]
	random.shuffle(documents)
	
	print(documents[2])
	
	# Creates a list with set pairs of (features, label) with each text and gender in the dict
	"""featuresets = [(find_features(n, FD), gender)
	for gender in documents[1]
	for n in documents[0]]"""
	featuresets = [(find_features(n, FD), gender)
	for gender in blogdict["gender"]
	for n in blogdict["text"]]
	
	print(featuresets[2])

	# Creates a training set with 70% of the featureset data
	training_set = featuresets[:round(len(featuresets)*0.7)]

	# Creates a dev and a test set with each 50% of the rest of the featureset data
	# (corresponding to 15% of the total)
	temp_set = featuresets[round(len(featuresets)*0.7):]

	dev_set = temp_set[:round(len(temp_set)/2)]
	test_set = temp_set[round(len(temp_set)/2):]
	
	return training_set, dev_set, test_set

def main(): 
	blogdict = read_file("sample.csv")
	#Looping through each blog text to the "text" key, and then tokenize, stemming and removing stopwords in the text.
	for i in range(0,len(blogdict["id"])):
		blogdict["text"][i] = stem_and_remove_stopwords_Sentence(blogdict["text"][i])

	FD = freq_model(blogdict)
	
	# Creates sets of data by using find_features function
	creating_sets(blogdict, FD)


if __name__=='__main__':
	main()





