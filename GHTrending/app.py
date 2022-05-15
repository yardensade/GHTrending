from flask import Flask, Response

from GHTrending import fetch_trending_repos

app = Flask(__name__)

@app.route('/')
def index():
    return 'UP AND GUNNING!'

@app.route('/trending/<int:repos_num>')
def trending_repos(repos_num):
    result = fetch_trending_repos(repos_num)
    resp = Response(result)
    resp.headers["content-type"] = "text/plain"
    return resp

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
