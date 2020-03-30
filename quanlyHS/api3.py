from flask import Blueprint, render_template, url_for, redirect, flash, request
from quanlyHS.db import db
from quanlyHS.models import Tables
from quanlyHS.forms import Diemdanh
from wtforms import ValidationError
from sqlalchemy import and_

HS = Tables.HocSinh
DD = Tables.DiemDanh
Lop = Tables.LopHoc

bp = Blueprint('api3', __name__)


@bp.route("/diemdanh", methods=['POST', 'GET'])
def diemdanh():
    dd = Diemdanh()
    if request.method == 'GET' and len(request.args) == 0:
        return render_template('diemdanh.html', title='Home', dd=dd)

    if request.method == ('GET' or 'POST') and len(request.args) != 0:
        dict_ = dict(request.args)
        result = db.session.query(DD, HS).join(HS).filter(and_(DD.MaGV == dict_['MaGV'], HS.MaLop == dict_['MaLop'])).all()
        result = [i for i in result]
        return render_template('diemdanh.html', title='Home', dd=dd, result=result)



@bp.route("/hocsinh/update", methods=['GET', 'POST'])
def update():
    
    return redirect(url_for('api3.diemdanh'))

# tao form nhu diem danh cac cai can sua, submit ->> database
# , dien vao viet code vao