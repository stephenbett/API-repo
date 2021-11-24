from flask import Flask ,jsonify
app = Flask(__name__)
@app.route('/')
def index ():
    return "{name: Stevoh Steen,}"
if __name__ =="__main__":
  app.run(debug   =True)
