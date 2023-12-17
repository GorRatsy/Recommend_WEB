from flask import Flask, render_template, request
from model import Recommender

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('/index.html')


@app.route('/about/')
def about():
    return render_template('/about.html')


@app.route('/recommendation/', methods=["POST", "GET"])
def recommender():

    if request.method=='GET':
        return render_template('/recommmend.html')

    elif request.method=='POST':
        user_id = request.form['userid']
        rec = Recommender(user_id)
        recommendations = rec.return_top_three()

        return render_template('/recommendations.html', items=recommendations)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)