# Chi-square test

# Libraries
import numpy as numpy
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import chi2

# Read the data

data = pd.read_csv('test_chi.csv')

print(data.head(10))

# Encoding data (because we need to input values to Chi-square method

label_encoder = LabelEncoder()
data['Geography'] = label_encoder.fit_transform(data['Geography'])
data['Gender'] = label_encoder.fit_transform(data['Gender'])

print(data.head(10))

# Choosing our X variable (features) and Y variable (label)

X = data.drop('Exited',axis=1)
y = data['Exited']

# Actual Chi-square test
chi_scores = chi2(X,y)


# Chi-scores
chi_stats, p_values = chi_scores

print(chi_stats)
print(p_values)







	
