import os
import pymongo
import json
import requests
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
import numpy as np
import  os 


current_dir = os.path.dirname(os.path.realpath("__file__"))
repo_dir = os.path.dirname(current_dir)
MODEL_FILE = os.path.join(repo_dir,"models","lstm_1hl_1do_bs128_10epc.h5")

model = load_model(MODEL_FILE)

#client = pymongo.MongoClient(host= MONGO_HOST, port=MONGO_PORT)

def predict(seed_text, next_words, max_sequence_len):
    tokenizer = Tokenizer()

    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted = model.predict(token_list, verbose=0)

        predicted_ind = np.argmax(predicted, axis=1)
        output_word = ""
        for word,index in tokenizer.word_index.items():
            if index == predicted_ind:
                output_word = word
                break
        seed_text += " "+output_word
    return seed_text.title()



def response(status, title, data={}, error={}):
    return json.dumps({
        "status": status,
        "title": title,
        "error": error,
        "data": data
    })
