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

content_dic = {
    "search_sites": "Search Sites",
    "search_engine": "Search Engine",
}


@app.route('/')
def index():
    return render_template("index.html", search_dic = search_dic)

@app.route('/search_result', methods=["GET", "POST"])
def search_result():

    if request.form["search"]:
        search_text = str(request.form["search"])
        search_list = search_text.splitlines()
        return render_template("search_result.html", search_list = search_list, search_dic = search_dic)
    else:
        return render_template("search_error.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=80,threaded=True)
