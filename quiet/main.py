#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import send_from_directory

from . import app


@app.route('/')
@app.route('/index')
def index():

    return send_from_directory('static', 'generated/page/index.html')


@app.route('/tags')
def tag():

    return send_from_directory('static', 'generated/page/tags.html')


@app.route('/tag/<tag>')
def tag_post(tag):

    return send_from_directory('static', 'generated/page/tag/{tag}.html'.format(tag=tag))


@app.route('/categories')
def category():

    return send_from_directory('static', 'generated/page/categories.html')


@app.route('/category/<category>')
def category_post(category):

    return send_from_directory('static', 'generated/page/category/{category}.html'.format(category=category))


@app.route('/page/<page>')
def page(page):

    return send_from_directory('static', 'generated/page/{page}.html'.format(page=page))


@app.route('/post/<year>/<month>/<post>')
def post(year, month, post):

    return send_from_directory('static',
                'generated/post/{year}/{month}/{post}.html'.format(year=year, month=month, post=post))
