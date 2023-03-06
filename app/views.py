from app import app
from flask import render_template

from .request import  publishedArticles, mainArticles, topHeadlines

@app.route('/')
def home():
    articles = publishedArticles()

    return  render_template('home.html', articles = articles)

@app.route('/headlines')
def headlines():
    headlines = topHeadlines()

    return  render_template('headlines.html', headlines = headlines)

@app.route('/articles')
def articles():
    main = mainArticles()

    return  render_template('articles.html', main = main)

@app.route('/trending')
def trending():

    return  render_template('trending.html')

