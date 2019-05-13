from flask import (
    Blueprint,request,render_template,
)
from flaskr.auth import login_required
from jinja2 import Markup
from pyecharts import options as opts
from pyecharts.charts import Bar,Line

from flaskr.db import get_db

bp = Blueprint('visible', __name__)


@bp.route('/doVisible',methods=('GET','POST'))
def doVisible():
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
        bar = Line()
        bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90]) 
        bar.add_yaxis("商家B", [25, 36, 10, 75, 90]) 
        bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题",),
                            toolbox_opts=opts.ToolboxOpts(),
                            datazoom_opts=[opts.DataZoomOpts()],)


    return render_template('pyecharts.html',
                           myechart=bar.render_embed(),
                           )
                           
    # return Markup(bar.render_embed())
