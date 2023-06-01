from flask import Flask, redirect, url_for
import MessageSender
from multiprocessing import Process

app = Flask(__name__)

p1, p2, p3 = Process()
r1, r2, r3 = False


def stop():
    global r1, r2, r3
    if r1:
        p1.terminate()
        r1 = False
    if r2:
        p2.terminate()
        r2 = False
    if r3:
        p3.terminate()
        r3 = False


def route(p):
    p.start()
    return redirect(url_for("main"))


@app.route("/", methods=['GET'])
def main():
    return "MAIN"


@app.route("/data1", methods=['GET'])
def get_data1():
    global r1, p1
    p1 = Process(target=MessageSender.send, args=(1,))
    stop()
    r1 = True
    return route(p1)


@app.route("/data2", methods=['GET'])
def get_data2():
    global r2, p2
    p2 = Process(target=MessageSender.send, args=(2,))
    stop()
    r2 = True
    return route(p2)


@app.route("/data3", methods=['GET'])
def get_data3():
    global r3, p3
    p3 = Process(target=MessageSender.send, args=(3,))
    stop()
    r3 = True
    return route(p3)


@app.route("/stop")
def stop_all():
    stop()
    return redirect(url_for("main"))


if __name__ == '__main__':
    app.run()
