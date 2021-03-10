# import streamlit as st
from transformers import pipeline
import pandas as pd
import numpy as np

# importing for API
import uvicorn
from fastapi import FastAPI
from Scores import Score
import pickle

app = FastAPI()

sentimentanalyzer = pipeline("sentiment-analysis")

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}


@app.post('/predict')
def predict_score(data:Score):
    data = data.dict()
    message = data['sentence']
    result = sentimentanalyzer(message)[0]
    if(result['label'] == 'POSITIVE'):
        final_score = 35+35*float(result['score'])
    elif(result['label'] == 'NEGATIVE'):
        final_score = 35 - 35*float(result['score'])
    else:
        final_score = 0
    # print(final_score)

    # Based on influencer's tweet data ( removing tweets with less than 5 words)
    # Since the average lenth of tweet 99.7, variange = 32.46
    avg_len = 99.7
    var_len = 32.46
    len_score = (len(message)-avg_len)/var_len
    len_score = len_score/(avg_len/var_len)
    len_score = 30-30*abs(len_score)
    # print(len_score)

    total_score = len_score + final_score

    return {
        'prediction': total_score
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload

