from flask import Blueprint, render_template, url_for, redirect, flash
from quanlyHS.db import db
from quanlyHS.models import Tables
from quanlyHS.forms import Lophoc, HocSinh, Giaovien, Lichday
from wtforms import ValidationError


bp = Blueprint('api2', __name__)

@bp.route("/admin", methods=['POST', 'GET'])
def admin():
    return render_template('admin.html', title='Admin')

@bp.route("/admin/lophoc", methods=['POST', 'GET'])
def lophoc():
    new_lop = Lophoc()
    Lop = Tables.LopHoc
    if new_lop.validate_on_submit():
        if db.session.query(Lop).filter(Lop.MaLop==new_lop.MaLop.data).first():
            raise ValidationError('Ma lop is dublicate please use another')

        else:
            user = Lop(MaLop=new_lop.MaLop.data, GVCN=new_lop.GVCN.data, PhongHoc=new_lop.PhongHoc.data)
            db.session.add(user)
            db.session.commit()
            flash('insert suscessfull', 'success')
            return redirect(url_for('api2.admin/lophoc'))

    return render_template('malop.html', title='Home', new_lop=new_lop)


@bp.route("/admin/hocsinh", methods=['POST', 'GET'])
def hocsinh():
    hs = HocSinh()
    HS = Tables.HocSinh
    if hs.validate_on_submit():
        if db.session.query(HS).filter(HS.MaHS== hs.MaHS.data).first():
            raise ValidationError('Ma HS is dublicate please use another')

        else:
            user = HS(MaHS=hs.MaHS.data, TenHS=hs.TenHS.data, NgaySinh=hs.NgaySinh.data, GioiTinh=hs.GioiTinh.data,
                        PhuHuynh=hs.PhuHuynh.data, DiaChi=hs.DiaChi.data, SDT_PH=hs.SDT.data, 
                        MaLop=hs.MaLop.data, Email=hs.Email.data)
            db.session.add(user)
            db.session.commit()
            flash('insert suscessfull', 'success')
            return redirect(url_for('api2.admin/hocsinh'))

    return render_template('hocsinh.html', title='Home', hs=hs)


@bp.route("/admin/giaovien", methods=['POST', 'GET'])
def giaovien():
    gv = Giaovien()
    GV = Tables.GiaoVien
    if gv.validate_on_submit():
        if db.session.query(GV).filter(GV.MaGV== gv.MaGV.data).first():
            raise ValidationError('Ma GV is dublicate please use another')

        else:
            user = GV(MaGV=gv.MaGV.data, TenGV=gv.TenGV.data, NgaySinh=gv.NgaySinh.data, GioiTinh=gv.GioiTinh.data, 
                        Email=gv.Email.data)
            db.session.add(user)
            db.session.commit()
            flash('insert suscessfull', 'success')
            return redirect(url_for('api2.giaovien'))

    return render_template('giaovien.html', title='Home', gv=gv)


@bp.route("/admin/lichday", methods=['POST', 'GET'])
def lichday():
    ld = Lichday()
    LD = Tables.QuanLyLichDay
    if ld.validate_on_submit():
        user = LD(MaLop=ld.MaLop.data, MaGV=ld.MaGV.data, NamHoc=ld.NamHoc.data, KyHoc=ld.KyHoc.data, 
                  Monday=ld.Monday.data, Tuesday=ld.Tuesday.data, Thursday=ld.Thursday.data,
                  Friday=ld.Friday.data)
        db.session.add(user)
        db.session.commit()
        flash('insert suscessfull', 'success')
        return redirect(url_for('api2.lichday'))

    return render_template('lichday.html', title='Home', ld=ld)