import requests

def data():
    resp = requests.get('http://codeforces.com/api/user.info?handles=tsebayoth;KAN;Um_nik;isaf27')
    if resp.status_code != 200:
        raise Exception('GET /tasks/ {}'.format(resp.status_code))
    return resp.json()
