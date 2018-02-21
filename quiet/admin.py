from flask import Blueprint, request, url_for, redirect, render_template, flash
from flask_login import login_required, login_user, logout_user, UserMixin

from . import app, gen, lm
from utils import ImportData
from config import *


admin = Blueprint('admin', __name__)
user = {'username': ADMIN_USERNAME, 'password': ADMIN_PASSWORD}


class User(UserMixin):
    """
    flask-login 的 UserMixin 类，实现了
    is_authenticated，is_active，is_anonymous 等方法，直接继承
    """
    pass


def query_user(username):
    """
    通过用户名，获取用户记录，如果不存在，则返回None
    """
    if user['username'] == username:
        return user


@lm.user_loader
def load_user(username):
    """
    从会话中加载用户信息
    """
    if query_user(username) is not None:
        curr_user = User
        curr_user.id = username
        return curr_user
    return None


@admin.route('/')
@login_required
def index():

    return render_template('admin.html', title="管理后台")


@admin.route('/login', methods=['GET', 'POST'])
def login():
    """管理员登录"""
    if request.method == 'POST':
        username = request.form.get('username')
        user = query_user(username)
        if user is not None and request.form['password'] == user['password']:
            curr_user = User()
            curr_user.id = username

            login_user(curr_user)

            next = request.args.get('next')
            return redirect(next or url_for('admin.index'))
        flash('用户名或者密码错误！')
    return render_template('login.html', title="管理员登录")


@admin.route('/logout')
@login_required
def logout():
    """管理员登出"""
    logout_user()
    return redirect(url_for('index'))


@admin.route('/upload/post', methods=['GET', 'POST'])
@login_required
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
    return render_template('upload_post.html', title="上传文章")


@admin.route('/upload/page', methods=['GET', 'POST'])
@login_required
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
    return render_template('upload_page.html', title="上传页面")

