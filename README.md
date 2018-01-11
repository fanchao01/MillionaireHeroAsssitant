# MillionaireHeroAsssitant

手机APP百万英雄、冲顶大会等答题类解决的答题助手，自动帮助从搜索引擎中搜索答案。


# 前提 
需要手机连接到电脑，并且将手机屏幕投射到PC屏幕中。

# 原理
截图投射到PC屏幕中的问题 -> ORC转成问题 -> 过滤 -> (启动浏览器) -> 调用浏览引擎API搜索

# 局限
1. 受手机屏幕投射到PC端的延迟，一般的手机助手延迟在3~5秒，可以使用airmirror等低延迟软件

2. 没有语义分析，只是简单的过滤影响搜索引擎的非关键词，答案准确度完全依赖搜索引擎，建议使用bing等不常用搜索引擎。

# 依赖
```
1. python2.6+ 
    https://www.python.org/downloads/ 下载2.7版本，不支持3.6+版本

2. pywin32
    安装python扩展包需要的windows环境
    https://jaist.dl.sourceforge.net/project/pywin32/pywin32/Build%20218/pywin32-218.win-amd64-py2.7.exe

3. selenium
    pip install seleniim
    https://selenium-release.storage.googleapis.com/index.html?path=3.8/ 下载对应操作系统的WebDriver，放到$PATH定义目录下即可

4. PIL
    pip install PIL>=1.1.7
    http://pythonware.com/products/pil/ 下载安装对应操作系统的库
    PIL可能会提示搜索不到Python环境，这个时候先运行本目录下的registery.py

5. aip
    百度云ORC的SDK
    https://ai.baidu.com/file/893D23892BF349738D66757C425176F9
    下载解压后运行 python setup.py

```

# 使用方法

```python
MillionaireHeroAsssitant >python main.py
millionaire >> c  # 输入c开始
millionaire >> q  # 输入q退出
```

# 最后

祝玩的愉快

