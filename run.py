#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
from quiet import app
from generate import Generate


if __name__ == '__main__':
    gen = Generate()
    t = time.time()
    gen()
    print('生成完成！！！',time.time()-t)
    app.run()



