from flask import Blueprint,request,render_template,redirect,url_for
from pyecharts import options as opts
from pyecharts.charts import Bar,Line,Scatter,Pie
from flaskr.db import get_db
from random import randrange
from pyecharts.globals import ThemeType


bp = Blueprint('visible', __name__)

X = []
Y = [[] for i in range(10)]
names  = []
theme = 'light'

@bp.route('/saveData/<chartType>',methods=('GET','POST'))
def saveData(chartType):
    if request.method == 'POST':
        global names
        names = request.form.getlist('tablename')
        db = get_db()
        cur = db.cursor()
        count = len(names)

        if count == 0:
            sqlparm = ''
            
        elif count >0:
            sqlparm = ' SELECT * FROM `{0}` '.format(names[0]) 
            for i in range(1,count):
                sqlparm += 'join `{0}` using(date) '.format(names[i])
            cur.execute(sqlparm)
            datas = cur.fetchall()
            
            for data in datas:
                X.append(data['date'])
                for j in range(0,count):
                   Y[j].append(data[names[j]])
            
        return redirect(url_for('visible.visible',chartType='lineChart') )


def bar_base() -> Bar:
    if len(names) == 0:
        pass
    elif len(names) >= 1:
        c = Bar()
        c.add_xaxis(X)
        c.set_global_opts(toolbox_opts=opts.ToolboxOpts(),
                            title_opts=opts.TitleOpts(title="BarChart"),
                            yaxis_opts=opts.AxisOpts(name="Data"),
                            xaxis_opts=opts.AxisOpts(name="Date"),
                            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
                            )
        
        for i in range(0,len(names)):
            c.add_yaxis(names[i],Y[i])
        
    return c
    

def line_base() -> Line:
    if len(names) == 0:
        pass

    elif len(names) >= 1:
        c = Line()
        c.add_xaxis(X) 
        c.set_global_opts(toolbox_opts=opts.ToolboxOpts(),
                            title_opts=opts.TitleOpts(title="LineChart"),
                            yaxis_opts=opts.AxisOpts(name="Data"),
                            xaxis_opts=opts.AxisOpts(name="Date"),
                            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
                            )
        
        for i in range(0,len(names)):
            c.add_yaxis(names[i],Y[i])

    return c

def scatter_base() -> Scatter:
    if len(names) == 0:
        pass

    elif len(names) >= 1:
        c = Scatter()
        c.add_xaxis(X)
        c.set_global_opts(toolbox_opts=opts.ToolboxOpts(),
                            title_opts=opts.TitleOpts(title="ScatterChart"),
                            yaxis_opts=opts.AxisOpts(name="Data"),
                            xaxis_opts=opts.AxisOpts(name="Date"),
                            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
                            )
        
        for i in range(0,len(names)):
            c.add_yaxis(names[i],Y[i])

    return c

@bp.route("/barChart",methods=('GET','POST'))
def get_bar_chart():
    c = bar_base()
    return c.dump_options()

@bp.route("/lineChart",methods=('GET','POST'))
def get_line_chart():
    c = line_base()
    return c.dump_options()


@bp.route("/scatterChart",methods=('GET','POST'))
def get_scatter_chart():
    c = scatter_base()
    return c.dump_options()


@bp.route("/visible/<chartType>",methods=('GET','POST'))
def visible(chartType):
    return render_template("pyecharts.html",operator=chartType,theme=theme)

@bp.route("/setTheme/<setTheme>",methods=('GET','POST'))
def setTheme(setTheme):
    global theme
    theme = setTheme
    before_url = request.referrer
    return redirect(before_url)