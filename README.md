
**Work Done**

This project was built from scratch using the IMDB movie reviews dataset provided by Keras. Here's an overview of all the steps involved:

**1. Load Dataset**

* Used Keras' `imdb.load_data()` to load 25,000 training and 25,000 test reviews.
* Each review is a sequence of integers (word indices).

**2. Word Index Preparation**

* Loaded word-index mapping via `imdb.get_word_index()`.
* Created a `reverse_word_index` dictionary to decode integer sequences back into words.
* Reserved:

  * 0 for padding
  * 1 for start
  * 2 for unknown words

**3. Preprocessing**

* Defined a `preprocess_text()` function that:

  * Converts user text to lowercase
  * Tokenizes it into word indices
  * Adds start token (1)
  * Maps unknown words to 2
  * Pads the sequence to 500 words using `sequence.pad_sequences()`

**4. Model Architecture**

* Built a Sequential model with the following layers:

  * `Embedding(10000, 128, input_length=500)` to turn word indices into dense 128-dimensional vectors
  * `SimpleRNN(128)` to learn temporal patterns
  * `Dense(1, activation='sigmoid')` to predict the sentiment score

**5. Compilation**
Used the following settings:
`model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])`

**6. Training**

* Trained the model on the padded review data
* Used `validation_split=0.2` to evaluate on unseen validation data
* Added early stopping with:

  * monitor set to `'val_loss'`
  * patience of 5
  * restoring best weights

**7. Model Saving**

* Saved the trained model as `simple_rnn_imdb.h5` for future inference use

**8. Prediction Functions**

* `decode_review(encoded)` function to convert numeric input back to text
* `predict_sentiment(text)` function to predict whether a user review is positive or negative

**9. Streamlit Deployment**

* Built a simple Streamlit app for user interaction
* Users can enter a review in the text input field
* The model returns the predicted sentiment in real-time
* Created a `requirements.txt` for deployment
* Uploaded the project to GitHub and deployed it on Streamlit Cloud


##snapshot :


![App Screenshot](https://github.com/Monashini/IMDB-RNN-Sentiment/blob/main/Screenshot%202025-06-28%20at%203.57.46%20PM.png?raw=true)



**Author**

Monashini S
GitHub: [https://github.com/Monashini](https://github.com/Monashini)

---

