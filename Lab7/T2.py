# ------------------------------------------
# imports
# ------------------------------------------
import pandas as pd
import numpy as np
import spacy
import os

# NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

# open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

# ------------------------------------------
# demo
# ------------------------------------------
demo_array = np.zeros((2, 5))

# ------------------------------------------
# main
# ------------------------------------------
# load spacy model
nlp = spacy.load("en_core_web_md")

# load dataset
# pandas.read_csv() : Read a comma-separated values (csv) file into DataFrame
currentFolder = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
data = pd.read_csv(os.path.join(currentFolder, "lab7_atis_data.csv"))

# Calculate how many sentences in total
n_sentences = len(data["sentences"])

# Calculate the dimensionality of word vectors
embedding_dim = nlp.vocab.vectors_length

# Initialize the array with zeros: X
# numpy.zeros() : Return a new array of given shape and type, filled with zeros.
X = np.zeros((n_sentences, embedding_dim))

# Iterate over the sentences
print(data["sentences"])

for idx, sentence in enumerate(data["sentences"]):
    # Pass each each sentence to the nlp object to create a document
    doc = nlp(sentence)

    # Save the document's .vector attribute to the corresponding row in X
    X[idx, :] = doc.vector

print("End of program")

# Get a cell value
# data.at[0, "sentences"]


# spacy doc
# A Doc is a sequence of Token objects. Access sentences and named entities, export annotations to numpy arrays, losslessly serialize to compressed binary strings.

# ------------------------------------------
# Install Spacy
# ------------------------------------------
# pip install -U pip setuptools wheel
# pip install -U spacy

# python -m spacy download en_core_web_md

# lab7_atis_data.csv


# ------------------------------------------
# to install python virtual environment in Conda
# ------------------------------------------
# conda create --name aihi python=3.10
# conda activate aihi
# (aihi) C:\Users\user\your_own_folder>   <--- to check if you are in the virtual environment, you should see (aihi) in the command prompt

# pip install pandas
# pip install numpy
# pip install pip setuptools wheel
# pip install spacy
# python -m spacy download en_core_web_md