# Bayes

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
	
#def labeling(feature, label):
#	for 
#	labeled_data = [(feature
	
# Creates a list with set pairs of (features, label) with each text and gender in the dict
featuresets = [(find_features(n), gender) for (n, gender) in (blogdict["text"], blogdict["gender"])]

# Creates a training set with 70% of the featureset data
training_set = featuresets[:round(len(featuresets)*0.7)]

# Creates a dev and a test set with each 50% of the rest of the featureset data
# (corresponding to 15% of the total)
temp_set = featuresets[round(len(featuresets)*0.7):]

dev_set = temp_set[:round(len(temp_set)/2)]
test_set = temp_set[round(len(temp_set)/2):]