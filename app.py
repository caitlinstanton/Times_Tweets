from flask import Flask, render_template, session, redirect,url_for, request

import twitter, nyt

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        twitter.search(request.form['searchterm'])
        nyt.search(request.form['searchterm'])
        f = open('tweets.csv','r')
        tweets = f.read()
        f.close()
        tweets = tweets.decode('utf-8')
        g = open('articles.csv','r')
        articles = g.read()
        g.close()
        articles = articles.decode('utf-8')
        return render_template("index.html",twitter=tweets,nyt=articles)

    return render_template("index.html",twitter='No Search Has Been Done',nyt='No Search Has Been Done')                 


if __name__ == "__main__":
    app.debug = True
    app.secret_key="Don't store this on github"
    app.run()
