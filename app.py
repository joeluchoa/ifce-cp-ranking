from flask import Flask, render_template
import requests

def data():
    resp = requests.get('http://codeforces.com/api/user.info?handles=tsebayoth;KAN;Um_nik;isaf27')
    if resp.status_code != 200:
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    return resp.json()

app = Flask(__name__)

@app.route('/')
def home():
    d = data()
    return render_template('home.html', data = d)

if __name__ == '__main__':
    app.run(debug = True)
