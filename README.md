mygallery
这个项目好复杂
首先创建app gallery，创建使用命令 python manage.py startapp
然后创建迁移文件，使用命令 python manage.py makemigrations
然后运行命令 python manage.py migrate

关于数据库
使用命令 python manage.py createsuperuser

然后实现代码 gallery 里面的 models.py ,添加 desc... 属性
在gallery里面的 admin 注册 本模块

在home中使用gallery app
先在 settings 中注册
在 urls 中配置
在 views 中实现 home 方法，此时才可以调用 gallery 类
最后 home.html 中调用 数据库数据。

修改urls便于存储图片
修改 gallery 类，把属性都存储到数据库
修改完类以后，对照到数据库。需要重新 makedmigrations , migrate.
