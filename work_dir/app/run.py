from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    names = ["World", "Flask" ,"Python"]
    return render_template("index.html", names = names)

@app.route('/test')
def test():
    return jsonify({
        "message": "test"
    })

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5000, debug=True, threaded=True)
