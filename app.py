from flask import Flask,render_template,jsonify
app = Flask(__name__)
JOBS=[
  {
    'id':1,
    'title':'PGT-PHYSICS',
    'location':'Mainpuri',
    'salary':'Rs. 50,000'
  },
  {
    'id':2,
    'title':'PGT-COMPUTER SCIENCE',
    'location':'Etawah',
    'salary':'Rs. 40,000'
  },
  {
    'id':3,
    'title':'TGT-MUSIC',
    'location':'Mainpuri',
    'salary':'Rs. 30,000'
  },
  {
    'id':4,
    'title':'PGT-HINDI',
    'location':'Auraiya',
    'salary':'Rs. 35,000'
  },
  {
    'id':5,
    'title':'HOSTEL-WARDEN',
    'location':'Mainpuri',
    'salary':'Rs. 65,000'
  },
  {
    'id':6,
    'title':'WEB-ADMIN',
    'location':'Mainpuri',
    'salary':'Rs. 120,000'
  }
]


@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

print(__name__)
if (__name__)== "__main__":
  app.run("0.0.0.0",debug=True)