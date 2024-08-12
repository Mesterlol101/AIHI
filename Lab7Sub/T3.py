# ------------------------------------------------------------
# imports
# ------------------------------------------------------------
from sklearn.svm import SVC
import numpy as np
import pandas as pd
import spacy
import os


from sklearn import metrics

# ------------------------------------------------------------
# installation
# ------------------------------------------------------------
# Install scikit-learn
# pip install -U scikit-learn


# ------------------------------------------------------------
# main
# ------------------------------------------------------------
# load spacy model
nlp = spacy.load("en_core_web_md")

# load dataset
currentFolder = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
data = pd.read_csv(os.path.join(currentFolder, "lab7_atis_data.csv"))

# Initialize the array with zeros: X
X_train = np.zeros((len(data["sentences"]), nlp.vocab.vectors_length))

# Iterate over the sentences
for idx, sentence in enumerate(data["sentences"]):
    X_train[idx, :] = nlp(sentence).vector

y_train = data["intents"]

clf = SVC()

# train the model using the sentence vectors... and their corresponding intents
# to teach the model how to predict an intent .. given any vector next time
clf.fit(X_train, y_train)

# Now, we feed in an input dataset of vectors to see the predictions.. (their corresponding predicted intents)
y_pred = clf.predict(X_train)

# Count the number of correct predictions
n_correct = 0
for i in range(len(y_train)):
    if y_pred[i] == y_train[i]:
        n_correct += 1

dataSize = len(y_train)

# Manual calculation of Accuracy
accuracy = n_correct / dataSize
print("Manual calculation of accuracy: {0}".format(accuracy))


print(
    "Predicted {0} correctly out of {1} test examples, accuracy {2}".format(
        n_correct, len(y_train), accuracy
    )
)

# Model Accuracy: how often is the classifier correct?
print("Metrics Accuracy:", metrics.accuracy_score(y_train, y_pred))