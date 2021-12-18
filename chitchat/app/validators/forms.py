from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length
from app.libs.enums import ClientTypeEnum
# from app.models.user import User
from app.validators.base import BaseForm as Form


class ClientForm(Form):
    account = StringField(validators=[DataRequired(),
                                      length(min=1,max=32)
                                      ])
    secret = StringField()
    # type = IntegerField(validators=[(DataRequired)]) # 客户端类型
    type = 100


    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


# class UserEmailForm(ClientForm):
#     account = StringField(validators=[
#         Email(message='invalidate email')
#     ])
#     secret = StringField(validators=[
#         DataRequired(),
#         # password can only include letters , numbers and "_"
#         Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
#     ])
#     nickname = StringField(validators=[DataRequired(),
#                                        length(min=2, max=22)])
#
#     def validate_account(self, value):
#         if User.query.filter_by(email=value.data).first():
#             raise ValidationError()

class TranslateForm(Form):
    text = StringField(validators=[DataRequired()])
    src = StringField(validators=[DataRequired()])
    tgt = StringField(validators=[DataRequired()])

class BookSearchForm(Form):
    pass
