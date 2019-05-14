from flask import Blueprint,request,render_template
from pyecharts import options as opts
from pyecharts.charts import Bar,Line,Scatter,Pie
from flaskr.db import get_db
from random import randrange


bp = Blueprint('visible', __name__)


# @bp.route('/barChart/<theme>',methods=('GET','POST'))
# def barChart(theme):
#     if request.method == 'POST':
#         names = request.form.getlist('tablename')
#         db = get_db()
#         cur = db.cursor()
#         count = len(names)
#         Ycount = 0

#         if count == 0:
#             sqlparm = ''
            
#         elif count == 1:
#             sqlparm = 'SELECT `{0}`.A as date,`{0}`.B as `{0}` FROM `{0}`'.format(names[0])
#             cur.execute(sqlparm)
#             datas = cur.fetchall()

#             X = []
#             Y1 = []
#             Ycount = 1
#             for data in datas:
#                 X.append(data['date'])
#                 Y1.append(data[names[0]])

#             bar = Bar(init_opts=opts.InitOpts(theme=theme))
#             bar.add_yaxis(names[0], Y1)
#             bar.add_xaxis(X)
#             bar.set_global_opts(toolbox_opts=opts.ToolboxOpts())

            
#         elif count == 2:
#             sqlparm = ' SELECT `{0}`.A as date,`{0}`.B as `{0}`, `{1}`.B as `{1}` FROM `{0}`,`{1}` where `{0}`.A = `{1}`.A '.format(names[0],names[1])
#             cur.execute(sqlparm)
#             datas = cur.fetchall()

#             X = []
#             Y1 = []
#             Y2 = []
#             Ycount = 2
#             for data in datas:
#                 X.append(data['date'])
#                 Y1.append(data[names[0]])
#                 Y2.append(data[names[1]])

#             bar = Bar(init_opts=opts.InitOpts(theme=theme))
#             bar.add_yaxis(names[0], Y1)
#             bar.add_yaxis(names[1], Y2)
#             bar.add_xaxis(X)
#             bar.set_global_opts(toolbox_opts=opts.ToolboxOpts())

#         elif count == 3:
#             sqlparm = ' SELECT `{0}`.A as date,`{0}`.B as `{0}`, `{1}`.B as `{1}`, `{2}`.B as `{2}` FROM `{0}`,`{1}`,`{2}` where `{0}`.A = `{1}`.A and `{1}`.A = `{2}`.A '.format(names[0],names[1],names[2])
#             cur.execute(sqlparm)
#             datas = cur.fetchall()

#             X = []
#             Y1 = []
#             Y2 = []
#             Y3 = []
#             Ycount = 3
#             for data in datas:
#                 X.append(data['date'])
#                 Y1.append(data[names[0]])
#                 Y2.append(data[names[1]])
#                 Y3.append(data[names[2]])

#             bar = Bar(init_opts=opts.InitOpts(theme=theme))
#             bar.add_yaxis(names[0], Y1)
#             bar.add_yaxis(names[1], Y2)
#             bar.add_yaxis(names[2], Y3)
#             bar.add_xaxis(X)
#             bar.set_global_opts(toolbox_opts=opts.ToolboxOpts())
           

#         return render_template('pyecharts.html',myechart=bar.render_embed())



# @bp.route('/lineChart/<theme>',methods=('GET','POST'))
# def lineChart(theme):
#     line = (
#         Line(init_opts=opts.InitOpts(theme=theme))
#         .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#         .add_yaxis("商家A", [5, 20, 36, 10, 75, 90]) 
#         .add_yaxis("商家B", [25, 36, 10, 75, 90]) 
#         .set_global_opts(toolbox_opts=opts.ToolboxOpts())
#     )

#     return render_template('pyecharts.html',myechart=line.render_embed())
                           

# @bp.route('/scatterChart/<theme>',methods=('GET','POST'))
# def scatterChart(theme):
#     scatter = (
#         Scatter(init_opts=opts.InitOpts(theme=theme))
#         .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#         .add_yaxis("商家A", [5, 20, 36, 10, 75, 90]) 
#         .add_yaxis("商家B", [25, 36, 10, 75, 90]) 
#         .set_global_opts(toolbox_opts=opts.ToolboxOpts())
#     )

#     return render_template('pyecharts.html',myechart=scatter.render_embed())


def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c

def line_base() -> Line:
    c = (
        Line()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c

def scatter_base() -> Scatter:
    c = (
        Scatter()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
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



@bp.route("/visible/<chartType>/<theme>",methods=('GET','POST'))
def visible(chartType,theme):
    return render_template("pyecharts.html",operator=chartType,theme=theme)