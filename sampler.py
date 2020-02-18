import random
import numpy as np
with open("sample.csv", "w") as out_file:
  with open("blogtext.csv", "r") as in_file:
  	#Reading the entire dataset in
  	l = in_file.readlines()
  	#Looping through an array of 68000 int, and using that to generate random indexes.
  	for i in np.random.randint(0,len(l),68000):
  		out_file.write(l[i])
