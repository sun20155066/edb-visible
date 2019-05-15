from flask import (
    Blueprint, render_template,request
)
from flaskr.db import get_db
from flaskr.auth import login_required


bp = Blueprint('web', __name__)


@bp.route('/index')
@login_required
def index():
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
