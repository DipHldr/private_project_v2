from flask import Flask,render_template,jsonify
from database import load_jobs_from_db
import json

app=Flask(__name__)

# import sqlalchemy
# db = sqlalchemy(app)

# from dataclasses import dataclass

# @dataclass
# class User(db.Model):
#   id: int
#   title: str
#   location:str
#   salary:int
#   currency:str
#   responsibilities:str
#   requirements:str

#   id = db.Column(db.Integer, primary_key=True, auto_increment=True)
#   title = db.Column(db.String(250), not_null=True)
#   location = db.Column(db.String(250), not_null=True)
#   salary = db.Column(db.Integer)
#   currency = db.Column(db.String(10))
#   responsibilities=db.Columns(db.String(2000))
#   requirements=db.Columns(db.String(2000))



@app.route("/")
def home():
    jobs=load_jobs_from_db()
    return render_template('home.html',jobs=jobs,company_name="Deep")

@app.route("/api/jobs")
def list_jobs():
    jobs=load_jobs_from_db()
    return jsonify(jobs)

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)