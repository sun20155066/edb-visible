from flask import Blueprint,request,render_template,redirect,url_for
from pyecharts import options as opts
from pyecharts.charts import Bar,Line,Scatter,Pie
from flaskr.db import get_db
from random import randrange


from pyecharts.globals import ThemeType


bp = Blueprint('visible', __name__)

X = []
Y1 = []
Y2 = []
Y3 = []
names  = []
theme = 'light'


@bp.route('/saveData/<chartType>/<theme>',methods=('GET','POST'))
def barChart(chartType,theme):
    if request.method == 'POST':
        global names,X,Y1,Y2,Y3
        names = request.form.getlist('tablename')
        db = get_db()
        cur = db.cursor()
        count = len(names)
        Ycount = 0

        if count == 0:
            sqlparm = ''
            
        elif count == 1:
            sqlparm = 'SELECT `{0}`.A as date,`{0}`.B as `{0}` FROM `{0}`'.format(names[0])
            cur.execute(sqlparm)
            datas = cur.fetchall()

            X = []
            Y1 = []
            Ycount = 1
            for data in datas:
                X.append(data['date'])
                Y1.append(data[names[0]])

            
        elif count == 2:
            sqlparm = ' SELECT `{0}`.A as date,`{0}`.B as `{0}`, `{1}`.B as `{1}` FROM `{0}`,`{1}` where `{0}`.A = `{1}`.A '.format(names[0],names[1])
            cur.execute(sqlparm)
            datas = cur.fetchall()

            X = []
            Y1 = []
            Y2 = []
            Ycount = 2
            for data in datas:
                X.append(data['date'])
                Y1.append(data[names[0]])
                Y2.append(data[names[1]])

        elif count == 3:
            sqlparm = ' SELECT `{0}`.A as date,`{0}`.B as `{0}`, `{1}`.B as `{1}`, `{2}`.B as `{2}` FROM `{0}`,`{1}`,`{2}` where `{0}`.A = `{1}`.A and `{1}`.A = `{2}`.A '.format(names[0],names[1],names[2])
            cur.execute(sqlparm)
            datas = cur.fetchall()

            X = []
            Y1 = []
            Y2 = []
            Y3 = []
            Ycount = 3
            for data in datas:
                X.append(data['date'])
                Y1.append(data[names[0]])
                Y2.append(data[names[1]])
                Y3.append(data[names[2]])
           
        return redirect(url_for('visible.visible',chartType='lineChart') )


def bar_base() -> Bar:
    if len(names) == 0:
        pass

    elif len(names) == 1:
        c = (
            Bar()
            .add_xaxis(X)
            .add_yaxis(names[0],Y1)
            .set_global_opts(toolbox_opts=opts.ToolboxOpts())
        )

    elif len(names) == 2:
        c = (
            Bar()
            .add_xaxis(X)
            .add_yaxis(names[0],Y1)
            .add_yaxis(names[1],Y2)
            .set_global_opts(toolbox_opts=opts.ToolboxOpts())
        )

    elif len(names) == 3:
        c = (
            Bar()
            .add_xaxis(X)
            .add_yaxis(names[0],Y1)
            .add_yaxis(names[1],Y2)
            .add_yaxis(names[2],Y3)
            .set_global_opts(toolbox_opts=opts.ToolboxOpts())
        )
        
    return c
    

def line_base() -> Line:
    if len(names) == 0:
        pass

    elif len(names) == 1:
        c = (
            Line()
            .add_xaxis(X)
            .add_yaxis(names[0],Y1)
            .set_global_opts(toolbox_opts=opts.ToolboxOpts())
        )

    elif len(names) == 2:
        c = (
            Line()
            .add_xaxis(X)
            .add_yaxis(names[0],Y1)
            .add_yaxis(names[1],Y2)
            .set_global_opts(toolbox_opts=opts.ToolboxOpts())
        )

    elif len(names) == 3:
        c = (
            Line()
            .add_xaxis(X)
            .add_yaxis(names[0],Y1)
            .add_yaxis(names[1],Y2)
            .add_yaxis(names[2],Y3)
            .set_global_opts(toolbox_opts=opts.ToolboxOpts())
        )
        
    return c

def scatter_base() -> Scatter:
    if len(names) == 0:
        pass

    elif len(names) == 1:
        c = (
            Scatter()
            .add_xaxis(X)
            .add_yaxis(names[0],Y1)
            .set_global_opts(toolbox_opts=opts.ToolboxOpts())
        )

    elif len(names) == 2:
        c = (
            Scatter()
            .add_xaxis(X)
            .add_yaxis(names[0],Y1)
            .add_yaxis(names[1],Y2)
            .set_global_opts(toolbox_opts=opts.ToolboxOpts())
        )

    elif len(names) == 3:
        c = (
            Scatter()
            .add_xaxis(X)
            .add_yaxis(names[0],Y1)
            .add_yaxis(names[1],Y2)
            .add_yaxis(names[2],Y3)
            .set_global_opts(toolbox_opts=opts.ToolboxOpts())
        )
        
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

    print('before_url======',before_url)
    return redirect(before_url)