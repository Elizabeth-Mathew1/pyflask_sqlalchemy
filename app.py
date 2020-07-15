from flask import Flask, session, url_for, redirect, render_template, request, abort, flash

app=Flask(__name__) #creating an instance of web app
@app.route("/")
def home():
    return render_template("index.html")
if __name__=="__main__":
    app.run()
