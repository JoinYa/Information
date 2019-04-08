from info.modules.index import index_blu
from flask import render_template


# 测试
@index_blu.route('/')
def index():
    return render_template("admin/index.html")



