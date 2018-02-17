#!/usr/bin/python
# -*- coding:utf-8 -*-

import shelve

from config import BLOG_DAT


class ImportData(object):
    """
    载入 shelve 保存的博客数据
    """

    _data = {}

    @classmethod
    def _load_data(cls):
        """载入数据"""
        data = shelve.open(BLOG_DAT)
        for i in data:
            cls._data[i] = data[i]

        return cls._data

    @classmethod
    def get_data(cls):
        """获取数据"""
        if len(cls._data) == 0:
            cls._load_data()

        return cls._data

    @classmethod
    def reload_data(cls):
        """重新载入数据"""
        cls._load_data()
