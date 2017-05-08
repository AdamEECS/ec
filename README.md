# ec

mongo服务启动方法：

```
mongod --dbpath /Users/username/data/db
```

程序启动方法：

```
sh start.sh
```

注：为调试css和js，应在 chrome - Network 启用「disable cache」。

## Pillow安装方法

debian直接安装pillow不成功，可能是缺少依赖，使用以下命令安装

```
apt-get update
apt-get install libjpeg62-turbo-dev libopenjpeg-dev libfreetype6-dev libtiff5-dev liblcms2-dev libwebp-dev tk8.6-dev python3-tk

```

然后重新安装pillow

```
pip3 uninstall pillow
pip3 install pillow
```