import main
from flask import Flask, request, render_template, jsonify, send_file, Markup, Response, session, redirect, url_for
import flask_restful as restful
import time
import os


app = Flask(__name__)
app.secret_key = 'xyz'
api = restful.Api(app)
main = main

#Update the logs using Restful API
class DataUpdate(restful.Resource):
    def _is_updated(self, request_time):
        path, content = main.readDataText()
        return os.stat(path).st_mtime > request_time
    def get(self):
        request_time = time.time()
        while not self._is_updated(request_time):
            time.sleep(10)
        path, content = main.readDataText()
        return {'content': content,
                'date': datetime.now().strftime('%Y/%m/%d %H:%M:%S')}

class Data(restful.Resource):
    def get(self):
        path, content = main.readDataText()
        return {'content': content}

@app.route('/')
def home():
    return render_template('home.html', topicList=main.getTopicList())

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/loginpost/', methods=['POST'])
def loginpost():
    username = request.form['username']
    password = request.form['password']
    myresult = main.getDBData("user")
    authenticateBool = False
    selectedName = ""
    selectedUserName = ""
    selectedListenerId = ""
    for result in myresult:
        listenerId = result[0]
        namedb = result[1]
        usernamedb = result[2]
        passworddb = result[3]  
        if(usernamedb==username and passworddb==password):
            authenticateBool = True
            selectedName = namedb
            selectedUserName = usernamedb
            selectedListenerId = listenerId
            break
        else:
            authenticateBool = False
    if authenticateBool==True:
        return redirect(url_for('transport', name=selectedName, username=selectedUserName, listenerId=selectedListenerId))
    else:
        return render_template('login.html', error="Wrong Username or Password")


@app.route('/signup/')
def signup():
    return render_template('signup.html')

@app.route('/signuppost/', methods=['POST'])
def signuppost():
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    counterSQL = 1
    myresult = main.getDBData("user")
    for x in myresult:
        counterSQL = counterSQL + 1
    main.insertDBData("user", counterSQL, name, username, password)
    return redirect(url_for('transport', name=name, username=username, listenerId=str(counterSQL)))

@app.route('/transport/')
def transport():
    name = request.args.get('name')
    username = request.args.get('username')
    listenerId = request.args.get('listenerId')
    content = main.getContentDictionary(int(listenerId))
    return render_template('transport.html', topicList=main.getTopicList(), name=name, username=username, listenerId=listenerId, content=content)

@app.route('/subscribepost/', methods=['POST'])
def subscribepost():
    name = request.form['name']
    username = request.form['username']
    topicList = request.form.getlist('checkbox')
    listenerId = request.form['listenerId']
    if request.form['submit_button'] == 'subscribe':
        main.subscribe(topicList, name, listenerId)
    else:
        main.unsubscribe(topicList, name, listenerId)
    return redirect(url_for('transport', name=name, username=username, listenerId=listenerId))
    
@app.route('/notifypost/', methods=['POST'])
def notify():
    topicList = request.form.getlist('checkbox')
    notify = main.notify(topicList)
    return render_template('home.html', msg="Notify Success")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')