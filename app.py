from flask import Flask, render_template, request
import tensorflow as tf
import pickle
from keras_preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# Load pre-trained model and tokenizer
model = load_model('imdb_model (1).h5')
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Define maximum sequence length for padding
max_len = 80000  # Adjust based on your model's configuration

def classify_text(text):
    sequences = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequences, maxlen=max_len)
    prediction = model.predict(padded_sequence)[0]
    sentiment = 'Positive' if prediction[1] > 0.5 else 'Negative'
    return sentiment

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    text = request.form['text']
    sentiment = classify_text(text)
    return render_template('index.html', text=text, sentiment=sentiment)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=9095)
