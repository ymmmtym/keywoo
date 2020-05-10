from flask import render_template, url_for, request, jsonify, flash
from keywoo import app
from keywoo import db
from keywoo.models.sites import Site
from keywoo.models.users import User
import json


with open("keywoo/data/sites.json", "r", encoding="utf-8") as sites_json:
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
                    flash(site + ' is deleted')
            if request.form["radio"] == "default":
                with open("./data/sites.json", "r", encoding="utf-8") as sites_json:
                    search_dic = json.load(sites_json)
                flash('loaded default sites')
            if request.form["radio"] == "reset":
                search_dic.clear()
                flash('reseted all sites')
            if request.form["radio"] == "add":
                if request.form["site_name"] and request.form["url"]:
                    search_dic.update({str(request.form["site_name"]):str(request.form["url"])})
                flash(request.form["site_name"]+' is added')
    return render_template("index.html", search_dic = search_dic)

@app.route('/result', methods=["GET", "POST"])
def result():
    if request.form["search"]:
        search_text = str(request.form["search"])
        search_list = search_text.splitlines()
        flash('Result Pages')
        return render_template("result.html", search_list = search_list, search_dic = search_dic)
    else:
        flash('failed')
        return render_template("index.html", search_dic = search_dic)

# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

# @app.route("/secret")
# @login_required
# def secret():
#     return "secret contents"