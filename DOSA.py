'''
create_model is a program that allows users to select either a model file 
or an annotated dataset and find similar data on the Blackfynn 
SPARC portal
Author: Karl G. Helmer
Institution: Massachusetts General Hospital
Date: 2018-12-06/07

Note that renaming of a model in Blackfynn app only renames the 
display name, but the internal name stays the same.
Thomas Jefferson - experiment = animal
Mount Sinai - experiment = mount_sinai
Northwell - experiment = experiment
'''

import json, sys
from blackfynn import Blackfynn
from blackfynn import Collection
from utils import select_file

modelNames = ['animal', 'mount_sinai', 'experiment']

localTermsFile = select_file()
with open(localTermsFile, 'r') as t:
    local = t.readlines()
    cleanLocal = [k.strip() for k in local]

# query blackfynn portal for properties
# set the blackfynn object to a specific organization ('SPARC Consortium')
# real way to do this is by adding these to your .blackfynn file 
# creating different profiles, one for each 
bf = Blackfynn(api_token='d95c0f4c-14f5-429c-afc0-7717fdcbb0be', api_secret='272db78d-b566-4274-aac3-de0d657a2556')

# find the datasets in bf Object and list them so the user can select one
datasets = bf.datasets()

propsDict = {}

print '\n'
print 'Datasets on SPARC Consortium:'
for d in datasets:
    ds = bf.get_dataset(d)
    dsModels = ds.models()

    print ds.id
    if dsModels:
        for m in dsModels:
            if m in modelNames:
                model = ds.get_model(m)
                # the keys of the schema are the properties, returns a list
                propsList = model.schema.keys()
                propsDict[ds.id] = propsList

#print propsDict
print '\n'
# now compare the models between the local file and the models of each dataset
numLocal = float(len(cleanLocal))
temp = {}

print "Overlap percentage with relevant datasets:"

#now figure out the overlap between the terms in the selected file
# and the terms in the relevant model files and print
for key in propsDict.keys():
    counter = 0
    for c in cleanLocal:
        val = propsDict[key]
        cl = c.lower()
        if cl in val:
            counter += 1 
    temp[key] = 100.0*float(counter)/numLocal

    print 'dataset ID = ', key
    print 'percent model overlap =', temp[key]
    print '\n'
