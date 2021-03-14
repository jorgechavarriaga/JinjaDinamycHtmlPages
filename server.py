"""
*************************************************************************
*    Course: 100 Days of Code - Dra. Angela Yu                          *
*    Author: Jorge Chavarriaga                                          *
*    Day: 57- Jinja Donamic Html Pages                                  *
*    Date: 2021-01-20                                                   *
*************************************************************************
"""

from flask import Flask, render_template
import random
from datetime import date
import requests



app = Flask(__name__)


@app.route('/')
def game():
    actual_year = date.today().year
    random_number = random.randint(1,10)
    return render_template("index.html", num=random_number, year=actual_year )


@app.route('/guess/<name>')
def my_guess(name):
    url = "https://api.agify.io/?name="
    data = requests.get(url + name).json()
    name_data = data['name']
    age_data = data['age']
    url2 = "https://api.genderize.io/?name="
    data2 = requests.get(url2 + name).json()
    gender_data = data2['gender']
    print(age_data == None)
    if age_data == None :
        return render_template("error.html", name=name_data)
    return render_template("guess.html", name=name_data, age=age_data, gender=gender_data)


@app.route('/blog/<num1>')
def get_blog(num1):
    blog_url = 'https://api.npoint.io/5abcca6f4e39b4955965'
    response = requests.get(blog_url)
    all_posts = response.json()
    total_posts = len(all_posts)
    return render_template("blog.html", posts=all_posts, total_posts=total_posts)


if __name__ == "__main__":
    app.run(debug=True, port=8080 )