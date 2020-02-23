# Feature extractor

# Creates a list of top 3000 common words in frequency distribution
word_features = list(fd.keys())[:3000]

# Inputs text and returns a dictionary with the commons words as keys, 
# and the values True/False if the common word appears in the text
def find_features(text):
	words = set(text)
	features = {}
	for w in word_features:
		features[w] = (w in words)

	return features
	