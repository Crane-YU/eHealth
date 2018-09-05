# 如何创建一个虚拟环境
- virtualenv -p python3 /Users/craneyu/Desktop/[file name]
- cd [file name]
- django-admin startproject [project_name]
- python3 manage.py startapp [app_name] 
- cd ..
- tree [project_name]

# manage.py
- 不会去修改的重要文件

# urls.py
- 用来设置每一个url的网址对应的函数以及对应方式，通常是要创建新的网页时要编辑的文件

# settings.py
- 此网站系统设计所在的地方，通常是创建新的网页时要先编辑的文件，
每次创建一个新的app，要把app文件加入到settings里面

# 数据库与Django的关系
- Django的数据库是以Model的方式进行操作的，以class类先创建好Model，然后通过对Model的操作达到操作数据库
- `__unicode__` and `__str__` have the same function
- admin.py 是Django默认的数据库内容管理界面

# 在设计数据的时候，前往不要放入标点符号，要不然不能跳转

# 如何用现有的CSS和JavaScript网页框架
- 大部分设计都是基于现有的网络框架
    - 以bootstrap为主，使用简单
    - CDN: A CDN’s mission is to virtually shorten that physical distance, 
    the goal being to improve site rendering speed and performance
    - 可以把bootstrap的CDN放到base.html的header中

