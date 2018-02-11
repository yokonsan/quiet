#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, render_template

from . import app


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')

@app.route('/tags')
def tag():

    return render_template('tags.html')

@app.route('/tag/<url>')
def tag_post(url):

    return render_template('tag.html')

@app.route('/categories')
def category():

    return render_template('categories.html')

@app.route('/category/<url>')
def category_post(url):

    return render_template('category.html')

@app.route('/page/<page>')
def page(page):

    return render_template('page.html')

@app.route('/post/<int:year>/<int:month>/<url>')
def post(year, month, url):

    return render_template('post.html')
