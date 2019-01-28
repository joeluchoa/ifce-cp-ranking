from flask import Flask, render_template
import lib.codeforces as api

app = Flask(__name__)

@app.route('/')
def home():
    d = api.data()
    return render_template('home.html', data = d)

if __name__ == '__main__':
    app.run(debug = True)
