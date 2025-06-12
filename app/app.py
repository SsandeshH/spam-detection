import string
import pandas as pd
from nltk.corpus import stopwords
import joblib
from flask import Flask,render_template,request
app = Flask(__name__)

def preprocess(text):
    text= text.lower() #lowercasin
    text = text.translate(str.maketrans('', '', string.punctuation)) 

    stopwords_en = stopwords.words("english")
    words = text.split() #tokenization
    filtered_words = [word for word in words if word not in stopwords_en]  # Remove stopwords
    
    vectorizer = joblib.load('/home/san/Desktop/spam-detection/models/vectorizer.pkl')
    text_input = ' '.join(filtered_words)

    vector = vectorizer.transform([text_input])
    return vector


def predict(processed_text):
    model = joblib.load('/home/san/Desktop/spam-detection/models/spam_classifier.pkl')
    prediction = model.predict(processed_text)
    return "Spam" if prediction[0] == 1 else "Ham"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods = ['POST'])
def submit():
    result = ''
    if request.method == 'POST':
        text = request.form.get('text')
        processed_text = preprocess(text)
        result = predict(processed_text)
        return(render_template('index.html',result = result))


if __name__ == "__main__":
    app.run(debug=True)