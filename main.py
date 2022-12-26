from flask import Flask, render_template, request
from counting_time import counting_time

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        date_input = request.form['date_input']
        data = counting_time(date_input)
        return render_template('index.html', data = data, date_input=date_input)
    return render_template('index.html')