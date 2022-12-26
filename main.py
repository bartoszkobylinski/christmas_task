from flask import Flask, render_template, request
import os
from counting_time import counting_time
from generate_image import create_images

OPENAI_APIKEY = os.environ.get('OPENAI_APIKEY','there were some problem with APIKEY')

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

@app.route("/images", methods=["GET", "POST"])
def images():
    if request.method == "POST":
        user_prompt = request.form.getlist('properties')
        user_prompt = f"Create Christmas image where you have {user_prompt[0]}, {user_prompt[1]} and {user_prompt[2]}"
        images = [image for image in create_images(OPENAI_APIKEY,user_prompt)]
        print(images)
        return render_template('images.html',user_prompt=user_prompt, images=images)
    return render_template('images.html')
