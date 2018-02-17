# quiet

本项目适合喜爱用`markdown`写博客的用户使用。

一个支持上传 markdown 文件生成 html 的 flask 静态轻博客，支持`table`和`Meta`信息。依赖少，配置简单，使用方便。

## 使用

直接下载本项目文件，并安装依赖:

```
pip install -r requirements.txt
```

配置好`config.py`的博客信息，将个人写好的`markdown`文件放到`source`文件夹对应文件夹内，
文章的`.md`文件放入`source/_posts/`文件夹，页面文件放入`source/_pages/`中。

如不希望程序自动生成文章标题、分类等信息，需要在文件中加入`Meta`信息，`Meta`信息需放置于`.md`文件的顶部，且于第一行开始，
之间不可有空行。如示例文件`source/_posts/Hello.md`的`Meta`信息为：

```
title: Hello world // 文章标题
summary: 第一篇文章 // 文章简介
url: hello-world // 文章 url
datetime: 2018-02-15 // 文章日期
category: 随笔 // 文章分类
tag: 测试 // 文章标签
     随笔

正文开始
```

**注意：**

1. `meta`信息之间不能有空行，但与正文之间必须有至少一个空行；
2. `meta`信息必须使用小写，并使用**英文**冒号；
3. 非文章页面（即 page 页面文件）的`meta`信息必须包含`title`和`url`（如：about）信息；
4. 如`tag`信息不只一个时，需换行并且至少有 4 个空格。


## 样式

文章页：

![demo](http://opxib6gmc.bkt.clouddn.com/quiet.jpg)

首页：

![demo](http://opxib6gmc.bkt.clouddn.com/quiet2.jpg)


## Enjoy it
