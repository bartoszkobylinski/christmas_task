from flask import Flask, render_template, request
from counting_time import counting_time

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        date_input = request.form['date_input']
        last_year = request.form['last_year']
        data = counting_time(date_input, last_year)
        return render_template('index.html', data = data, date_input=date_input, last_year=last_year)
    return render_template('index.html')