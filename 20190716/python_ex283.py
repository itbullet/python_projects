from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    return """<html><body><pre>
  _,-=._              /|_/|
  `-.}   `=._,.-=-._.,  @ @._,
     `._ _,-.   )      _,.-'
        `    G.m-"^m`m'
</pre>
<p>Ты тиво делаишь?</p></body></html>"""

app.run(host="172.30.20.132", port="8000")