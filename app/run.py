#!/usr/bin/python

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# common setting
search_dic = {
    "Google": "https://www.google.com/search?q=",
    "Weblio English": "https://ejje.weblio.jp/content/",
    "Amazon": "https://www.amazon.co.jp/s?k=",
    "Rakuten": "https://search.rakuten.co.jp/search/mall/",
    "Yahoo Auctions": "https://auctions.yahoo.co.jp/search/search?p=",
    "Yahoo Auctions(record)": "https://auctions.yahoo.co.jp/search/search?auccat=22260&p=",
    "Spotify": "https://open.spotify.com/search/results/",
    "Discogs": "https://www.discogs.com/ja/search/?q="
}

@app.route('/')
def index():
    internal_links = ["search_site", "search_engine"]
    return render_template("index.html", names = internal_links)

@app.route('/search_site')
def test():
    return jsonify(search_dic)

@app.route('/search_engine')
def search_engine():
    return render_template("search_engine.html")

@app.route('/search_result', methods=["GET", "POST"])
def search_result():

    if request.form["search"]:
        search_text = str(request.form["search"])
        search_list = search_text.splitlines()
        return render_template("search_result.html", search_list = search_list, search_dic = search_dic)
    else:
        return render_template("error.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5000,threaded=True)
