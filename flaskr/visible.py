from flask import Blueprint,request,render_template
from pyecharts import options as opts
from pyecharts.charts import Bar,Line,Scatter,Pie
from flaskr.db import get_db


bp = Blueprint('visible', __name__)


@bp.route('/barChart/<theme>',methods=('GET','POST'))
def barChart(theme):
    if request.method == 'POST':
        names = request.form.getlist('tablename')
        db = get_db()
        cur = db.cursor()
        datas = []
        for name in names:
            cur.execute('SELECT * FROM `{0}`'.format(name))
            datas.append(cur.fetchall())
        X = []
        Y = []
        for data in datas:
           
            for j in data :
                X.append(j['A'])
                Y.append(j['B'])

        # bar.add_xaxis(X)
        # bar.add_yaxis("商家A", Y)
        # bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
        # bar = Bar()
        bar = (
            Bar(init_opts=opts.InitOpts(theme=theme))
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [5, 20, 36, 10, 75, 90]) 
            .add_yaxis("商家B", [25, 36, 10, 75, 90]) 
            .set_global_opts(toolbox_opts=opts.ToolboxOpts(),datazoom_opts=[opts.DataZoomOpts()])
        )

    bar = (
            Bar(init_opts=opts.InitOpts(theme=theme))
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [5, 20, 36, 10, 75, 90]) 
            .add_yaxis("商家B", [25, 36, 10, 75, 90]) 
            .set_global_opts(toolbox_opts=opts.ToolboxOpts())
        )

    return render_template('pyecharts.html',myechart=bar.render_embed())



@bp.route('/lineChart/<theme>',methods=('GET','POST'))
def lineChart(theme):
    line = (
        Line(init_opts=opts.InitOpts(theme=theme))
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 10, 75, 90]) 
        .add_yaxis("商家B", [25, 36, 10, 75, 90]) 
        .set_global_opts(toolbox_opts=opts.ToolboxOpts())
    )

    return render_template('pyecharts.html',myechart=line.render_embed())
                           

@bp.route('/scatterChart/<theme>',methods=('GET','POST'))
def scatterChart(theme):
    scatter = (
        Scatter(init_opts=opts.InitOpts(theme=theme))
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 10, 75, 90]) 
        .add_yaxis("商家B", [25, 36, 10, 75, 90]) 
        .set_global_opts(toolbox_opts=opts.ToolboxOpts())
    )

    return render_template('pyecharts.html',myechart=scatter.render_embed())
