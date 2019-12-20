# scrapybilibili 运行说明文档
## 项目概述
  * 基于Scrapy框架搭建一套自动爬虫程序爬取bilibili视频信息与up主信息；
  * 数据存储于MongoDB非关系型数据库；
  * 创建每日更新crontab，crontab文件路径为'scrapybilibili/scrapybilibili/bilibili_crontab'；
  * 项目包括一个配置文件'scrapy.cfg'、一个定义数据结构的items文件'items.py'、一个定义Item Pipeline的文件'pipelines.py'、一个项目的全局配置文件'settings.py'、一个定义SpiderMiddlewares的文件'middlewares.py'、两个Spider文件'bilibili.py'(定义视频信息爬取逻辑)与'bilibiliup.py'(定义视频 Up 的主信息爬取逻辑)。
## 配置文件说明
  * 项目启动前需修改配置文件'scrapybilibili/scrapybilibili/scrapybilibili/settings.py'，主要需要修改的是MongoDBurl属性（'MONGO_URI'）与MongoDB数据库名称（'MONGO_DB'）。
## 项目部署与使用（window）
  * 可以通过调用'bilibili_crontab'实现定时爬取，进入项目根目录后在命令行输入:
  ```
  'crontab testing_crontab'；
  ```
  * 可以通过scrapy的crawl命令实现爬取，需要注意的是由于'bilibiliup.py'中视频Up主页的url构造是基于视频信息的爬取结果，所以需要先执行视频信息的爬取再执行up主信息的爬取，命令如下：
  ```
  cd scrapybilibili/scrapybilibili 
  scrapy crawl bilibili
  scrapy crawl bilibiliup
  ```
  
