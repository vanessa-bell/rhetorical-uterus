from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stance')
def stance():
    return render_template('stance.html')

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
