#!flask/bin/python

#Imports for modelling and deployment
import os
from flask import Flask
from flask import request,jsonify
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import *
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
import pickle

# read the data
df = pd.read_csv('/data/spam.csv', encoding='ISO-8859-1')

# data preprocessing
df.drop(columns=['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True)
df.rename({'v1': 'label', 'v2': 'messages'}, axis=1, inplace=True)

# making Features and Target
X = df['messages']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.1,
                                                    random_state=2020)

# make a pipeline
text_clf = Pipeline([('tfidf', TfidfVectorizer()), ('clf', LinearSVC())])

# fir the data to pipeline
text_clf.fit(X_train, y_train)

#pickle the file for predicitons
filename = 'spam_classification_pipeline.pkl'
pickle.dump(text_clf, open(filename, 'wb'))

app = Flask(__name__)

# to verify if server is up and running
@app.route('/isAlive')
def index():
    return "Yes!! server is running"

# the actual api to give the results
@app.route('/predict', methods=['POST'])
def get_prediction():
    # Works only for a single sample
    data = request.get_json(force=True)  # Get data posted as a json
    predict_request = [data['msg']]
    model = pickle.load(open('spam_classification_pipeline.pkl', 'rb'))
    prediction = model.predict(predict_request)  # runs globally loaded model on the data
    # Take the first value of prediction
    output = prediction[0]
    return jsonify(output)


if __name__ == '__main__':
    if os.environ['ENVIRONMENT'] == 'production':
        app.run(port=80, debug=True)