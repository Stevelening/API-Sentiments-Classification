#Install Libraries
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import traceback
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer

import re

app = Flask(__name__)
CORS(app)

@app.route('/prediction', methods=['GET'])
#define function

def predict():
    def tokenize_text(text):
        token = RegexpTokenizer(r'[a-zA-Z0-9]+')
        return cv.transform([text])
    def sentiment(rw):
        if (rw == '[1]'):
            return 'Positif'
        elif (rw == '[0]'):
            return 'Negatif'
        else :
            return 'aucun'
    def pourcentage(liste, rw):
        if (rw == '[1]'):
            return str(round(liste[0][1]*100,3))+' %'
        elif (rw == '[0]'):
            return str(round(liste[0][0]*100,3))+' %'
    if MNB:
        try:
            json_ = request.args.get('text')
            print(json_)
            #json_ = request.json
            text = str(json_) # on convertit le commentaire en chaine de caracteres
            # We tokenize the text
            t_text = tokenize_text(text)
            # We predict
            predict = list(MNB.predict(t_text))
            print('\n Cet enonce traduit un sentiment : "'+sentiment(str(predict))+'" a "'+pourcentage(MNB.predict_proba(t_text), str(predict))+'"\n')
            return jsonify({'prediction': str(predict), 'sentiment':sentiment(str(predict)), 'pourcentage':pourcentage(MNB.predict_proba(t_text), str(predict))})
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Model not good')
        return ('Model is not good')
if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except:
        port = 12345 
    MNB = joblib.load("machineLearningClassification.pkl") 
    print ('Model loaded')
    cv = joblib.load("mycv.pkl") # Load my "cv"
    print ('cv loaded')
    application.run(port=port, debug=True)