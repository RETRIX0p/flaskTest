from flask import Flask



app = Flask(__name__) # app instance

@app.route('/') # decorater
#def func():
def home():
    return '<h2> Flask Mastery series</h2>'

if __name__ == '__main__':
    app.run(debug=True)
