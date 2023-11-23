import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re
from unicodedata import normalize
import string

def preprocess_text(text):
    text = normalize('NFD',text).encode("ascii","ignore")
    text = text.decode("UTF-8")
    # convert to string
    text = str(text)
    # convert to lowercase
    text = text.lower()
    # remove punctuation
    text = text.translate(str.maketrans('','',string.punctuation))
    # remove non-printable chars from text
    re_print = re.compile('[^%s]'% re.escape(string.printable))
    text = re_print.sub('',text)
    # remove numbers
    text = re.sub(r'[\d]+','',text)
    # remove multiple spaces
    text = ' '.join(text.split())
    return text
    
def translation(input_sentence):
    with open('model.pkl', 'rb') as f:
        clf2 = pickle.load(f)

    with open('eng_tokenizer.pkl', 'rb') as f:
        eng_tokenizer = pickle.load(f)

    with open('max_length.pkl', 'rb') as f:
        max_length = pickle.load(f)

    with open('fr_tokenizer.pkl', 'rb') as f:
        fr_tokenizer = pickle.load(f)

    input_sentence = preprocess_text(str(input_sentence))
    input_seq = eng_tokenizer.texts_to_sequences([input_sentence])
    input_seq_final = pad_sequences(input_seq,maxlen=max_length,padding="post")
    prediction = clf2.predict([input_seq_final])
    output_translation = np.argmax(prediction,axis=-1)
    
    output_sentence = []
    for i in output_translation[0]:
        if i in fr_tokenizer.index_word:
            output_sentence.append(fr_tokenizer.index_word[i])
        else:
            output_sentence.append(' ')
    return ' '.join(output_sentence)


def app():
    st.subheader("Enter the String:")
    string = st.text_input("")

    st.write('')
    if st.button("Enter"):
        res = translation(string)
        st.write("Translated String:")
        st.markdown(f'<div style="background-color: #f0f0f0; padding: 10px;color:#000000;font-size:24px;">{res}</div>',
                    unsafe_allow_html=True)
