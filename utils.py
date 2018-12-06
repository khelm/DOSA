'''
This file is a set of utility functions used in the DOSA project.

Author: Karl G. Helmer
Institution: Massachusetts General Hospital
Date: 2018-12-06
'''
import json
from pprint import pprint
from Tkinter import Tk
from tkinter.filedialog import askopenfilename


#This function reads a json model file and returns a json object.
#The JSON dict is the only thing in the file.
def read_json(fileName):

    with open(fileName) as f:
        data = f.json_load(f)
        pprint(data)

    return data


#This function reads a set of annotation terms from a file
#The file is in the format one term per line.
def read_terms(termFileName):

    with open(termFileName, 'r') as t:
        terms = t.readlines()
        cleanTerms = [term.strip() for term in terms]

    return cleanTerms


def select_file():
    Tk().withdraw() # don't want a full GUI, keep the root window from appearing
    filename = askopenfilename() # show "Open" dialog box; return path to file
    print(filename)

    return filename


