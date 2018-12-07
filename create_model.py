'''
create_model is a program that allows users to select either a model file 
or an annotated dataset and find similar data on the Blackfynn 
SPARC portal
Author: Karl G. Helmer
Institution: Massachusetts General Hospital
Date: 2018-12-06
'''

import json, sys
from blackfynn import Blackfynn
from blackfynn import Collection
from Tkinter import Tk
from tkinter.filedialog import askopenfilename
from utils import select_file, read_terms, read_json


# select associated terms file
termsFilePath = select_file()

# open terms file and import relationships and classes
rels, clas = read_terms(termsFilePath)
print rels, clas

# query blackfynn portal for properties
# set the blackfynn object to a specific organization ('SPARC Consortium')
# real way to do this is by adding these to your .blackfynn file 
# creating different profiles, one for each 
bf = Blackfynn(api_token='d95c0f4c-14f5-429c-afc0-7717fdcbb0be', api_secret='272db78d-b566-4274-aac3-de0d657a2556')

# to get a list of the possible organizations - unused at the moment
#organizations = bf.organizations()

# find the datasets in bf Object and list them so the user can select one
datasets = bf.datasets()
x = 0
print '\n'  #new line for formatting
for d in datasets:
    x = x+1
    print x, d.name, d.id

print '\n'
whichData = input('Input the number of the project you want to create a model for: ')

try:
    ds = bf.get_dataset(datasets[int(whichData)-1])
except:
    print "Requested data set not available."

#create a model
try:
    model = ds.create_model('experiment')
except:
    print "Requested model not available"
    sys.exit()

# now add each term from the classes list as a new property in the model
for i, term in enumerate(clas):
    if i == 0:
        model.add_property(term, title=True)
    else:
        model.add_property(term)

# now add each relationship (which are owl datatype/object properties)
for r in rels:
    ds.create_relationship_type(r, 'none')

ds.update



