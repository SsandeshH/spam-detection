from flask import Flask,render_template,request
app = Flask(__name__)

def preprocess(text):
    return ''


def predict(processed_text):
    return ''

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