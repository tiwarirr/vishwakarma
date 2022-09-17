from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
  return "<h1>Vishwa Karma Ji Daya Karo</h1>"

print(__name__)
if (__name__)== "__main__":
  app.run("0.0.0.0",debug=True)