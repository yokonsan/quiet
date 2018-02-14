#!/usr/bin/python
# -*- coding:utf-8 -*-

from quiet import app
from generate import Generate


if __name__ == '__main__':
    gen = Generate()
    gen.main()
    app.run()



