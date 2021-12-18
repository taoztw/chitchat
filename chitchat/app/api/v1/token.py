from flask import current_app, jsonify
from app.libs.error_code import AuthFailed
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app.config.secure import USERNAME, PASSWORD

api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    identity = verity_user(form.data['account'], form.data['secret'])
    # Token
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'],
                                identity['account'],
                                expiration)
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201 # 201代表已经创建资源


def generate_auth_token(uid, ac_type,account, expiration=7200):
    """ 生成令牌 """
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'account': account
    })  # bytes类型的字符串

def verity_user(account, secret):
    if account == USERNAME and secret == PASSWORD:
        return {'uid': 1,'account':account}
    else:
        return AuthFailed()