from flask import Flask
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    try:
        url = 'http://ip.jsontest.com/'
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        else:
            return "Error trying to call {}".format(url), 500
    except Exception as e:
        return "Error trying to call {} ERROR MESSAGE: {}".format(url, e), 500
    

@app.route('/healthcheck')
def healthcheck():
    return "OK, IM HEALTHY", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5252)
