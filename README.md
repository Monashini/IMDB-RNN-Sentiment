

````markdown
## 🔧 Work Done

This project was built from scratch using the IMDB movie reviews dataset provided by Keras. Here's an overview of all the steps involved:

---

### 📥 1. Load Dataset
- Used Keras' `imdb.load_data()` to load 25,000 training and 25,000 test reviews.
- Each review is a sequence of integers (word indices).

---

### 🔤 2. Word Index Preparation
- Loaded word-index mapping via `imdb.get_word_index()`.
- Created a `reverse_word_index` dictionary to decode integer sequences back into words.
- Reserved:
  - `0` for padding  
  - `1` for start  
  - `2` for unknown words

---

### 🧼 3. Preprocessing
- Defined a `preprocess_text()` function:
  - Converts user text to lowercase
  - Tokenizes into word indices
  - Adds start token (`1`)
  - Unknown words mapped to `2`
  - Final sequence padded to 500 words using `sequence.pad_sequences()`

---

### 🏗 4. Model Architecture
Used `Sequential()` model with:

- `Embedding(10000, 128, input_length=500)`  
  → Transforms word indices into dense 128-d vectors  
- `SimpleRNN(128)`  
  → Learns temporal dependencies  
- `Dense(1, activation='sigmoid')`  
  → Outputs sentiment (positive/negative)

---

### 🎯 5. Compilation

```python
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
````

---

### 🧪 6. Training

* Trained on padded reviews
* Used `validation_split=0.2` to evaluate on unseen data
* Added `EarlyStopping` callback with:

  * `monitor='val_loss'`
  * `patience=5`
  * `restore_best_weights=True`

---

### 💾 7. Model Saving

* Saved trained model as `simple_rnn_imdb.h5` for future use

---

### 📊 8. Prediction Functions

* `decode_review(encoded)` → Converts numeric review back to text
* `predict_sentiment(text)` → Predicts sentiment from raw user input (positive or negative)

---

### 🌐 9. Streamlit Deployment

* Built an interactive UI using Streamlit:

  * User types a review
  * Model predicts and displays sentiment
* Added `requirements.txt` for deployment
* Uploaded to GitHub and deployed on Streamlit Cloud

---

## 👩‍💻 Author

**Monashini S**
GitHub: [@Monashini](https://github.com/Monashini)

```

```
