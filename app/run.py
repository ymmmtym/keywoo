#!/usr/bin/python

from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
def get_toppage(str):
    list = str.split('/')
    return list[0] + '//' + list[2]
app.jinja_env.globals['get_toppage'] = get_toppage
app.config['JSON_AS_ASCII'] = False

with open("data/sites.json", "r", encoding="utf-8") as sites_json:
    search_dic = json.load(sites_json)

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        if request.form["radio"]:
            global search_dic
            if request.form["radio"] == "delete":
                del_sites = request.form.getlist("check")
                for site in del_sites:
                    del search_dic[site]
            if request.form["radio"] == "default":
                with open("./data/sites.json", "r", encoding="utf-8") as sites_json:
                    search_dic = json.load(sites_json)
            if request.form["radio"] == "reset":
                search_dic.clear()
            if request.form["radio"] == "add":
                if request.form["site_name"] and request.form["url"]:
                    search_dic.update({str(request.form["site_name"]):str(request.form["url"])})
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
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0',port=port,threaded=True)
