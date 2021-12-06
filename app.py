from flask import Flask
app=Flask(__name__)

@app.route('/')
def index ():
    return "hellow word"


@app.route('/ashwini')
def ashwini():
    return "hellow ashwini"

if __name__=='__main__':
    app.run(debug=true)

