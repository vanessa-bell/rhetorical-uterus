from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
mongo_object = MongoClient(HOST,PORT)
db = mongo_object['uterus']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stance/<stance_id>')
def stance(stance_id):
    data = db.stances.find_one({"name":stance_id})    
    return render_template('stance.html',data=data)

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
