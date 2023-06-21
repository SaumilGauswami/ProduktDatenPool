import resources
from flask import Flask, redirect, url_for
from models import get_session
from utils.log_utils import config_logger
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from tables.product import SolarTable, User
from flask_login import current_user, LoginManager, login_user, logout_user


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))


def create_app():
    app = Flask('data_api_app')
    app.config.from_object('config')

    database_url = app.config.get('DATABASE_URL')
    if not database_url:
        raise Exception("Environment Exception: DATABASE_URL not set.")

    session = get_session(database_url)

    admin = Admin(app)
    # admin.add_view(MyModelView(SolarTable, session))
    admin.add_view(ModelView(User, session))

    config_logger(app)

    resources.create_api(app)

    def close_session(response_or_exc):
        session.remove()
        return response_or_exc

    app.teardown_request(close_session)
    app.teardown_appcontext(close_session)
    return app


main_app = create_app()

if __name__ == '__main__':
    main_app.run('0.0.0.0', 5009)

