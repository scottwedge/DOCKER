from flask import Flask

server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello World!"

@server.route("/time1")
def time1():
    return "Current time is: datetime.datetime.now()"

@server.route("/time2")
def time2():
    return "Current time is: datetime.datetime.utcnow()"

if __name__ == "__main__":
    server.run(host="0.0.0.0")
