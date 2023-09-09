
http://c.biancheng.net/python_spider/bs4.html
由于 Bautiful Soup 是第三方库，因此需要单独下载，下载方式非常简单，执行以下命令即可安装：
pip install bs4
由于 BS4 解析页面时需要依赖文档解析器，所以还需要安装 lxml 作为解析库：
pip install lxml
Python 也自带了一个文档解析库 html.parser， 但是其解析速度要稍慢于 lxml。除了上述解析器外，还可以使用 html5lib 解析器，安装方式如下：
pip install html5lib

模块随机获取UA

pip install fake-useragent