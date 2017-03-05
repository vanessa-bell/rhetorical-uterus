from flask import Flask, render_template
from pymongo import MongoClient
from news import getNews

app = Flask(__name__)
mongo_object = MongoClient()
db = mongo_object['uterus']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stance/<stance_id>')
def stance(stance_id):
    #gather stance data from db
    data = db.stances.find_one({"stance_id":stance_id})    
    anti = data['anti']
    rebuttal = data['rebuttal']

    #use query from db to get recent news sources (list of dicts)
    news = getNews(data['query'])    

    return render_template('stance.html',
        name=data['name'],
        anti_summary=anti['text'],anti_quotes=anti['quotes'],anti_pubs=anti['publications'],
        rebut_summary=rebuttal['text'],rebut_quotes=rebuttal['quotes'],rebut_pubs=rebuttal['publications'],
        ethos=data['ethos'],pathos=data['pathos'],logos=data['logos'],
        sources=data['sources'],news=news
    )

@app.route('/resources')
def resources():
    return render_template('resources.html')


@app.route('/approach')
def approach():
    return render_template('approach.html')


@app.route('/discussion')
def discussion():
    return render_template('discussion.html')


if __name__ == '__main__':
    app.run(debug=True)
