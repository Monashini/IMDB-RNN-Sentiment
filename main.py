import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model

#load the imbd dataset word index
word_index=imdb.get_word_index()
reverse_word_index={value:key for key,value in word_index.items()}

#load the model
model = load_model('simple_rnn_imdb.h5')

#🔁 Decode Function (int → words)
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i, '?') for i in encoded_review])
    
#🧼 Preprocess Function (text → padded sequence)
def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [1] + [word_index.get(word, 2) for word in words]  # 1 = <START>, 2 = <UNK>
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

##prediction function
def predict_sentiment(review):
    preprocessedinput=preprocess_text(review)
    prediction=model.predict(preprocessedinput)
    sentiment='Positive' if prediction[0][0] > 0.5 else 'Negative'
    return sentiment, prediction[0][0]


import streamlit as st

# Streamlit UI
st.set_page_config(page_title="🎬 IMDB Sentiment Predictor", layout="centered")

st.title("🎬 Movie Review Sentiment Analysis")
st.markdown("Enter a movie review below and let the RNN predict whether it's **Positive** or **Negative**!")

# User input
user_review = st.text_area("📝 Enter your review here:")

# Predict button
if st.button("🔍 Predict"):
    if user_review.strip() == "":
        st.warning("Please enter a review to analyze.")
    else:
        sentiment, score = predict_sentiment(user_review)
        
        # Display results
        st.subheader("📊 Prediction Result")
        st.write(f"**Sentiment:** `{sentiment}`")
        st.write(f"**Confidence Score:** `{score:.4f}`")

        # Optional: Show colored emoji label
        if sentiment == "Positive":
            st.success("🌟 This review is likely **positive**.")
        else:
            st.error("⚠️ This review is likely **negative**.")
















