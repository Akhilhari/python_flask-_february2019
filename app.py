from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "hello..."

@app.route("/home")
def home():
    return "My Home page"  

@app.route("/contact")
def contact():
    return "9495409381"

if(__name__=="__main__"):
    app.run()

    