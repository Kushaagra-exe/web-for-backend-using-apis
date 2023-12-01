from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def hello():
    return "<h1>Temporary Closed, Under Development        Contact @Kushaagra_exe </h1>"

@app.route('/infogen', methods = ['POST', 'GET'])
def hello1():
    return "<h1>Temporary Closed, Under Development        Contact @Kushaagra_exe </h1>"

@app.route('/bin-lookup', methods = ['POST', 'GET'])
def hello2():
    return "<h1>Temporary Closed, Under Development        Contact @Kushaagra_exe </h1>"

@app.route('/activity-suggestor', methods = ['POST', 'GET'])
def hello3():
    return "<h1>Temporary Closed, Under Development        Contact @Kushaagra_exe </h1>"

