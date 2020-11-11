from flask import Flask
import datetime

server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello World!"

@server.route("/time1")
def time1():
    nt = datetime.datetime.now()
    return str(nt)

@server.route("/time2")
def time2():
    ut = datetime.datetime.utcnow()
    return str(ut)

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000, debug=True)
