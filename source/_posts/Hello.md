title: Hello world
summary: 第一篇文章
url: hello-world
datetime: 2018-02-15
category: 随笔
tag: 测试
     随笔


## Hello world

这是一篇测试文章，测试`markdown`语法是否支持。

代码片段：

```Python
# hello.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print('Hello world!')
```

这是一个列表：

- 第一条
- 第二条
    1. 第二条第一条
    2. 第二天第二条

这是一段话：

青青子衿，**悠悠我心**，***但为君故***，*沉吟至今*。

> 慨当以慷，忧思难忘
> 何以解忧？唯有杜康

这是一个链接：[yukunweb.com](http://www.yukunweb.com)

这是一张图片：![cat](http://imgout.ph.126.net/57363048/pexels-photo-416208.jpg)

还支持表格：

| 默认列 | 左对齐列 | 右对齐列 | 居中列 |
|:----|:----|----:|:----:|
| Hello | Hello | Hello | Hello |
