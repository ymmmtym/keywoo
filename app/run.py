from flask import *
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    names = ["json", "form"]
    return render_template("index.html", names = names)

@app.route('/json')
def test():
    return jsonify({
        "message": "test"
    })

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/result', methods=["GET", "POST"])
def result():
    search_str = str(request.form["search"])
    return render_template("result.html", search_str = search_str)

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5000, debug=True, threaded=True)