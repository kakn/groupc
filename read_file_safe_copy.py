# Reading the file

import csv
import re
import langid
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

def main(): 
	blogdict = read_file("sample.csv")
	#Looping through each blog text to the "text" key, and then tokenize, stemming and removing stopwords in the text.
	for i in range(0,len(blogdict["id"])):
		blogdict["text"][i] = stem_and_remove_stopwords_Sentence(blogdict["text"][i])
	
	Freq_list=[]

	for i in blogdict["text"]: 
		Freq_list.append(word_tokenize(i))
	print(Freq_list[0:3])
	print(FreqDist(Freq_list).most_common(10))
def gender_features(word):
	#Takes a text and then checks which of the unigrams we got form our freq distribution, are present in the blog post.
	#
	return {'last_letter': word[-1]}
gender_features('Shrek')


if __name__=='__main__':
	main()





