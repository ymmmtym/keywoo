#!/usr/bin/python

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

with open("data/search_sites.json", "r", encoding="utf-8") as search_sites_json:
    search_dic = json.load(search_sites_json)


@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        if request.form["name"] and request.form["url"]:
            search_dic.update({str(request.form["name"]):str(request.form["url"])})

    return render_template("index.html", search_dic = search_dic)

@app.route('/result', methods=["GET", "POST"])
def result():
    if request.form["search"]:
        search_text = str(request.form["search"])
        search_list = search_text.splitlines()
        return render_template("result.html", search_list = search_list, search_dic = search_dic)
    else:
        return render_template("index.html", search_dic = search_dic)

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=80,threaded=True)
