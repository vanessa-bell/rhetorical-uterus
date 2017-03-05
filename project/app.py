from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
mongo_object = MongoClient()
db = mongo_object['uterus']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stance/<stance_id>')
def stance(stance_id):
    data = db.stances.find_one({"stance_id":stance_id})    
    anti = data['anti']
    rebuttal = data['rebuttal']
    pathos = data['pathos']
    ethos = data['ethos']
    logos = data['logos']
    sources = data['sources']
    return render_template('stance.html',
        name=data['name'],
        anti_summary=anti['text'],anti_q1=anti['quotes'][0],anti_q2=anti['quotes'][1],anti_q3=anti['quotes'][2],
        rebut_summary=rebuttal['text'],rebut_q1=rebuttal['quotes'][0],rebut_q2=rebuttal['quotes'][1],rebut_q3=rebuttal['quotes'][2],
        ethos_title=data['ethos']['title'],ethos_text=data['ethos']['text'],
        pathos_title=data['pathos']['title'],pathos_text=data['pathos']['text'],
        logos_title=data['logos']['title'],logos_text=data['logos']['text']
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
