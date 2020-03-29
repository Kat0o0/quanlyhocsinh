from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import urllib

from quanlyHS.db import db

app = Flask(__name__, template_folder='template')
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# cai dat database
params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=LAPTOP-ENF51THV\SQLEXPRESS;DATABASE=CSDL_BTN;Trusted_Connection=yes;') # noqa
url_db = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_DATABASE_URI'] = url_db
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db.init_app(app)
db.app = app
# import models vao day
# xong db moi ceate duoc model
from quanlyHS.models import User # noqa
# db.create_all()
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'



from quanlyHS import api # noqa
from quanlyHS import api2 # noqa
from quanlyHS import api3
app.register_blueprint(api.bp)
app.register_blueprint(api2.bp)
app.register_blueprint(api3.bp)