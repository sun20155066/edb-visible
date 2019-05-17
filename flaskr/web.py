from flask import (
    Blueprint, render_template,request,send_from_directory,jsonify,redirect,url_for
)
from flaskr.db import get_db
from flaskr.auth import login_required
import os
import time

import pymysql #支持Python3.0
##读取excel使用(支持03)
import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple
from builtins import int



bp = Blueprint('web', __name__)


ALLOWED_EXTENSIONS = set(['txt', 'xls', 'xlsx'])  # 允许上传的文件后缀

# 判断文件是否合法
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

##将excel文件导入mysql中
def importExcelToMysql(path):
    db = get_db()
    cur = db.cursor()
    tablename = 'User_' + path.split('\\')[-1].split('.')[0]
    #删除表
    cur.execute("drop table if exists {0}".format(tablename))
    #创建表
    cur.execute('create table {0} ( A varchar(255), B varchar(255) )'.format(tablename))
    #根据Excel路径读取Excel
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    #根据sheet名称获取sheet,sheets[0]为第一个表格名称
    worksheet = workbook.sheet_by_name(sheets[0])
    ##遍历行
    for i in range(1, worksheet.nrows):
        row = worksheet.row(i)
 
        ##初始化数组
        sqlstr = []
        ##遍历列
        for j in range(0, worksheet.ncols):
            ##构造数组
            sqlstr.append(worksheet.cell_value(i, j))
 
        ##插入数据库
        valuestr = [str(sqlstr[0]), int(sqlstr[1])]
 
        ##执行sql语句
        cur.execute(
            "insert into {0} ".format(tablename) +
            "values(%s,%s)", valuestr)
    
    #提交
    db.commit()
 

@bp.route("/downloader")
def downloader():
    return send_from_directory('templates', 'uploadTemplate.xlsx', as_attachment=True)  # as_attachment=True 一定要写，不然会变成打开，而不是下载

@bp.route('/importFile')
def importFile():
    return render_template('web/importFile.html')

userDatas = []
@bp.route('/upload', methods=['POST'])
def upload():
    f=request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值
    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
        fname=f.filename
        basedir = os.path.dirname(__file__)
        upload_path = os.path.join(basedir, "upload", fname)
        f.save(upload_path)  #保存文件到upload目录
        importExcelToMysql(upload_path)
        userDatas.append('User_' + fname.split('.')[0])
        userDatas2 = list(set(userDatas))
        userDatas2.sort(key = userDatas.index)
        userDatas2.reverse()

        return render_template('web/myData.html',userDatas=userDatas2)
    else:
        return jsonify({"errno": 1001, "errmsg": "fail"})

@bp.route('/myData')
@login_required
def myData():
    global userDatas
    userDatas = []
    return render_template('web/myData.html')



@bp.route('/index')
@login_required
def index():
    global tableNames
    tableNames = []
    """Show dataVisible web."""
    db = get_db()
    cur = db.cursor()
    cur.execute(
        'show tables'
    )
    tables = cur.fetchall()
    return render_template('web/index.html', tables=tables)


tableNames = []

@bp.route('/<tableName>/add')
def add(tableName):
    db = get_db()
    cur = db.cursor()

    tableNames.append(tableName)
    tableNames2 = list(set(tableNames))
    tableNames2.sort(key = tableNames.index)
    tableNames2.reverse()

    cur.execute(
        'show tables'
    )
    tables = cur.fetchall()

    return render_template('web/index.html',tables=tables,tableNames=tableNames2)
