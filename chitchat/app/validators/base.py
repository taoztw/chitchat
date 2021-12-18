from flask import request
from wtforms import Form
from app.libs.error_code import ParameterException

class BaseForm(Form):
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super().validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self