from flask import Blueprint, render_template, url_for, redirect, flash, jsonify, request
from quanlyHS.db import db
from quanlyHS.models import Tables
from quanlyHS.forms import Diemdanh
from wtforms import ValidationError
from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from sqlalchemy import and_
import json

HS = Tables.HocSinh
DD = Tables.DiemDanh
Lop = Tables.LopHoc

bp = Blueprint('api3', __name__)


@bp.route("/diemdanh", methods=['POST', 'GET'])
def diemdanh():
    dd = Diemdanh()
    # if dd.validate_on_submit():
    #     result = db.session.query(DD, HS).join(HS).filter(and_(DD.MaGV == 'GV1', HS.MaLop == '6A1')).all()
    #     # dict_ = {}
    #     # for i in result:
    #     #     dictdcd
        

    #     return render_template('diemdanh.html', title='Home', dd=dd, result= result)
    MaGV = request.args['MaGV']
    MaLop = request.args['MaLop']
    print(MaGV, MaLop, type(MaGV), type(MaLop))
    return render_template('diemdanh.html', title='Home', dd=dd)



@bp.route("/index", methods=['POST', 'GET'])
def index(id):
    dd = Diemdanh()
    
    return render_template('diemdanh.html', title='Home', dd=dd)