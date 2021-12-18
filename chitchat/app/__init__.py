from app.app import Flask
from flask_cors import CORS
def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


# def register_plugin(app):
#     from app.models.base import db
#     db.init_app(app)
#     with app.app_context():  # 手动将app 上下文入栈
#         db.create_all()


def create_app():
    """
    每一个项目都是一个app，app下面有两种配置文件 setting和secure
    将falsk核心对象的实例化放在app中，入口文件直接调用该方法返回的app对象，启动app
    :return:
    """
    app = Flask(__name__)
    cors = CORS(app)
    app.config.from_object("app.config.setting")
    app.config.from_object("app.config.secure")

    register_blueprints(app)
    # register_plugin(app)

    return app
