from flask import Blueprint, jsonify

from utils import ImportData


api = Blueprint('api', __name__)


@api.route('/posts')
def get_posts():
    """
    所有文章信息
    :return: json
    """

    return jsonify(ImportData.get_data().get('post_data'))


@api.route('/post/<int:id>')
def get_post(id):
    """
    指定 id 文章信息
    """
    for p in ImportData.get_data().get('post_data'):
        if p.get('id') == id:

            return jsonify(p)
    return jsonify({'msg': '没有数据'})


@api.route('/pages')
def get_pages():
    """
    所有页面
    """

    return jsonify(ImportData.get_data().get('page_data'))


@api.route('/page/<url>')
def get_page(url):
    """
    指定页面信息
    """
    for p in ImportData.get_data().get('page_data'):
        if p.get('url') == url:

            return jsonify(p)
    return jsonify({'msg': '没有数据'})


@api.route('/tags')
def get_tags():
    """
    所有标签信息
    """

    return jsonify(ImportData.get_data().get('tag_data'))


@api.route('/tag/<tag>')
def get_tag(tag):
    """
    指定标签信息
    """
    for t in ImportData.get_data().get('tag_data'):
        if t.get('tag') == tag:

            return jsonify(t)
    return jsonify({'msg': '没有数据'})


@api.route('/categories')
def get_categories():
    """
    所有分类信息
    """

    return jsonify(ImportData.get_data().get('category_data'))


@api.route('/category/<cate>')
def get_category(cate):
    """
    指定分类信息
    """
    for c in ImportData.get_data().get('category_data'):
        if c.get('category') == cate:

            return jsonify(c)
    return jsonify({'msg': '没有数据'})




