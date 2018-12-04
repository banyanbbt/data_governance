# Banyan Data

Banyan Data Governance open source project.

基于 Python 语言的，数据治理工具。


目录结构
========

```
data_governance       项目根目录
  analyzers           内容分析器：内容解析的规则
  data                数据文件目录
  logs                日志文件目录
  services            内容处理器：读入数据、数据分析、筛选和清洗
  settings            项目配置文件
  sqls                数据库统计和分析脚本
  utils               项目工具包：文件读取、解析、写入工具
  REAMDME.md          项目说明文档
  requirements.txt    项目依赖
  analyze.py          数据分析入口
  file_manage.py      文件处理入口
  stats_calculate.py  状态统计入口
```



安装运行环境和项目依赖
=======

1. 安装 Python 运行环境
--------

```

>> python

Python 3.6.1

```


2. 安装 MongoDB
--------

```console

# Install MongoDB Community Edition on OS X

brew install mongodb

sudo mkdir -p /data/db

sudo mongod --dbpath /data/db

```


3. 安装项目依赖
--------

```console

pip install -r requirements.txt

```

