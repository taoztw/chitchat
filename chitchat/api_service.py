from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

app = create_app()


# 捕捉所有异常
@app.errorhandler(Exception)
def framework_error(e):
    # APIException
    # HTTPException
    # Exception
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 调试模式
        if not app.config['DEBUG']:
            return ServerError()
        else:
            return e


if __name__ == '__main__':
    app.run(debug=True, port=5005)
