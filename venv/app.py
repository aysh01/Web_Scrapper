from flask import Flask
from flask import render_template, request as req, jsonify
import requests as reqq
from bs4 import BeautifulSoup

# pymongo
import pymongo
import pandas as pd

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['mydb']
collection = db['users']
collection1 = db['data']


@app.route('/')
def run():
    return render_template('index.html')


@app.route('/scrape', methods=['POST'])
def scrape():
    search = req.form['url']
    url = f"https://www.google.com/search?q={search}&sourceid=chrome-mobile&ie=UTF-8"
    response = reqq.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")
    search_results = soup.find_all("h3")

    result_titles = []
    result_titles = [result.get_text() for result in search_results]

    for result in search_results:
        if result.find("a"):
            continue  # "a"
        result_titles.append(result.get_text())

    search_input = search.split(",")

    try:
        collection.insert_one({'Search': search})
        print("Inserted into database successfully.")
    except Exception as e:
        print("An error occured")
    return render_template('results.html', search=search, url=url, result_titles=result_titles, search_input=search_input)


@app.route('/submit', methods=['POST'])
def submit():
    data = req.json['unique']

    for i in data:
        collection1.insert_one({'item': i})

    return jsonify({'message': 'Data submitted succesfully'})


if __name__ == '__main__':
    app.run(debug=True)
