import os
from functools import wraps

from flask import Blueprint, request, url_for, redirect, render_template

from . import app, gen
from utils import ImportData


admin = Blueprint('admin', __name__)


@admin.route('/login')
def login():
    pass


@admin.route('/upload/post', methods=['GET', 'POST'])
def upload_post():
    """
    支持用户上传 md 文件并生成 html
    :return:
    """
    source_folder = app.config['POST_PATH']
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        path = os.path.join(source_folder, filename)
        file.save(path)
        # 生成 html
        gen()
        # 重置 shelve 数据
        ImportData.reload_data()

        return redirect(url_for('index'))
    return render_template('upload_post.html')

@admin.route('/upload/page', methods=['GET', 'POST'])
def upload_page():
    """
    支持用户上传 md 文件并生成 html
    :return:
    """
    source_folder = app.config['PAGE_PATH']
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        path = os.path.join(source_folder, filename)
        file.save(path)

        # 生成 html
        gen()
        # 重置 shelve 数据
        ImportData.reload_data()

        return redirect(url_for('index'))
    return render_template('upload_page.html')

