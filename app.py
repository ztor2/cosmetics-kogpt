from flask import Flask, render_template, request, flash
from transformers import pipeline
from utils import *

app = Flask(__name__)
app.secret_key = '1234'


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def generate_text():
    keyword = request.form['keyword']
    if len(keyword) == 0:
        flash('1글자 이상의 키워드를 입력해주세요.')
        return render_template('index.html')
    length = int(request.form['length'])
    types = request.form['types']
    nums = int(request.form['nums'])
    temperature = 0.4 if types == 'strict' else 0.9
    textgen_option(temperature, length)
    generator = pipeline('text-generation', model='./model', tokenizer="./model/tokenizer")
    generated_text = review_generate(keyword, generator, nums)
    return render_template("index.html", generated_text=generated_text)


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host="127.0.0.1", port="5000", debug=True)
