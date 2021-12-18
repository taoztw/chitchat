from collections import namedtuple

from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer \
    as Setializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed, Forbidden
from app.libs.scope import is_in_scope


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(token, password):
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        # print('token_auth文件输出 user info',user_info)
        g.user = user_info
        return True


def verify_auth_token(token):
    s = Setializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    # 验证token的合法性， 时效性
    except BadSignature:
        raise AuthFailed(msg='token is invalid',
                         error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired',
                         error_code=1003)
    uid = data['uid']
    # ac_type = data['type']
    account = data['account']
    # scope = data['scope']
    # 这里可以拿到request请求对象
    # allow = is_in_scope(scope, request.endpoint) # 拿到请求要访问的试图函数
    # if not allow:
    #     raise Forbidden()
    return (uid, account)