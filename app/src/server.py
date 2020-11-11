from flask import Flask

server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello World!"

@server.route("/time1")
def time1():
    ct = datetime.datetime.now()
    return ct

@server.route("/time2")
def time2():
    ct = datetime.datetime.utcnow()
    return ct

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)
