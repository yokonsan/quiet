#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import codecs
import shutil
import shelve

from markdown import Markdown
from jinja2 import Environment, FileSystemLoader


GENERATED_FILE = './quiet/static/generated/'


def get_all_file():
    """
    扫描指定文件夹下的所有 markdown 文件
    :return:
    """
    pass


def clean_generated():
    """
    清空 generated 文件夹下的文件
    """
    pass


def set_url(file, meta):
    """
    解析 meta 组合文章 url
    :param meta:
    :return: url
    """
    date = meta.get('datetime')
    pass


def markdown_to_html(file):
    """
    将 markdown 文件转换为 html
    :param file: markdown file
    """
    with codecs.open(file, mode="r", encoding="utf-8", errors='ignore') as f:
        body = f.read()
        md = Markdown(extensions=['fenced_code', 'codehilite(css_class=highlight,linenums=True)',
                                  'meta', 'admonition', 'tables', 'wikelinks'])
        content = md.convert(body)
        meta = md.Meta if hasattr(md, 'Meta') else {}

        set_url(file, meta)

        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template('post.html')
        html = template.render(
        )
        pass


def save_html(html):
    """
    保存 html 文件
    :param html: html 文件
    """
    pass





